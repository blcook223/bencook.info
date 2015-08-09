from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class PagesSitemap(Sitemap):
    """
    Sitemap for pages in site
    """
    changefreq = 'weekly'
    priority = 0.5

    def __init__(self, pages):
        self.pages = pages

    def items(self):
        """
        Return all pages
        """
        return self.pages

    def location(self, obj):
        return reverse(obj)
