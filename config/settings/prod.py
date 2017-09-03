# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'jsfigures.com', 'http://jsfigures.com/', 'www.jsfigures.com/', "*"]

HTTP_HOST_WITH_PROTOCOL = 'http://jsfigures.com/'
HTTP_HOST_NAME_WITH_PROTOCOL = 'http://jsfigures.com/'
# for you domain
FACEBOOK_APP_ID = '4445452121212319264308'

from .env import *
