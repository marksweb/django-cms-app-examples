__author__ = 'mwalker'

from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import ugettext_lazy as _


class HomeMultiArticle(CMSPlugin):
    """
    Home page articles, displayed in two columns.
    """
    left_title_1 = models.CharField(
        _("Left side, Slide 1 Title"),
        max_length=80
    )
    left_text_1 = models.TextField(
        _("Left side, Slide 1 Content")
    )
    left_url_1 = models.CharField(
        _("Left side, Slide 1 Link"),
        max_length=255
    )

    left_title_2 = models.CharField(
        _("Left side, Slide 2 Title"),
        max_length=80,
        blank=True
    )
    left_text_2 = models.TextField(
        _("Left side, Slide 2 Content"),
        blank=True
    )
    left_url_2 = models.CharField(
        _("Left side, Slide 2 Link"),
        max_length=255,
        blank=True
    )

    left_title_3 = models.CharField(
        _("Left side, Slide 3 Title"),
        max_length=80,
        blank=True
    )
    left_text_3 = models.TextField(
        _("Left side, Slide 3 Content"),
        blank=True
    )
    left_url_3 = models.CharField(
        _("Left side, Slide 3 Link"),
        max_length=200,
        blank=True
    )

    left_title_4 = models.CharField(
        _("Left side, Slide 4 Title"),
        max_length=80,
        blank=True
    )
    left_text_4 = models.TextField(
        _("Left side, Slide 4 Content"),
        blank=True
    )
    left_url_4 = models.CharField(
        _("Left side, Slide 4 Link"),
        max_length=255,
        blank=True
    )

    left_title_5 = models.CharField(
        _("Left side, Slide 5 Title"),
        max_length=80,
        blank=True
    )
    left_text_5 = models.TextField(
        _("Left side, Slide 5 Content"),
        blank=True
    )
    left_url_5 = models.CharField(
        _("Left side, Slide 5 Link"),
        max_length=255,
        blank=True
    )

    left_title_6 = models.CharField(
        _("Left side, Slide 6 Title"),
        max_length=80,
        blank=True
    )
    left_text_6 = models.TextField(
        _("Left side, Slide 6 Content"),
        blank=True
    )
    left_url_6 = models.CharField(
        _("Left side, Slide 6 Link"),
        max_length=255,
        blank=True
    )

    right_title_1 = models.CharField(
        _("Right side, Slide 1 Title"),
        max_length=80
    )
    right_text_1 = models.TextField(
        _("Right side, Slide 1 Content")
    )
    right_url_1 = models.CharField(
        _("Right side, Slide 1 Link"),
        max_length=255,
    )

    right_title_2 = models.CharField(
        _("Right side, Slide 2 Title"),
        max_length=80,
        blank=True
    )
    right_text_2 = models.TextField(
        _("Right side, Slide 2 Content"),
        blank=True
    )
    right_url_2 = models.CharField(
        _("Right side, Slide 2 Link"),
        max_length=255,
        blank=True
    )

    right_title_3 = models.CharField(
        _("Right side, Slide 3 Title"),
        max_length=80,
        blank=True
    )
    right_text_3 = models.TextField(
        _("Right side, Slide 3 Content"),
        blank=True
    )
    right_url_3 = models.CharField(
        _("Right side, Slide 3 Link"),
        max_length=255,
        blank=True
    )

    right_title_4 = models.CharField(
        _("Right side, Slide 4 Title"),
        max_length=80,
        blank=True
    )
    right_text_4 = models.TextField(
        _("Right side, Slide 4 Content"),
        blank=True
    )
    right_url_4 = models.CharField(
        _("Right side, Slide 4 Link"),
        max_length=255,
        blank=True
    )

    right_title_5 = models.CharField(
        _("Right side, Slide 5 Title"),
        max_length=80,
        blank=True
    )
    right_text_5 = models.TextField(
        _("Right side, Slide 5 Content"),
        blank=True
    )
    right_url_5 = models.CharField(
        _("Right side, Slide 5 Link"),
        max_length=255,
        blank=True
    )

    right_title_6 = models.CharField(
        _("Right side, Slide 6 Title"),
        max_length=80,
        blank=True
    )
    right_text_6 = models.TextField(
        _("Right side, Slide 6 Content"),
        blank=True
    )
    right_url_6 = models.CharField(
        _("Right side, Slide 6 Link"),
        max_length=255,
        blank=True
    )

    def __unicode__(self):
        return "First item left: {} - First item right: {}".format(
            self.left_title_1, self.right_title_1
        )


class HomeFullArticle(CMSPlugin):
    """
    Full width news articles for the home page.
    """
    title_1 = models.CharField(
        _("Slide 1 Title"),
        max_length=80
    )
    text_1 = models.TextField(
        _("Slide 1 Content")
    )
    url_1 = models.CharField(
        _("Slide 1 URL"),
        max_length=255)

    title_2 = models.CharField(
        _("Slide 2 Title"),
        max_length=80,
        blank=True
    )
    text_2 = models.TextField(
        _("Slide 2 Content"),
        blank=True
    )
    url_2 = models.CharField(
        _("Slide 2 URL"),
        max_length=255,
        blank=True
    )

    title_3 = models.CharField(
        _("Slide 3 Title"),
        max_length=80,
        blank=True
    )
    text_3 = models.TextField(
        _("Slide 3 Content"),
        blank=True
    )
    url_3 = models.CharField(
        _("Slide 3 URL"),
        max_length=255,
        blank=True
    )

    title_4 = models.CharField(
        _("Slide 4 Title"),
        max_length=80,
        blank=True
    )
    text_4 = models.TextField(
        _("Slide 4 Content"),
        blank=True
    )
    url_4 = models.CharField(
        _("Slide 4 URL"),
        max_length=255,
        blank=True
    )

    title_5 = models.CharField(
        _("Slide 5 Title"),
        max_length=80,
        blank=True
    )
    text_5 = models.TextField(
        _("Slide 5 Content"),
        blank=True
    )
    url_5 = models.CharField(
        _("Slide 5 URL"),
        max_length=255,
        blank=True
    )

    title_6 = models.CharField(
        _("Slide 6 Title"),
        max_length=80,
        blank=True
    )
    text_6 = models.TextField(
        _("Slide 6 Content"),
        blank=True
    )
    url_6 = models.CharField(
        _("Slide 6 URL"),
        max_length=255,
        blank=True
    )

    def __unicode__(self):
        return u"First item: {title1}".format(title1=self.title_1)
