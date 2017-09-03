from django.contrib import admin
from django.core.urlresolvers import NoReverseMatch
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _



class CategoryAdmin(admin.ModelAdmin):
    """
    Admin for Category model.
    """
    fields = ('title', 'parent', 'description', 'slug')
    # list_display = ('title', 'slug', 'get_tree_path', 'description')
    list_display = ('title', 'slug', 'description')

    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'description')
    list_filter = ('parent',)

