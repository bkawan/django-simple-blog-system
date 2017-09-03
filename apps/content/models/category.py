from django.urls import reverse

from apps.content.managers import contents_published, ContentEntryRelatedPublishedManager
from apps.core.models.category import AbstractCategory


class Category(AbstractCategory):
    published_content_entries = ContentEntryRelatedPublishedManager()

    @staticmethod
    def get_all_categories():
        return Category.objects.select_related('parent')

    def get_absolute_url(self):
        return reverse('content:category_detail', kwargs={'path': self.tree_path})

    def contents_published(self):
        # self.entries is a queryset of content_entry of the category
        return contents_published(self.entries)
