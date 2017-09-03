from django.conf.urls import url

from apps.content.views.short_link import ContentEntryShortLink
# from apps.slide.views.short_link import GoogleSlideShortLink
from .views import LandingPageView

app_name = 'core'
urlpatterns = [
    url(r'^$', view=LandingPageView.as_view(), name='landing_page'),
    url(r'^(?P<token>[\dA-Z]+)/$',
        ContentEntryShortLink.as_view(),
        name='content_entry_short_link'),

]
