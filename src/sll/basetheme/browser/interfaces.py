from Products.CMFPlone.browser.interfaces import INavigationTree
from collective.base.interfaces import IViewlet
from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager


# Browser layer

class ISllBasethemeLayer(Interface):
    """Marker interface for browserlayer."""


# Viewlet manager

class IAboveColumnsViewletManager(IViewletManager):
    """"""


# Viewlet

class ISiteActionsViewlet(IViewlet):
    """Viewlet interface for SiteActionsViewlet"""

    def actions():
        """Returns content listing of actions

        :rtype: content listing
        """


class IFooterInfoViewlet(IViewlet):
    """Viewlet interface for FooterInfoViewlet"""

    def items():
        """Returns list of dictionary of footer infos

        :rtype: list
        """

    def width():
        """Returns width for styling

        :rtype: str
        """


class IFooterSubfoldersViewlet(INavigationTree, IViewlet):
    """Viewlet interface for FooterSubfoldersViewlet"""

    def navigationTreeRootPath():
        """Returns path for navigation root

        :rtype: str
        """

    def navigationTree():
        """Returns list of dictionary of navigation tree components

        :rtype: list
        """

    def items():
        """Returns list of dictionary of navigation tree components + site map

        :rtype: list
        """


class IFooterMessageViewlet(IViewlet):
    """Viewlet interface for FooterMessageViewlet"""
