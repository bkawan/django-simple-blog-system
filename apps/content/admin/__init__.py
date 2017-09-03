from django.contrib import admin

from apps.content.admin.content import ContentEntryAdmin
from apps.content.admin.category import CategoryAdmin
from apps.content.models import ContentEntry
from apps.content.models.category import Category

admin.site.register(Category, CategoryAdmin)
admin.site.register(ContentEntry, ContentEntryAdmin)
