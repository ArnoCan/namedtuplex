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

    def testCase000(self):

        class MyClassABC(ABC):
            _fields = ('f10', 'f11', 'f12')
            def _my_method(self):
                return 123
            
        class MyClassABC2(MyClassABC):
            _fields = ('f0', 'f1', 'f2')
            def _my_method(self):
                return 234

        myinstance = MyClassABC2(1, 2, 3, 4, 5, 6,)
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance._my_method(), 234)


    def testCase020(self):

        class MyClassABC(ABC):
            pass
        
        class MyClass1(MyClassABC):
            _fields = ('f0',)
            def _my_method(self):
                return 1
            
        class MyClass2(MyClass1):
            _fields = MyClass1._fields + ('f1',)
            _merge = False
            def _my_method(self):
                return 12
    
        class MyClass3(MyClass2):
            _fields = MyClass2._fields + ('f2',)
            _merge = False

        class MyClass4(MyClass3):
            _fields = MyClass3._fields + ('f3',)
            _merge = False

        myinstance = MyClass4(1, 2, 3, 4)
        self.assertTrue(isinstance(myinstance, MyClass1))
        self.assertTrue(isinstance(myinstance, MyClass2))
        self.assertTrue(isinstance(myinstance, MyClass3))
        self.assertTrue(isinstance(myinstance, MyClass4))
        self.assertEqual(myinstance._my_method(), 12)
        
            

if __name__ == '__main__':
    unittest.main()

