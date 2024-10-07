# -*- coding: utf-8 -*-
# pylint: skip-file
import codecs
import os
import sys
from distutils.core import setup

from setuptools import find_packages

with open('prospector2/__pkginfo__.py') as f:
    exec(f.read())
_VERSION = globals()['__version__']


_PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_INSTALL_REQUIRES = [
    'pylint-plugin-utils>=0.2.6',
    'requirements-detector>=0.6',
    'setoptconf>=0.2.0',
    'dodgy>=0.1.9',
    'pyyaml',
    'mccabe>=0.5.0',
    'pyflakes<2.4.0,>=0.8.1',
    'pycodestyle<2.8.0,>=2.0.0',
    'pep8-naming>=0.3.3,<=0.12.1',
    'pydocstyle>=2.0.0',
    'pylint<2',
    'flake8==3.5.0',
]
# ^ flake8 dropped Python 2 support (in 4.0.0? <https://flake8.pycqa.org/en/latest/release-notes/4.0.0.html>)
# ^ versions of flake8>3.5.0 cause:
# flake8 3.9.2 requires pycodestyle<2.8.0,>=2.7.0, but you'll have pycodestyle 2.3.1 which is incompatible.
# flake8 3.9.2 requires pyflakes<2.4.0,>=2.3.0, but you'll have pyflakes 1.6.0 which is incompatible.
# ^ flake8==3.5.0 causes:
# pep8-naming 0.13.1 requires flake8>=3.9.1, but you'll have flake8 3.5.0 which is incompatible.
# - 'pyflakes<2.0.0,>=0.8.1',
#   'pycodestyle<2.7.0,>=2.0.0',
#   - cause:
#     flake8 3.9.1 requires pycodestyle<2.8.0,>=2.7.0, but you'll have pycodestyle 2.3.1 which is incompatible.
#     flake8 3.9.1 requires pyflakes<2.4.0,>=2.3.0, but you'll have pyflakes 1.6.0 which is incompatible.
#   - but unfortunately, 'pep8-naming>=0.13.1' has Python3-only inline formatting
#     - 0.12.1 is last release (<0.13.0) with Python 2 support
# Fix:
# python2 -m pip uninstall --yes pycodestyle pyflakes pep8-naming flake8 prospector2
# python2 -m pip uninstall --yes pylint-plugin-utils requirements-detector setoptconf dodgy pyyaml pydocstyle
# cd prospector2
# python2 -m pip install -e . # OR:
# Require this:
# prospector2 @ git+https://github.com/Poikilos/prospector2@master

_PACKAGE_DATA = {
    'prospector2': [
        'blender_combinations.yaml',
    ]
}
profiledir = os.path.join(os.path.dirname(__file__), 'prospector2/profiles/profiles')
_PACKAGE_DATA['prospector2'] += [profile for profile in os.listdir(profiledir)]

_CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: MacOS :: MacOS X',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: '
    'GNU General Public License v2 or later (GPLv2+)',
]

_OPTIONAL = {
    'with_frosted': ('frosted>=1.4.1',),
    'with_vulture': ('vulture>=0.6,<0.25',),
    'with_pyroma': ('pyroma>=2.3',),
    'build_tools': ('nose', 'coverage', 'coveralls', 'mock'),
}

with_everything = [req for req_list in _OPTIONAL.values() for req in req_list]
_OPTIONAL['with_everything'] = sorted(with_everything)

if os.path.exists('README.rst'):
    _LONG_DESCRIPTION = codecs.open('README.rst', 'r', 'utf-8').read()
else:
    _LONG_DESCRIPTION = 'Prospector: python static analysis tool. See http://prospector.readthedocs.io'


setup(
    name='prospector2',
    version=_VERSION,
    url='http://prospector.readthedocs.io',
    author='landscape.io',
    author_email='code@landscape.io',
    license='GPLv2',
    zip_safe=False,
    description='Prospector: python static analysis tool',
    long_description=_LONG_DESCRIPTION,
    keywords='pylint pyflakes pep8 mccabe frosted prospector static code analysis',
    classifiers=_CLASSIFIERS,
    package_data=_PACKAGE_DATA,
    include_package_data=True,
    packages=_PACKAGES,
    entry_points={
        'console_scripts': [
            'prospector = prospector2.run:main',
            'prospector2 = prospector2.run:main', # duplicate just to make it more friendly to figure out what to run :-)
        ],
    },
    install_requires=_INSTALL_REQUIRES,
    extras_require=_OPTIONAL,
)
