import math
import re
from urllib.parse import urlsplit

from django.conf import settings
from django.urls import reverse
from django.utils.html import strip_tags


def count_words(html_string):
    matching_words = re.findall(r'\w+', strip_tags(html_string))
    return len(matching_words)


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 200.0)  # assume 200wpm reading speed
    return int(read_time_min)


from random import randint


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


import string

# string.digits = "0123456789"
# string.ascii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

BASE36_ALPHABET = string.digits + string.ascii_uppercase


def base36(value):
    """
    Encode into base 36
    :param value: pk or any number
    :return: return base36
    """
    result = ""
    while value:
        # return quotient and remainder
        # until and unless the quotient ie the value is 0 it continues
        # value/36
        # eg 12/5 gives 2 , 3 ie quotient and remainder
        value, i = divmod(value, 36)
        # append to result until quotient is 0
        result = BASE36_ALPHABET[i] + result
    return result


def get_http_host_with_protocol(request=None):
    """
    by default request is none and it will return from http_host_with_protocol from settings
    :param request: request object
    :return: http_host_with_protocol eg http://example.com
    """
    if request:
        scheme = urlsplit(request.build_absolute_uri(None)).scheme
        # scheme = request.is_secure() and "https" or "http"
        if hasattr(request, 'META'):
            host = request.META.get('HTTP_HOST', None)
            if host:
                return '{}://{}'.format(scheme, host)
    return settings.HTTP_HOST_WITH_PROTOCOL


def get_url_shortener(object, reverse_short_link, request=None):
    host_name = get_http_host_with_protocol(request)
    return '{}{}'.format(host_name,
                         reverse(reverse_short_link,
                                 args=[base36(object.pk)]))
