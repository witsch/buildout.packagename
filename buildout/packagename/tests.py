from os.path import join
from string import strip
from subprocess import check_call
from pkg_resources import get_distribution


name = 'buildout.packagename'
home = get_distribution(name).location


def extract_buildout():
    lines = map(strip, open(join(home, 'README.rst')))
    return '\n'.join(lines[lines.index('[buildout]'):])


def test_buildout_uses_package_name(tmpdir):
    app = tmpdir.join('app')
    buildout = tmpdir.join('buildout.cfg')
    buildout.write(extract_buildout())
    check_call([
        join(home, 'bin', 'buildout'),
        'buildout:directory=%s' % home,
        'app:interpreter=%s' % app,
        '-c', str(buildout)])
    app.check(file=True)
    check_call([str(app), '-c', 'import %s' % name])
