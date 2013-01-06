from Products.CMFCore.utils import getToolByName
from sll.basetheme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_remove_css__one_css(self):
        css = getToolByName(self.portal, 'portal_css')
        self.assertIsNotNone(css.getResource('base.css'))

        from sll.basetheme.upgrades import remove_css
        remove_css(self.portal, 'base.css')

        self.assertIsNone(css.getResource('base.css'))

    def test_remove_css__two_css(self):
        css = getToolByName(self.portal, 'portal_css')
        self.assertIsNotNone(css.getResource('base.css'))
        self.assertIsNotNone(css.getResource('print.css'))

        from sll.basetheme.upgrades import remove_css
        remove_css(self.portal, ['base.css', 'print.css'])

        self.assertIsNone(css.getResource('base.css'))
        self.assertIsNone(css.getResource('print.css'))

    def test_install_sll_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sll.basetheme'])
        self.assertFalse(installer.isProductInstalled('sll.basetheme'))

        from sll.basetheme.upgrades import install_sll_basetheme
        install_sll_basetheme(self.portal)

        self.assertTrue(installer.isProductInstalled('sll.basetheme'))

    def test_reimport_viewlets(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "plone.portalfooter"
        skinname = "*"
        viewlets = (
            u'plone.footer',
            u'plone.colophon',
            u'plone.site_actions',
            u'sll.basetheme.footer.info',
            u'sll.basetheme.footer.subfolders')
        self.assertEqual(storage.getOrder(manager, skinname), viewlets)

        storage.setOrder(manager, skinname, viewlets)

        from sll.basetheme.upgrades import reimport_viewlets
        reimport_viewlets(self.portal)

        self.assertEqual(storage.getOrder(manager, skinname), viewlets)
