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
            myvar = 33
            def method(self):
                return 123
            
        class MyClassABC1(ABC):
            myvar = 44
            def method(self):
                return 1234

        class MyClass(MyClassABC):
            _fields = ('f0', 'f1', 'f2')
            _fielddefaults = (111, 222, 333)

        class MyClassABC2(MyClassABC, MyClassABC1):
            pass
        
        class MyClass2(MyClass, MyClassABC2):
            _fields = ('f20', 'f21', 'f22')

#            _verbose=True

        myinstance = MyClass2(1, 2, 3)

        self.assertTrue(isinstance(myinstance, MyClassABC))
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClass))
        self.assertTrue(isinstance(myinstance, MyClass2))
        
        
        self.assertTrue(type(myinstance), MyClassABC)
        self.assertTrue(type(myinstance), MyClassABC1)
        self.assertTrue(type(myinstance), MyClass)
        self.assertTrue(type(myinstance), MyClass2)
        self.assertTrue(type(myinstance.__class__), ABC)


        self.assertEqual(myinstance.method(), 123)
        self.assertEqual(myinstance._asdict(), {"f20": 1, "f21": 2, "f22": 3, "f0": 111, "f1": 222, "f2": 333,})


if __name__ == '__main__':
    unittest.main()

