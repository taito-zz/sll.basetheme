from Products.CMFCore.utils import getToolByName
from sll.basetheme.tests.base import IntegrationTestCase


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

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-sll.basepolicy:default'), u'0')

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
