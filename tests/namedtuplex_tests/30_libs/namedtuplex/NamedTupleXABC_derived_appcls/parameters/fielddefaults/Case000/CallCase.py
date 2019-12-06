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
import namedtuplex.abc

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
            _fields = ('f0', 'f1', 'f2', 'f3', 'f4',)
            _fielddefaults = ('default0', 'default1', 123, 1.32e-6, 44444444444333333333333222222222222222111111111111)

        myinstance = MyClass()
        self.assertEqual(myinstance, MyClass._fielddefaults)
        

if __name__ == '__main__':
    unittest.main()

