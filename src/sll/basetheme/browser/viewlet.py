from Acquisition import aq_inner
from Products.ATContentTypes.interfaces import IATDocument
from Products.ATContentTypes.interfaces import IATFolder
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.browser.interfaces import INavigationTree
from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder
from decimal import Decimal
from decimal import ROUND_DOWN
from five import grok
from plone.app.contentlisting.interfaces import IContentListing
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.viewlets.interfaces import IPortalFooter
from plone.app.layout.viewlets.interfaces import IPortalHeader
from plone.memoize import view
from sll.basetheme.browser.interfaces import ISllBasethemeLayer
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface


_ = MessageFactory("plone")


grok.templatedir('viewlets')


class BaseViewlet(grok.Viewlet):
    """Base class for viewlet"""
    grok.baseclass()
    grok.context(Interface)
    grok.layer(ISllBasethemeLayer)
    grok.require('zope2.View')


class SiteActionsViewlet(BaseViewlet):
    """Viewlet class to show site actions"""
    grok.name('plone.site_actions')
    grok.template('site-actions')
    grok.viewletmanager(IPortalHeader)

    @view.memoize
    def actions(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': IATFolder.__identifier__,
            'path': {
                'query': '{}/site-actions'.format(portal_state.navigation_root_path()),
                'depth': 1,
            },
            'sort_on': 'getObjPositionInParent',
        }
        res = catalog(query)
        return IContentListing(res)


class FooterInfoViewlet(BaseViewlet):
    """Viewlet class to show footer info"""
    grok.name('sll.basetheme.footer.info')
    grok.template('footer-info')
    grok.viewletmanager(IPortalFooter)

    @view.memoize
    def items(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        catalog = getToolByName(context, 'portal_catalog')
        query = {
            'object_provides': IATDocument.__identifier__,
            'path': {
                'query': '{}/footer-info'.format(portal_state.navigation_root_path()),
                'depth': 1,
            },
            'sort_on': 'getObjPositionInParent',
        }
        items = [{
            'id': item.id,
            'title': item.Title(),
            'url': item.getURL(),
            'description': item.Description(),
            'text': item.getObject().CookedBody(),
        } for item in IContentListing(catalog(query))]
        return items

    @view.memoize
    def width(self):
        return 'width: {}%'.format(
            (Decimal(100) / Decimal(len(self.items()))).quantize(Decimal('.01'), rounding=ROUND_DOWN))


class FooterSubfoldersViewlet(BaseViewlet):
    """Viewlet class to show footer subfolders."""
    grok.implements(INavigationTree)
    grok.name('sll.basetheme.footer.subfolders')
    grok.template('footer-subfolders')
    grok.viewletmanager(IPortalFooter)

    @view.memoize
    def navigationTreeRootPath(self):
        return getNavigationRoot(self.context)

    @view.memoize
    def navigationTree(self):
        context = aq_inner(self.context)
        query = NavtreeQueryBuilder(context)()
        query['path'] = {
            'query': self.navigationTreeRootPath(),
            'depth': 2,
        }
        strategy = getMultiAdapter((context, self), INavtreeStrategy)
        return buildFolderTree(context, obj=context, query=query, strategy=strategy)['children']

    @view.memoize
    def items(self):
        items = self.navigationTree()
        items.append({
            'Title': _(u'Site Map'),
            'getURL': '{}/sitemap'.format(self.navigationTreeRootPath()),
            'children': [],
        })
        return items