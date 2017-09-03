# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'simpleblog',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',

    }
}

#
DEFAULT_FROM_EMAIL = 'bikeshkawang@gmail.com'
SERVER_EMAIL = 'bikeshkawang@gmail.com'
ADMINS = [('bikesh kawan', 'bikeshkawang@gmail.com')]
MANAGERS = ADMINS
GOOGLE_SITE_VERIFICATION = 'hV4EwwprownATbXeq6IZCsdfsd3wEn83E4vAjL0owTzkK4l8'
DISCUSS_URL = 'https://example.disqus.com/'
FACEBOOK = {'page_link': "http://facebook.com/jsfigures"}
TWITTER = {'page_link': "http://facebook.com/jsfigures"}
GOOGLE = {'page_link': "http://facebook.com/jsfigures"}
COMPANY_NAME = 'JS Figures'
COMPANY_DESCRIPTION = "Daily news about using open source R for big data analysis, predictive modeling, data science, and visualization since 2008"
