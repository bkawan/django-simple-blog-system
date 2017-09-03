from django.http import Http404
from django.views.generic import ListView
from tagging.models import Tag, TaggedItem
from tagging.utils import calculate_cloud, get_tag

from apps.content.models import ContentEntry


class TagListView(ListView):
    template_name = 'content/tag_list.html'

    def get_queryset(self):
        tags = Tag.objects.usage_for_queryset(
            ContentEntry.published.all(), counts=True)

        return calculate_cloud(tags, steps=6)


class BaseTagDetail(object):
    def get_queryset(self):
        self.tag = get_tag(self.kwargs['tag'])
        if self.tag is None:
            raise Http404("Matching tags not found".format(self.kwargs
                                                           ['tag']))
        return TaggedItem.objects.get_by_model(ContentEntry.published.all(), self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class TagDetail(BaseTagDetail, ListView):
    template_name = 'content/tag_detail.html'
    context_object_name = 'contents'
