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
