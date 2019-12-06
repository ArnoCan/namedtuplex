from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

from namedtuplex.abc import ABC


class CallUnits(unittest.TestCase):

    def testCase020(self):

        class MyClassABC1(ABC):
            _fields = ('f0',)
            def method1(self):
                return 1
            
        class MyClassABC2(MyClassABC1):
            _fields = ('f1',)
            _merge = False
            def method2(self):
                return 12
    
        class MyClassABC3(MyClassABC2):
            _fields = ('f2',)
            _merge = False
            def method3(self):
                return 123

        class MyClassABC4(MyClassABC3):
            _fields = ('f3',)
            _merge = False
            def method4(self):
                return 1234


        class MyClassABCAll(MyClassABC4, MyClassABC3, MyClassABC2, MyClassABC1):
            _fields = ('f4',)
            def method(self):
                return 567


        myinstance = MyClassABCAll(1, 2, 3, 4, 5)
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABC3))
        self.assertTrue(isinstance(myinstance, MyClassABC4))
        self.assertTrue(isinstance(myinstance, MyClassABCAll))

        self.assertEqual(myinstance.method1(), 1)
        self.assertEqual(myinstance.method2(), 12)
        self.assertEqual(myinstance.method3(), 123)
        self.assertEqual(myinstance.method4(), 1234)
        self.assertEqual(myinstance.method(), 567)
        
            

if __name__ == '__main__':
    unittest.main()

