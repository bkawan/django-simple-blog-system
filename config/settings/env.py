# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simpleblog',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

DEFAULT_FROM_EMAIL = 'bikeshkawang@gmail.com'
SERVER_EMAIL = 'bikeshkawang@gmail.com'
ADMINS = [('bikesh kawan', 'bikeshkawang@gmail.com')]
MANAGERS = ADMINS
GOOGLE_SITE_VERIFICATION = 'hV4EwwprownATbXeq6IZCsdfsd3wEn83E4vAjL0owTzkK4l8'
FACEBOOK = {'page_link': "http://facebook.com/healthmandu"}
TWITTER = {'page_link': "http://facebook.com/healthmandu"}
GOOGLE = {'page_link': "https://plus.google.com/103977365721792469348"}
COMPANY_NAME = 'Simple Blog System'
COMPANY_DESCRIPTION = "This is a simple blog system made with Django...If you like it, share and like...."

import dj_database_url

DATABASES['default'] = dj_database_url.config()
