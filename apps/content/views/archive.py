from django.views.generic.dates import MonthArchiveView
from apps.content.models.content import ContentEntry

class BlogMonthArchiveView(MonthArchiveView):
    paginate_by = 10
    date_field = 'publication_date'
    template_name = 'content/archive_month.html'
    queryset = ContentEntry.published.all()
    context_object_name = 'contents'
