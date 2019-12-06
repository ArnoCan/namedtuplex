from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

_myglobal = 1

import abc
from collections import OrderedDict 
from collections import namedtuple
import namedtuplex.abc

from pythonids import PYV3X

class CallUnits(unittest.TestCase):

    def testCase000(self):
        class MyClassABC(namedtuplex.abc.NamedTupleXABC):
            pass
        
        res0 = MyClassABC
        res0_name = res0.__name__
        self.assertEqual(res0_name, 'MyClassABC')
        
        res0_base_name = res0.__class__.__name__
        self.assertEqual(res0_base_name, 'NamedTupleXABCMeta')

        res0_fields = res0._fields
        self.assertTrue(isinstance(res0_fields, abc.abstractproperty))


        class MyClass(namedtuplex.abc.NamedTupleXABC):
            _fields = ('f0', )
            _tuplefactory = namedtuple

        myinstance = MyClass(1,)
        self.assertEqual(myinstance._asdict(), OrderedDict([('f0', 1), ]))


        self.assertEqual(myinstance._tuplefactory.__func__, namedtuple)
#         if PYV3X: 
#             self.assertEqual(myinstance._tuplefactory, namedtuple)
#         else:
#             self.assertEqual(myinstance._tuplefactory.__func__, namedtuple)

if __name__ == '__main__':
    unittest.main()

