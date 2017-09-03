from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from apps.content.models import ContentEntry


class ContentEntryShortLink(RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        content_entry = get_object_or_404(ContentEntry.published, pk=int(kwargs['token'], 36))
        return content_entry.get_absolute_url()
