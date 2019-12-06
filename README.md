namedtuplex
==============

The *namedtuplex* package provides extended named tuples with additional features
including an abstract base class, standard and extended class factories with
function-style default values and additional parameters.
The best application is for return values as tuples with a variable number 
of valid members. 

The contained interfaces are:

- **namedtuple**:
	
  The drop-in replacement of *collections.namedtuple* with optional class registration
  as default.

- **namedtuplex**:
	
  The drop-in replacement of *collections.namedtuple* with additional features - including
  default values, and custom tuple factories.

- **NamedTupleXABC**:
	
  Abstract base class in accordance to [PEP3119] supporting inheritance and mixin, 
  could be customised as required. 
  Includes a metaclass **NamedTupleXABCMeta**.
  See also [abc].

For the standard library *collections.namedtuple* see Python documentation.
For the fast enumeration of the *Python* implementation and release refer to *pythonids*.
See documentation for online references.

**Online documentation**:

* https://namedtuplex.sourceforge.io/


**Runtime-Repository**:

* PyPI: https://pypi.org/project/namedtuplex/

  Install: *pip install namedtuplex*, see also section 'Install' of the online documentation.


**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/namedtuplex/files/

* bitbucket.org: https://bitbucket.org/acue/namedtuplex

* github.com: https://github.com/ArnoCan/namedtuplex/

* pypi.org: https://pypi.org/project/namedtuplex/


Project Data
------------

* PROJECT: 'namedtuplex'

* MISSION: The replacement of the standard *collections.namedtuple* by an advanced named tuple library.

* VERSION: 00.01

* RELEASE: 00.01.021

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints

Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

*  Python2.7, and Python3.5+

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy


**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense, BlackArch, ParrotOS, Pentoo

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

Current Release
---------------

Major Changes:

* Initial release.


ToDo:

* Test of *verbose* parameter as defined by *collections.namedtuple*
* MicroPython, CircuitPython

Known Issues:

* not yet

