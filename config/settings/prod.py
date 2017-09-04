# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'http://django-simple-blog.herokuapp.com', "*"]

HTTP_HOST_WITH_PROTOCOL = 'http://django-simple-blog.herokuapp.com'
HTTP_HOST_NAME_WITH_PROTOCOL = 'http://django-simple-blog.herokuapp.com'
# for you domain
FACEBOOK_APP_ID = '44451212452121212319264308'

from .env import *
