from django.conf.urls import url

from apps.content.views.categories import CategoryListView, CategoryDetailView
from apps.content.views.contents import ContentDateDetail
from apps.content.views.search import ContentEntrySearch
from apps.content.views.tags import TagListView, TagDetail
from apps.content.views.archive import BlogMonthArchiveView

app_name = 'content'

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        ContentDateDetail.as_view(),
        name='content_entry_detail'),
    url(r'^search/$', ContentEntrySearch.as_view(), name='content_entry_search'),

]

urlpatterns += [
    url(r'^categories/$', CategoryListView.as_view(), name='categories'),
    url(r'^categories/(?P<path>[-\/\w]+)/$', CategoryDetailView.as_view(), name='category_detail'),
]

urlpatterns += [
    url(r'^tags/$', TagListView.as_view(), name='tag_list'),
    url(r'^tags/(?P<tag>[^/]+(?u))/$', TagDetail.as_view(), name='tag_detail'),
]

urlpatterns += [
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        BlogMonthArchiveView.as_view(),
        name='archive_month'),
]
