PROFILE_ID = 'profile-sll.basetheme:default'


def reimport_jsregistry(setup):
    """Reimport jsregistry"""
    setup.runImportStepFromProfile(PROFILE_ID, 'jsregistry', run_dependencies=False, purge_old=False)
