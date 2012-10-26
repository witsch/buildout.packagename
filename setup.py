from setuptools import setup, find_packages

name = 'buildout.packagename'
version = '1.0'

buildout = open('buildout.cfg').readlines()
readme = open('README.rst').read() % '  '.join(buildout)
changes = open('CHANGES.txt').read()

setup(name=name,
    version=version,
    description='A `zc.buildout` extension to extract the package '
                'name from an adjacent `setup.py`.',
    long_description=readme + changes,
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='BSD',
    keywords='buildout extension setuptools',
    author='Andreas Zeidler',
    author_email='witsch@plone.org',
    url='https://github.com/witsch/' + name,
    packages=find_packages(),
    namespace_packages=['buildout'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
    ],
    extras_require={
        'testing': [
            'zc.buildout',
            'pytest>=2.3',
            'pytest-pep8',
        ],
    },
    entry_points={
        'zc.buildout.extension': 'default=%s:extension' % name,
    })
