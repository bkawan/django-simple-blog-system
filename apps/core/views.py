from django.views.generic import ListView

# Create your views here.
from apps.content.models import ContentEntry
from apps.core.constants import PUBLISHED


class LandingPageView(ListView):
    model = ContentEntry
    template_name = 'pages/landing_page.html'
    paginate_by = 8
    context_object_name = 'contents'

    def get_queryset(self):
        return super().get_queryset().filter(status=PUBLISHED)
