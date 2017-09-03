from django.views.generic import DetailView

from apps.content.models import ContentEntry


class ContentDateDetail(DetailView):
    model = ContentEntry
    template_name = 'content/content_detail.html'

    def get_queryset(self):
        return super().get_queryset().select_related('user').prefetch_related('categories')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=None)
        if obj:
            obj.visit_count += 1
            obj.save()

        return obj
