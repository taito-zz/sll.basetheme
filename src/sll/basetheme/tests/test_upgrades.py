from sll.basetheme.upgrades import PROFILE_ID

import mock
import unittest


class TestCase(unittest.TestCase):
    """TestCase for upgrade steps."""

    def test_reimport_jsregistry(self):
        from sll.basetheme.upgrades import reimport_jsregistry
        setup = mock.Mock()
        reimport_jsregistry(setup)
        setup.runImportStepFromProfile.assert_called_with(PROFILE_ID, 'jsregistry', run_dependencies=False, purge_old=False)
