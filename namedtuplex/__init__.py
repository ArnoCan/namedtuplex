# -*- coding: utf-8 -*-
"""The package 'namedtuplex' provides advanced call interfaces and classes for *namedtuples*.
"""
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                "@Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"


class NamedTupleXError(Exception):
    """Generic package error."""
    pass


class NamedTupleXSyntaxError(NamedTupleXError):
    """Common syntax error."""
    pass


class NamedTupleXParameterError(NamedTupleXError):
    """Parameters erroroneous."""
    pass


class NamedTupleXRangeError(NamedTupleXError):
    """Range mismatch."""
    pass


class NamedTupleXABCError(NamedTupleXError):
    """Common syntax error."""
    pass


