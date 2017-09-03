from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.content.models_bases.content import AbstractEntry, PUBLISHED


class ContentEntry(AbstractEntry):
    @staticmethod
    def get_all_entries():
        queryset = ContentEntry.objects.filter(status=PUBLISHED).order_by('-id', '-publication_date').select_related(
            'user').prefetch_related(
            'categories'
        )
        return queryset


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = ContentEntry.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "{}-{}".format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=ContentEntry)
