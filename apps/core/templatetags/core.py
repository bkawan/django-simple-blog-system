import re
from math import ceil

from django.conf import settings
from django.template import Library

from apps.util.default import get_http_host_with_protocol as _get_http_host_with_protocol

register = Library()


# TODO @bikesh "not in use"
@register.inclusion_tag('core/tags/pagination.html')
def pagination(is_paginated, page_obj, paginator, link=None):
    return {
        'is_paginated': is_paginated,
        'page_obj': page_obj,
        'paginator': paginator
    }


@register.inclusion_tag('core/tags/connect_to_social_page.html')
def connect_to_social_page():
    social_page_link = {
        'facebook': settings.FACEBOOK['page_link'],
        'google': settings.GOOGLE['page_link'],
        'twitter': settings.TWITTER['page_link']
    }

    return {"social_page_link": social_page_link}


@register.simple_tag
def get_http_host_with_protocol(request=None):
    return _get_http_host_with_protocol(request=request)


