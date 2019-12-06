from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

_myglobal = 1

import unittest

import os
import abc
import namedtuplex.abc
import pickle


class MyClass(namedtuplex.abc.NamedTupleXABC):
    _fields = ('f0', 'f1', 'f2',)
    _fielddefaults = (11, 22, 33,)
    _rename = True
    _module = '/my/module'
    _verbose = True


class CallUnits(unittest.TestCase):

    def testCase000(self):


        myinstance = MyClass(1, 2, 3)
        self.assertEqual(myinstance, (1, 2, 3))

#         x0 = myinstance.__base__
#         x1 = myinstance.__bases__
        x1 = myinstance.__class__.__name__
        x2 = myinstance.__class__.__base__
        x3 = myinstance.__class__.__bases__
        
        x4 = myinstance._tuplefactory
        x5 = myinstance._tuplefactory.__name__
        x66 = dir(myinstance._tuplefactory)

        y1 = myinstance._tuplefactory.__func__
        y2 = myinstance._tuplefactory.__func__.__name__
        y3 = myinstance._tuplefactory.__func__.__module__

        fx = myinstance._tuplefactory.__func__.__module__ + '.' + myinstance._tuplefactory.__func__.__name__
        y66 = dir(myinstance._tuplefactory.__func__)
        
        _myfile = os.path.dirname(__file__) + os.sep + 'test.p'
        f = open(_myfile, 'wb')
        pickle.dump(myinstance, f, protocol=2)
        f.close()
        
        f = open(_myfile, 'rb')
        myinstance.copy = pickle.load(f)
        f.close()

        
if __name__ == '__main__':
    unittest.main()

