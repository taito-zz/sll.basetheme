from Products.CMFCore.utils import getToolByName
from sll.basetheme.tests.base import IntegrationTestCase


def get_css_resource(obj, name):
    return getToolByName(obj, 'portal_css').getResource(name)


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_sll_basetheme_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('sll.basetheme'))

    def test_browserlayer(self):
        from sll.basetheme.browser.interfaces import ISllBasethemeLayer
        from plone.browserlayer import utils
        self.assertIn(ISllBasethemeLayer, utils.registered_layers())

    def test_cssregistry__jquerytools_dateinput__rendering(self):
        resource = get_css_resource(self.portal, '++resource++plone.app.jquerytools.dateinput.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__jquery_autocomplete__rendering(self):
        resource = get_css_resource(self.portal, '++resource++plone.formwidget.autocomplete/jquery.autocomplete.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_basetheme_main__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__sll_basetheme_main__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__sll_basetheme_main__compression(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__sll_basetheme_main__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__sll_basetheme_main__cookable(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__sll_basetheme_main__enabled(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__sll_basetheme_main__expression(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__sll_basetheme_main__media(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__sll_basetheme_main__rel(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__sll_basetheme_main__rendering(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_basetheme_main__title(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__sll_basetheme_extra__applyPrefix(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__sll_basetheme_extra__authenticated(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__sll_basetheme_extra__compression(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__sll_basetheme_extra__conditionalcomment(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__sll_basetheme_extra__cookable(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__sll_basetheme_extra__enabled(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__sll_basetheme_extra__expression(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getExpression(), '')

    def test_cssregistry__sll_basetheme_extra__media(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__sll_basetheme_extra__rel(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__sll_basetheme_extra__rendering(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__sll_basetheme_extra__title(self):
        resource = get_css_resource(self.portal, '++resource++sll.basetheme/css/extra.css')
        self.assertIsNone(resource.getTitle())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sll.basetheme:default'), u'2')

    def test_theme_skins(self):
        skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual(skins.getSkinPaths()[1][0], 'Sunburst Theme')

    def test_viewlets__plone_portalfooter(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"
        skinname = "*"
        self.assertEqual(storage.getHidden(manager, skinname), (
            u'plone.colophon',
            u'plone.footer',
            u'plone.site_actions',
            u'sll.basetheme.footer.message'))

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.basetheme'])
        self.assertFalse(installer.isProductInstalled('sll.basetheme'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.basetheme'])
        from sll.basetheme.browser.interfaces import ISllBasethemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISllBasethemeLayer, utils.registered_layers())
