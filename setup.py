# -*- coding: utf-8 -*-
"""The *namedtuplex* package provides extended named tuples
with additional features including an abstract base class, 
standard and extended class factories with function-style
default values and additional parameters.

Additional local options:
   --sdk:
       Requires sphinx, epydoc, and dot-graphics.

   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import re

import setuptools


try:
    #
    # optional remote debug only
    #
    from rdbg import start        # load a slim bootstrap module
    start.start_remote_debug()    # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass


import yapyutils.help
import yapyutils.files.utilities

#
# setup extension modules
#
import setupdocx

# documents
from setupdocx.build_docx import BuildDocX
from setupdocx.dist_docx import DistDocX
from setupdocx.install_docx import InstallDocX
from setupdocx.build_apiref import BuildApirefX
from setupdocx.build_apidoc import BuildApidocX

# unittests
from setuptestx.testx import TestX


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"
__vers__ = [0, 1, 21, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'

__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


#-------------------------------------------------------
#
# Package parameters for setuptools - see also setup.cfg
#
#-------------------------------------------------------

_name = 'namedtuplex'
"""package name"""

__pkgname__ = "namedtuplex"
"""package name"""

_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)
"""assembled version string"""

_author = __author__
"""author of the package"""

_author_email = __author_email__
"""author's email """

_license = __license__
"""license"""

_packages = ['namedtuplex']
"""Python packages to be installed."""

_packages_sdk = ['namedtuplex']
"""Python packages to be installed."""

_scripts = [
]
"""Scripts to be installed."""

_package_data = {
    'namedtuplex': [
        'README.md', 'ArtisticLicense20.html', 'licenses-amendments.txt',
    ],
}
"""Provided data of the package."""

_url = 'https://sourceforge.net/projects/namedtuplex/'
"""URL of this package"""

# _download_url="https://github.com/ArnoCan/namedtuplex/"
_download_url = "https://sourceforge.net/projects/namedtuplex/files/"


_install_requires = [
    'pythonids >= 0.1.0',
    'namedtupledefs >= 0.1.20',  # will be obsolte as soon as collections.namedtuple is adapted
]
"""prerequired non-standard packages"""


_description = "Extended *namedtuple* - extends fabric and provides abstract classes."

_README = os.path.join(os.path.dirname(__file__), 'README.md')
_long_description = '\n' + open(_README).read() + '\n'
"""detailed description of this package"""

if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write(
            "WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'pythonids',
            'sphinx >= 1.6',
            'epydoc >= 3.0',
        ]
    )

    _packages = _packages_sdk

_test_suite = "tests.CallCase"

__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Help on addons.
if '--help-namedtuplex' in sys.argv:
    yapyutils.help.usage('setup')
    sys.exit(0)

if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


class build_docx(BuildDocX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """
    
    def __init__(self, *args, **kargs):
#        self.name = _name
#         self.copyright = __copyright__
#         self.status = __status__
#        self.release = __release__
        BuildDocX.__init__(self, *args, **kargs)


class install_docx(InstallDocX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
#         self.name = _name
#         self.copyright = __copyright__
#         self.status = __status__
#         self.release = __release__
        InstallDocX.__init__(self, *args, **kargs)


class dist_docx(DistDocX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        DistDocX.__init__(self, *args, **kargs)


class build_apidoc(BuildApidocX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        BuildApidocX.__init__(self, *args, **kargs)


class build_apiref(BuildApirefX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        BuildApirefX.__init__(self, *args, **kargs)


class testx(TestX):
    """For test, debug, and packaging of namedtuplex and setuplibx.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        TestX.__init__(self, *args, **kargs)


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=_author,
    author_email=_author_email,
    cmdclass={
        'build_apidoc': build_apidoc,
        'build_apiref': build_apiref,
        'build_docx':   build_docx,
        'install_docx': install_docx,
        'dist_docx':    dist_docx,
        'testx':        testx,
    },
    description=_description,
    download_url=_download_url,
    entry_points={
        'distutils.commands': [
            'build_apidoc = namedtuplex.build_apidoc:BuildApidocX',
            'build_apiref = namedtuplex.build_apiref:BuildApirefX',
            'build_docx = namedtuplex.build_docx:BuildDocX',
            'install_docx = namedtuplex.install_docx:InstallDocX',
            'dist_docx = namedtuplex.dist_docx:DistDocX',
        ]
    },
    install_requires=_install_requires,
    license=_license,
    long_description=_long_description,
    name=_name,
    package_data=_package_data,
    packages=_packages,
    scripts=_scripts,
    url=_url,
    version=_version,
    zip_safe=False,
)

if '--help' in sys.argv:
    print()
    print("Help on provided package extensions by " + str(_name))
    print("   --help-" + str(_name))
    print()

sys.exit(0)