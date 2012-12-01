from Products.CMFPlone.utils import getToolByName
from sll.basepolicy.upgrades import install_packages


import logging


logger = logging.getLogger(__name__)


def install_sll_basetheme(context):
    """Intall sll.basepolicy"""
    install_packages(context, 'sll.basetheme')


def remove_css(context, oids):
    """Remove css"""
    if not isinstance(oids, list):
        oids = [oids]
    css = getToolByName(context, 'portal_css')
    for oid in oids:
        logger.info('Removing css: {}.'.format(oid))
        css.manage_removeStylesheet(oid)
