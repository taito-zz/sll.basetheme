from Acquisition import aq_inner
from Products.ATContentTypes.interfaces import IATDocument
from Products.ATContentTypes.interfaces import IATFolder
from Products.CMFPlone.browser.navtree import NavtreeQueryBuilder
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.base.interfaces import IAdapter
from decimal import Decimal
from decimal import ROUND_DOWN
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.root import getNavigationRoot
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from sll.basetheme.browser.interfaces import IFooterInfoViewlet
from sll.basetheme.browser.interfaces import IFooterMessageViewlet
from sll.basetheme.browser.interfaces import IFooterSubfoldersViewlet
from sll.basetheme.browser.interfaces import ISiteActionsViewlet
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.interface import implements


_ = MessageFactory("plone")


class SiteActionsViewlet(ViewletBase):
    """Global viewlet
    Shows site actions
    """
    implements(ISiteActionsViewlet)
    index = ViewPageTemplateFile('viewlets/site-actions.pt')

    @view.memoize
    def actions(self):
        """Returns content listing of actions

        :rtype: content listing
        """
        portal_state = self.context.restrictedTraverse('@@plone_portal_state')
        path = '{}/site-actions'.format(portal_state.navigation_root_path())
        return IAdapter(self.context).get_content_listing(IATFolder, path=path, depth=1, sort_on='getObjPositionInParent')
        # portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        # catalog = getToolByName(context, 'portal_catalog')
        # query = {
        #     'object_provides': IATFolder.__identifier__,
        #     'path': {
        #         'query': '{}/site-actions'.format(portal_state.navigation_root_path()),
        #         'depth': 1,
        #     },
        #     'sort_on': 'getObjPositionInParent',
        # }
        # res = catalog(query)
        # return IContentListing(res)


class FooterInfoViewlet(ViewletBase):
    """Global viewlet
    Show footer info
    """
    implements(IFooterInfoViewlet)
    index = ViewPageTemplateFile('viewlets/footer-info.pt')

    @view.memoize
    def items(self):
        """Returns list of dictionary of footer infos

        :rtype: list
        """
        # portal_state = self.context.restrictedTraverse('@@plone_portal_state')
        # context = aq_inner(self.context)
        # portal_state = getMultiAdapter((context, self.request), name="plone_portal_state")
        # portal_path = '/'.join(portal_state.portal().getPhysicalPath())
        # catalog = getToolByName(context, 'portal_catalog')
        # query = {
        #     'object_provides': IATDocument.__identifier__,
        #     'path': {
        #         'query': '{}/footer-info'.format(portal_path),
        #         'depth': 1,
        #     },
        #     'sort_on': 'getObjPositionInParent',
        # }
        # items = [{
        #     'id': item.id,
        #     'title': item.Title(),
        #     'url': item.getURL(),
        #     'description': item.Description(),
        #     'text': item.getObject().CookedBody(),
        # } for item in IContentListing(catalog(query))]
        # return items
        res = []
        adapter = IAdapter(self.context)
        path = '{}/footer-info'.format(adapter.portal_path())
        for item in adapter.get_content_listing(IATDocument, path=path, depth=1, sort_on='getObjPositionInParent'):
            res.append({
                'id': item.id,
                'title': item.Title(),
                'url': item.getURL(),
                'description': item.Description(),
                'text': item.getObject().CookedBody(),
            })
        return res

    @view.memoize
    def width(self):
        """Returns width for styling

        :rtype: str
        """
        return 'width: {}%'.format(
            (Decimal(100) / Decimal(len(self.items()))).quantize(Decimal('.01'), rounding=ROUND_DOWN))


class FooterSubfoldersViewlet(ViewletBase):
    """Global viewlet
    Shows footer subfolders
    """
    # grok.implements(INavigationTree)
    implements(IFooterSubfoldersViewlet)
    index = ViewPageTemplateFile('viewlets/footer-subfolders.pt')

    @view.memoize
    def navigationTreeRootPath(self):
        """Returns path for navigation root

        :rtype: str
        """
        return getNavigationRoot(self.context)

    @view.memoize
    def navigationTree(self):
        """Returns list of dictionary of navigation tree components

        :rtype: list
        """
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
        """Returns list of dictionary of navigation tree components + site map

        :rtype: list
        """
        items = self.navigationTree()
        items.append({
            'Title': _(u'Site Map'),
            'getURL': '{}/sitemap'.format(self.navigationTreeRootPath()),
            'children': [],
        })
        return items


class FooterMessageViewlet(ViewletBase):
    """Global viewlet
     Shows footer message"""
    implements(IFooterMessageViewlet)
    index = ViewPageTemplateFile('viewlets/footer-message.pt')


# class AboveColumnsViewletManager(grok.ViewletManager):
#     """Viewlet Manager for Carousel"""
#     grok.context(INavigationRoot)
#     grok.implements(IAboveColumnsViewletManager)
#     grok.layer(ISllBasethemeLayer)
#     grok.name('sll.basetheme.above.columns')
