from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

import collections
import namedtuplex.abc

class CallUnits(unittest.TestCase):

    def testCase000(self):

        class MyClassABC(namedtuplex.abc.NamedTupleXABC):
            _fields = ('f0', 'f1', 'f2',)
            def __new__(self, cls, *args, **kargs):
                return super(MyClassABC, self).__new__(self, cls, *args, 
                                                       tuplefactory=collections.namedtuple,
                                                       **kargs)
            def __init__(self, cls, *args, **kargs):
                try:
                    kargs.pop('tuplefactory')
                except KeyError:
                    pass
                return super(MyClassABC, self).__new__(self, cls, *args, **kargs)

        res = MyClassABC
        res_name = res.__name__
        self.assertEqual(res_name, 'MyClassABC')
        
        res_base_name = res.__class__.__name__
        self.assertEqual(res_base_name, 'NamedTupleXABCMeta')

        res_fields = res._fields
        self.assertEqual(res_fields, ('f0', 'f1', 'f2'))

        #FIXME:
        print("#4TEST:")
        x00 = res.__name__
        x10 = res.__class__.__name__
        x20 = res.__class__.__bases__
        x30 = res.__class__.__base__
        
        class A(object): pass
        class B(A): pass

        A00 = A.__name__
        A10 = A.__class__.__name__
        A20 = A.__class__.__bases__
        A30 = A.__class__.__base__
        
        B00 = B.__name__
        B10 = B.__class__.__name__
        B20 = B.__class__.__bases__
        B30 = B.__class__.__base__
        
        self.assertEqual(type(res), namedtuplex.abc.NamedTupleXABCMeta)
        self.assertTrue(isinstance(res, namedtuplex.abc.NamedTupleXABCMeta))
        
        self.assertTrue(issubclass(res, namedtuplex.abc.NamedTupleXABC))


if __name__ == '__main__':
    unittest.main()

