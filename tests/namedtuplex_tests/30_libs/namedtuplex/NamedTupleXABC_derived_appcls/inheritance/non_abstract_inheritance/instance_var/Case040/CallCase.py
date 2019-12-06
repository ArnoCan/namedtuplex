from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

from namedtuplex.abc import ABC, NamedTupleXABCMeta


class CallUnits(unittest.TestCase):

    def testCase000(self):

        class MyClassABC1(ABC):
            _fields = ('f10', 'f11', 'f12')
            def _my_method(self):
                return 123
            
            def __new__(cls, name, bases, namespace, *args, **kw):
                # drop keyword argument
                return super(MyClassABC1, cls).__new__(cls, name, bases, namespace)

            def __init__(self, *args, **kw):
                try:
                    self.typeid = kw.pop('typeid')
                except KeyError:
                    self.typeid = 0

        class MyClassABC2(MyClassABC1):
            _fields = ('f0', 'f1', 'f2')
            def _my_method(self):
                return 234
            
            def __new__(cls, *args, **kw):
                # drop keyword argument
                return MyClassABC1.__new__(cls, *args)
                    
            def __init__(self, *args, **kw):
                try:
                    self.attr2 = kw.pop('attr2')
                except KeyError:
                    self.attr2 = 0


        myinstance1 = MyClassABC1(1, 2, 3, typeid=4711)
        myinstance2 = MyClassABC2(1, 2, 3, typeid=4711, attr2=815)

        self.assertTrue(isinstance(myinstance1, MyClassABC1))
        self.assertTrue(isinstance(myinstance2, MyClassABC2))

        self.assertEqual(myinstance1._my_method(), 123)
        self.assertEqual(myinstance2._my_method(), 234)
        
        self.assertEqual(myinstance1.typeid, 4711)
        self.assertEqual(myinstance2.attr2, 815)

        
            

if __name__ == '__main__':
    unittest.main()

