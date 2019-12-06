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
            
            def __new__(cls, *args, **kw):
                try:
                    _typeid = kw.pop('typeid')
                except KeyError:
                    _typeid = 0
                    
                return MyClassABC.__new__(cls, *args, **kw)

        myinstance = MyClassABC2(1, 2, 3, typeid=4711)
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance._my_method(), 234)


    def testCase020(self):

        class MyClassABC1(ABC):
            _fields = ('f0',)
            def _my_method(self):
                return 1
            
        class MyClassABC2(MyClassABC1):
            _fields = MyClassABC1._fields + ('f1',)
            _merge = False
            def _my_method(self):
                return 12
    
        class MyClassABC3(MyClassABC2):
            _fields = MyClassABC2._fields + ('f2',)
            _merge = False
            def _my_method(self):
                return 123

        class MyClassABC4(MyClassABC3):
            _fields = MyClassABC3._fields + ('f3',)
            _merge = False
            def _my_method(self):
                return 1234

        myinstance = MyClassABC4(1, 2, 3, 4)
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABC3))
        self.assertTrue(isinstance(myinstance, MyClassABC4))
        self.assertEqual(myinstance._my_method(), 1234)
        
            

if __name__ == '__main__':
    unittest.main()

