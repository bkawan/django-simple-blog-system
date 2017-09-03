from django.conf import settings
from django.db.models import Count
from django.template import Library

from apps.content.models import ContentEntry
from apps.content.models.category import Category

register = Library()


@register.inclusion_tag('appearance/tags/widgets/contents_recent.html')
def get_recent_contents(number=5):
    """
    Returt the most entries. By default it will return 5 entries.
    :param number:
    :return:
    """

    return {
        'contents': ContentEntry.published.all()[:number]
    }


@register.inclusion_tag('appearance/tags/widgets/categories.html')
def get_categories():
    return {
        'categories': Category.published_content_entries.all().annotate(
            count_published_content_entries=Count('entries')
        )
    }


@register.inclusion_tag('appearance/tags/widgets/archive.html')
def archive_posts():
    return {
        'dates': ContentEntry.objects.all().dates('publication_date', 'month')
    }


@register.inclusion_tag('appearance/tags/widgets/search_bar.html')
def get_search_bar():
    return {
        'company_name': settings.COMPANY_NAME
    }
