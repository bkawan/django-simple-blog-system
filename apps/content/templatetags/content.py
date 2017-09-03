from django.template import Library
from django.urls import reverse
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def get_root_categories_badges_display(root_categories):
    badges = ''
    for category in root_categories:
        badges += '''<a href="{}"> <span class="badge badge-success">{}</span></a> '''.format(
            category.get_absolute_url(),
            category.title)

    return mark_safe(badges)


@register.simple_tag
def get_categories_badges_display(categories):
    badges = ''
    for category in categories:
        # hex_color = random_with_N_digits(6)
        badges += '''<a href="{}"> <span>{}</span></a> '''.format(
            category.get_absolute_url(),
            category.title
        )
    return mark_safe(badges)


@register.simple_tag
def get_tags_badges_display(tags):
    badges = ''
    for tag in tags:
        tag_detail = reverse('content:tag_detail', kwargs={'tag': tag})
        tag_detail_link = '''<a href="{}" title="{}" class="text-black">{}</a>'''.format(tag_detail, tag, tag)
        badges += '''<span class="text-muted">{}</span> '''.format(
            tag_detail_link
        )

    return mark_safe(badges)
