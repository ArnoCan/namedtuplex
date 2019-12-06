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

        class MyMixIn(object):
            def method(self):
                return "MyMixIn1_method"
            
            def _asdict(self):  # MixIn cannot override a standard namedtuple
                return "MyMixIn1_asdict"

        class MyMixIn1(object):
            def method(self):
                return "MyMixIn1_method"
            
            def _asdict(self):  # MixIn cannot override a standard namedtuple
                return "MyMixIn1_asdict"

        class MyClass1(ABC):
            _fields = ('f00', 'f01', 'f02')
            def method(self):
                return 123
            
            def __new__(cls, name, bases, namespace, *args, **kw):
                # drop keyword argument
                return super(MyClass1, cls).__new__(cls, name, bases, namespace)

            def __init__(self, *args, **kw):
                try:
                    self.typeid = kw.pop('typeid')
                except KeyError:
                    self.typeid = 0

        class MyClass2right(MyClass1, MyMixIn):
            _fields = ('f10', 'f11', 'f12')
            def method(self):
                return 234
            
            def __new__(cls, *args, **kw):
                # drop keyword argument
                return MyClass1.__new__(cls, *args)
                    
            def __init__(self, *args, **kw):
                try:
                    self.attr2 = kw.pop('attr2')
                except KeyError:
                    self.attr2 = 0

        class MyClass2left(MyMixIn1, MyClass2right):
            _fields = ('f0', 'f1', 'f2')
            def method(self):
                return 567
            
            def __new__(cls, *args, **kw):
                # drop keyword argument
                return MyClass1.__new__(cls, *args)
                    
            def __init__(self, *args, **kw):
                try:
                    self.attr2 = kw.pop('attr2')
                except KeyError:
                    self.attr2 = 0



        myinstance1 = MyClass1(1, 2, 3, typeid=4711)
        myinstance2r = MyClass2right(1, 2, 3, typeid=4711, attr2=815)
        myinstance2l = MyClass2left(1, 2, 3, typeid=4711, attr2=815)

        self.assertTrue(isinstance(myinstance1, MyClass1))
        self.assertTrue(isinstance(myinstance2r, MyClass2right))
        self.assertTrue(isinstance(myinstance2l, MyClass2left))

        self.assertEqual(myinstance1.method(), 123)
        self.assertEqual(myinstance2r.method(), 234)
        self.assertEqual(myinstance2l.method(), 567)
        
        self.assertEqual(myinstance1.typeid, 4711)
        self.assertEqual(myinstance2r.attr2, 815)
        self.assertEqual(myinstance2l.attr2, 815)

        
        self.assertNotEqual(myinstance2r._asdict(), "MyMixIn_asdict")  # MixIn cannot override a standard namedtuple
        self.assertNotEqual(myinstance2l._asdict(), "MyMixIn_asdict")  # MixIn cannot override a standard namedtuple

        class MyClass3right(MyClass2right):
            _fields = ('z',)            
            def _asdict(self):  # MixIn can override a derived non-abstract class
                return "MyMixIn_asdict"

        class MyClass3left(MyClass2left):
            _fields = ('z',)            
            def _asdict(self):  # MixIn can override a derived non-abstract class
                return "MyMixIn_asdict"

        myinstance3r = MyClass3right(1, 2, 3, 4, 5, 6, 7,)
        myinstance3l = MyClass3left(1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)

        self.assertEqual(myinstance3r._asdict(), "MyMixIn_asdict")
        self.assertEqual(myinstance3l._asdict(), "MyMixIn_asdict")
                    

if __name__ == '__main__':
    unittest.main()

