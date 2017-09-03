from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from apps.content.models.category import Category


def get_category_or_404(path):
    """
    Retrieve a Category Instance
    find slug of the category by splitting the category path
    :param path: path of the category
    :return: return Category
    """
    path_bits = [p for p in path.split('/') if p]
    return get_object_or_404(Category, slug=path_bits[-1])


class CategoryListView(ListView):
    template_name = 'content/category_list.html'

    def get_queryset(self):
        return Category.objects.all().annotate(count_contents_published=Count('entries'))


class BaseCategoryDetail(object):
    def get_queryset(self):
        """

        :return: Contents published of the related categories
        """

        self.category = get_category_or_404(self.kwargs['path'])

        return self.category.contents_published  # return all the queries containing content_entry ie related name entries

    def get_context_data(self, **kwargs):
        """

        :param kwargs:
        :return: current category in context
        """

        context = super().get_context_data(**kwargs)
        context['category'] = self.category

        return context


class CategoryDetailView(BaseCategoryDetail, ListView):
    template_name = 'content/category_content_list.html'
    context_object_name = 'contents'
