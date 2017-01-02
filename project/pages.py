# -*- coding: utf-8 -*-
"""
The project pages map for project
"""
from optimus.builder.pages import PageViewBase
from optimus.conf import settings

from project.sitemap import PageSitemap, tree_from_directory_structure


#sitemap_tree = tree_from_directory_structure(settings.TEMPLATES_DIR)
##sitemap_tree.show()


"""
Page objects
"""
class BasicPage(PageViewBase):
    """
    Basic page view
    """
    title = "Index"
    template_name = "index.html"
    destination = "index.html"


class PageWithSitemap(BasicPage):
    """
    Page view aware of sitemap
    """
    sitemap = {}

    def get_context(self):
        context = super(PageWithSitemap, self).get_context()

        context.update({
            'site_sitemap': self.sitemap,
        })
        return context


# Enabled pages to build
#PAGES = PageSitemap(sitemap_tree, PageWithSitemap).ressources
PAGES = [BasicPage()]
