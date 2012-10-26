from os.path import abspath, curdir
from sys import path


def extension(buildout):

    def setup(name, *args, **kw):
        buildout['buildout'].setdefault('package-name', name)

    # monkey-patch `setuptools.setup` with the above...
    import setuptools
    original = setuptools.setup
    setuptools.setup = setup

    # now try to import `setup.py` from the current directory, extract
    # the package name using the helper above and set `package-name`
    # in the buildout configuration...
    here = abspath(curdir)
    path.insert(0, here)
    import setup

    # mention `setup` again to make pyflakes happy... :p
    setup

    # reset `sys.path` and undo the above monkey-patch
    path.remove(here)
    setuptools.setup = original

    return buildout
