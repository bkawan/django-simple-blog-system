# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simpleblog',
        'USER': 'password',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
DEFAULT_FROM_EMAIL = 'bikeshkawang@gmail.com'
SERVER_EMAIL = 'bikeshkawang@gmail.com'
ADMINS = [('bikesh kawan', 'bikeshkawang@gmail.com')]
MANAGERS = ADMINS
GOOGLE_SITE_VERIFICATION = 'hV4EwwprownATbXeq6IZCsdfsd3wEn83E4vAjL0owTzkK4l8'
FACEBOOK = {'page_link': "http://facebook.com/jsfigures"}
TWITTER = {'page_link': "http://facebook.com/jsfigures"}
GOOGLE = {'page_link': "http://facebook.com/jsfigures"}
COMPANY_NAME = 'JS Figures'
COMPANY_DESCRIPTION = "Daily news about using open source R for big data analysis, predictive modeling, data science, and visualization since 2008"

import dj_database_url

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
