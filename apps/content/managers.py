from django.db import models


DRAFT, PUBLISHED = "Draft", "Published"

SEARCH_FIELDS = ['title',
                 'content',
                 'tags',
                 'categories__title', ]


def contents_published(queryset):
    """
    This outside manager class, in order to make chainable queryset    
    :param queryset: 
    :return: Return only contents published
    """
    qs = queryset.filter(status=PUBLISHED)

    return qs


class ContentPublishedManager(models.Manager):
    """
    Manager to retrieve published contents.
    
    """

    def get_queryset(self):
        """
        :return: return published contents. 
        """

        return contents_published(super().get_queryset())

    def search(self, q):
        """ Base Search for all contens """

        return self.basic_search(q)

    def basic_search(self, q):
        """
        Basic Search
        :param q:
        :return:
        """

        lookup = None
        for query in q.split():
            query_part = models.Q()
            for field in SEARCH_FIELDS:
                """ Append all the query in query_part with or operator"""
                query_part |= models.Q(**{'{}__search'.format(field): query})
            if lookup is None:
                lookup = query_part
            else:
                lookup |= query_part

        return self.get_queryset().filter(lookup)


class ContentEntryRelatedPublishedManager(models.Manager):
    """
    Manager to retrieve objects associated with published entries.
    used for tag and category since they have associated related name entries
    """

    def get_queryset(self):
        """
        Return a queryset containing published entries.
        """
        return super().get_queryset().filter(
            entries__status=PUBLISHED).distinct()
