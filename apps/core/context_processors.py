from django.conf import settings

from config.settings import COMPANY_NAME, COMPANY_DESCRIPTION

if settings.DEBUG:
    from config.settings.dev import (
        HTTP_HOST_NAME_WITH_PROTOCOL,
        FACEBOOK_APP_ID,
    )
else:
    from config.settings import (
        HTTP_HOST_NAME_WITH_PROTOCOL,
        FACEBOOK_APP_ID,
    )


def get_http_host_name_with_protocol(request):
    return {'HTTP_HOST_NAME_WITH_PROTOCOL': HTTP_HOST_NAME_WITH_PROTOCOL}


def get_facebook_app_id(request):
    return {'FACEBOOK_APP_ID': FACEBOOK_APP_ID}


def get_company_name(request):
    return {'COMPANY_NAME': COMPANY_NAME,
            'COMPANY_DESCRIPTION': COMPANY_DESCRIPTION
            }
