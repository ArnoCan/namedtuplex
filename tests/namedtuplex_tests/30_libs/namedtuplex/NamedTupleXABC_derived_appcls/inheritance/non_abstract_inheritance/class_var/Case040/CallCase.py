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
                try:
                    cls._typeid = kw.pop('typeid')  # see exec-code
                except KeyError:
                    cls._typeid = 0
                try:
                    cls.clsvar = kw.pop('clsvar')
                except KeyError:
                    cls.clsvar = 111
                ret = super(MyClassABC1, cls).__new__(cls, name, bases, namespace, *args, **kw)
                return ret

        class MyClassABC2(MyClassABC1):
            _fields = ('f0', 'f1', 'f2')
            def _my_method(self):
                return 234
            
            def __new__(cls, *args, **kw):
                try:
                    cls.attr2 = kw.pop('attr2')
                    cls.attr2 = 0
                except KeyError:
                    cls.attr2 = 0

                return MyClassABC1.__new__(cls, *args, **kw)
                    

        myinstance1 = MyClassABC1(1, 2, 3, typeid=4711, clsvar=222)
        myinstance2 = MyClassABC2(1, 2, 3, typeid=4711, clsvar=333)

        self.assertTrue(isinstance(myinstance1, MyClassABC1))
        self.assertTrue(isinstance(myinstance2, MyClassABC2))

        self.assertEqual(myinstance1._my_method(), 123)
        self.assertEqual(myinstance2._my_method(), 234)
        
        self.assertEqual(myinstance1._typeid, 4711)
        self.assertEqual(myinstance2._typeid, 4711)

        self.assertEqual(myinstance1.clsvar, 222)
        self.assertEqual(myinstance2.clsvar, 333)

        self.assertTrue(hasattr(myinstance1.__class__, 'clsvar'))
        self.assertTrue(hasattr(myinstance2.__class__, 'clsvar'))
        self.assertEqual(myinstance1.__class__.clsvar, 222)
        self.assertEqual(myinstance2.__class__.clsvar, 333)
        
        self.assertFalse(hasattr(myinstance1.__class__, 'attr2'))
        
        # remember - order matters
        myinstance3 = MyClassABC1(1, 2, 3)
        self.assertTrue(hasattr(myinstance3.__class__, 'clsvar'))
        self.assertEqual(myinstance3.__class__.clsvar, 111)
        self.assertEqual(myinstance3._typeid, 0)

if __name__ == '__main__':
    unittest.main()

