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

        class MyClassABC1(ABC, object):
            _fields = ('f0',)
            def _my_method(self):
                return 1
            
        class MyClassABC2(object,):
            _fields = ('f1',)
            def _my_method(self):
                return 12
    
        class MyClassABC3(object):
            _fields = ('f2',)
            def _my_method(self):
                return 123

        class MyClassABC4(object):
            _fields = ('f3',)
            def _my_method(self):
                return 1234

        class MyClassABCAll(MyClassABC1, MyClassABC2, MyClassABC3, MyClassABC4):
            _fields = ('f4',)
            def _my_method(self):
                return 567

        myinstance = MyClassABCAll(1, 2, 3, 4, 5,)

        self.assertTrue(type(myinstance.__class__), MyClassABC1)

        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABC3))
        self.assertTrue(isinstance(myinstance, MyClassABC4))
        self.assertEqual(myinstance._my_method(), 567)
        
            

if __name__ == '__main__':
    unittest.main()

