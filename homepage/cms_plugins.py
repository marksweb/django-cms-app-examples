__author__ = 'mwalker'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from .forms import HomeMultiArticleAdminForm, HomeFullArticleAdminForm
from .models import HomeMultiArticle, HomeFullArticle


class HomeMultiArticlePlugin(CMSPluginBase):
    """
    Plugin for multi-article homepage blocks.
    """
    model = HomeMultiArticle
    name = _("Multi article")
    form = HomeMultiArticleAdminForm
    render_template = "multi_article.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


class HomeFullArticlePlugin(CMSPluginBase):
    """
    Plugin for full width homepage articles.
    """
    model = HomeFullArticle
    name = _("Full width article")
    form = HomeFullArticleAdminForm
    render_template = "full_article.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(HomeMultiArticlePlugin)
plugin_pool.register_plugin(HomeFullArticlePlugin)