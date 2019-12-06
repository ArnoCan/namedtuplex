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
            def _my_method(self):
                return 123
            
        class MyClassABC2(MyClassABC):
            _fields = ('f0', 'f1', 'f2')

        myinstance = MyClassABC2(1, 2, 3)
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance._my_method(), 123)


    def testCase020(self):

        class MyClassABC1(ABC):
            def _my_method(self):
                return 1
            
        class MyClassABC2(MyClassABC1):
            def _my_method(self):
                return 12
    
        class MyClassABC3(MyClassABC2):
            _fields = ('f1',)
            def _my_method(self):
                return 123

        class MyClassABC4(MyClassABC3):
            _fields = MyClassABC3._fields + ('f2',)
            _merge = False
            def _my_method(self):
                return 1234

        myinstance = MyClassABC4(1, 2,)

        self.assertTrue(isinstance(myinstance, ABC))
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABC3))
        self.assertTrue(isinstance(myinstance, MyClassABC4))
        
        self.assertEqual(myinstance._my_method(), 1234)
        
            

if __name__ == '__main__':
    unittest.main()

