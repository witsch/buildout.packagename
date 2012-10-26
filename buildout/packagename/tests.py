from os.path import join
from pkg_resources import get_distribution
from subprocess import check_call


name = 'buildout.packagename'
home = get_distribution(name).location


def test_buildout_uses_package_name(tmpdir):
    app = tmpdir.join('app')
    check_call([
        join(home, 'bin', 'buildout'),
        'app:interpreter=%s' % app,
        '-c', join(home, 'buildout.cfg')])
    app.check(file=True)
    check_call([str(app), '-c', 'import %s' % name])
