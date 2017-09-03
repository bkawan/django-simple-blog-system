import os

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField
from tagging.fields import TagField
from tagging.utils import parse_tag_input

from apps.content.managers import ContentPublishedManager
from apps.content.models.category import Category
from apps.content.utils.default import get_url_shortener
from apps.util.default import count_words, get_read_time

DRAFT, PUBLISHED = "Draft", "Published"
STATUS_CHOICES = (
    (DRAFT, DRAFT),
    (PUBLISHED, PUBLISHED),
    ('Trashed', 'Trashed'),
    ('Hidden', 'Hidden'),
    ('Archived', 'Archived'),
)


class CoreEntry(models.Model):
    """
    Abstract core Content entry model class providing
    the fields and methods required for publishing
    content over time.
    """

    title = models.CharField(
        _('title'), max_length=255, help_text="Full title of the Content Entry")

    slug = models.SlugField(
        _('slug'), max_length=255,
        unique_for_date='publication_date',
        help_text=_("Used to build the Content entry's URL."))

    status = models.CharField(
        _('status'), db_index=True, max_length=20,
        choices=STATUS_CHOICES, default=DRAFT)
    publication_date = models.DateTimeField(
        _('publication date'),
        db_index=True, default=timezone.now,
        help_text=_("Used to build the entry's URL."))

    created_at = models.DateTimeField(
        _('creation date'), default=timezone.now)

    updated_at = models.DateTimeField(_('update at'), default=timezone.now)

    objects = models.Manager()
    published = ContentPublishedManager()

    @property
    def previous_entry(self):
        """
        Returns the previous published entry if exists.
        """
        return self.previous_next_entries[0]

    @property
    def next_entry(self):
        """
        Returns the next published entry if exists.
        """
        return self.previous_next_entries[1]

    @property
    def short_url(self):
        """
        Returns the entry's short url.
        """

        return get_url_shortener(self)

    @property
    def category_list(self):
        if self.categories.all():
            return [category.title for category in self.categories.all()]
        return ['General']

    @property
    def all_categories(self):
        return self.categories.all()

    @property
    def root_category_list(self):
        if self.categories.all():
            return set([category.get_root().title for category in self.categories.all()])
        return ['General']

    @property
    def root_categories(self):
        return set([category.get_root() for category in self.categories.all()])

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the
        the updated_at field.
        """
        self.updated_at = timezone.now()
        super(CoreEntry, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """

        publication_date = self.publication_date
        if timezone.is_aware(publication_date):
            publication_date = timezone.localtime(publication_date)
        return ('content:content_entry_detail', (), {
            'year': publication_date.strftime('%Y'),
            'month': publication_date.strftime('%m'),
            'day': publication_date.strftime('%d'),
            'slug': self.slug})

    def __str__(self):
        return '%s: %s' % (self.title, self.status)

    class Meta:
        """
        CoreEntry's meta information.
        """
        abstract = True
        ordering = ['-publication_date']
        get_latest_by = 'publication_date'
        verbose_name = _('Content Entry')
        verbose_name_plural = _('Content Entries')
        index_together = [['slug', 'publication_date'],
                          ['status', 'publication_date',
                           ]]


class ContentEntry(models.Model):
    """
    Abstract ContentEntry Model class providing field and methods to
    write short and full description of the content inside entry;
    """
    content = RedactorField(help_text='Full Description of the Content')

    class Meta:
        abstract = True

    @property
    def word_count(self):
        """

        :return: total word of the content
        """
        return count_words(self.content)

    @property
    def read_time(self):
        """

        :return: read time for cotent in minutes
        """
        return get_read_time(self.content)


def image_upload_to(instance, filename):
    """Store image in the directory of it's class name."""
    class_name = instance.__class__.__name__
    upload_to = 'uploads/images/{}'.format(class_name)
    now = timezone.now()
    filename, extension = os.path.splitext(filename)
    path = os.path.join(upload_to,
                        now.strftime('%Y'),
                        now.strftime('%m'),
                        now.strftime('%d'),
                        '{}{}'.format(slugify(filename), extension))

    return path


class ImageEntry(models.Model):
    image = models.ImageField(
        _('image'), blank=True,
        upload_to=image_upload_to,
        help_text=_('Featured Image for the Content'))

    image_caption = models.TextField(
        _('caption'), blank=True,
        help_text=_("Image's caption."))

    image_source = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class CategoriesEntry(models.Model):
    """
    Abstract model class to categorize the entries.
    """
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='entries',
        verbose_name=_('categories'))

    class Meta:
        abstract = True


class TagsEntry(models.Model):
    """
    Abstract model class to add tags to the entries.
    """
    tags = TagField(_('tags'))

    @property
    def tags_list(self):
        """
        Return iterable list of tags.
        """
        return parse_tag_input(self.tags)

    class Meta:
        abstract = True


class UserEntry(models.Model):
    """
    Abstract model class to add relationship
    between the entries and their user.
    """
    user = models.ForeignKey(
        User,
        related_name='entries',
        verbose_name=_('User'))

    class Meta:
        abstract = True


class ContentSourcesEntry(models.Model):
    """ Source of the Content"""

    content_source = RedactorField(
        blank=True,
        null=True,
        help_text='Reference and the source of the content'
    )

    class Meta:
        abstract = True
        verbose_name = _('Content Source')
        verbose_name_plural = _('Content Sources')


class VisitCount(models.Model):
    visit_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


class AbstractEntry(
    CoreEntry,
    ContentEntry,
    ContentSourcesEntry,
    ImageEntry,
    CategoriesEntry,
    TagsEntry,
    VisitCount,
    UserEntry):
    """
    
    Final abstract entry model class assembling
    all the abstract entry model classes into a single one.

    In this manner we can override some fields without
    reimplemting all the AbstractEntry.
    """

    class Meta(CoreEntry.Meta):
        abstract = True
