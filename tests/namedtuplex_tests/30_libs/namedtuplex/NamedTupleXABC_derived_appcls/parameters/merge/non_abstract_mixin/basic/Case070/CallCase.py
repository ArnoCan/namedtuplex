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
            def method1(self):
                return 1
            
        class MyClassABC2(ABC):
            def method2(self):
                return 12
    
        class MyClassABC3(ABC):
            def method3(self):
                return 123

        class MyClassABC4(ABC):
            def method4(self):
                return 1234

        class MyClassABCAll(MyClassABC1, MyClassABC2, MyClassABC3, MyClassABC4):
            def methodAll(self):
                return 567

        class MyClass0(MyClassABCAll):
            _fields = ('f0', 'f1', 'f2',)
            def method(self):
                return 89

        class MyClass(MyClass0):
            _fields = MyClass0._fields + ('f3',)
            _merge = False
            def method(self):
                return 890

        myinstance = MyClass(1, 2, 3, 4)
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABC3))
        self.assertTrue(isinstance(myinstance, MyClassABC4))
        self.assertTrue(isinstance(myinstance, MyClass0))
        self.assertTrue(isinstance(myinstance, MyClass))

        self.assertEqual(myinstance.method1(), 1)
        self.assertEqual(myinstance.method2(), 12)
        self.assertEqual(myinstance.method3(), 123)
        self.assertEqual(myinstance.method4(), 1234)
        self.assertEqual(myinstance.methodAll(), 567)
        self.assertEqual(myinstance.method(), 890)
        
            

if __name__ == '__main__':
    unittest.main()
