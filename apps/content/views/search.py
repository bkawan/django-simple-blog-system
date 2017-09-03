from django.views.generic import ListView

from apps.content.models import ContentEntry


class BaseContentEntrySearch(object):
    q = ''
    error = None

    def get_queryset(self):
        contents = ContentEntry.published.none()

        if self.request.GET:
            self.q = self.request.GET.get('q', '').strip()
            if self.q:
                if not self.q[0:2].isalnum() and not len(self.q) > 2:
                    self.error = "Search Field must be at least 3 character and starts with alpha or alphanumeric"
                else:
                    contents = ContentEntry.published.search(self.q).distinct()
            else:

                contents = ContentEntry.published.all()
        else:
            self.error = "This is no search Query, please check search  parameter in url"

        return contents

    def get_context_data(self, **kwargs):
        """
        Add Extra data to context ie error and pattern
        :param kwargs: query parameter
        :return: context object
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'error': self.error, 'q': self.q, 'total_query': self.get_queryset().count()
        })
        return context


class ContentEntrySearch(BaseContentEntrySearch, ListView):
    template_name = 'content/content_search.html'
    paginate_by = 1
    context_object_name = 'contents'

    def get_context_data(self, **kwargs):
        return super().get_context_data()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('categories').select_related('user')
