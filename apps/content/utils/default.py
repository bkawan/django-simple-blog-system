from django.urls import reverse

from apps.util.default import base36, get_http_host_with_protocol


def get_url_shortener(entry, request=None):
    host_name = get_http_host_with_protocol(request)
    return '{}{}'.format(host_name,
                         reverse('core:content_entry_short_link',
                                 args=[base36(entry.pk)]))
