from django.contrib import admin


class ContentEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    exclude = ['visit_count', 'updated_at', 'created_at']
