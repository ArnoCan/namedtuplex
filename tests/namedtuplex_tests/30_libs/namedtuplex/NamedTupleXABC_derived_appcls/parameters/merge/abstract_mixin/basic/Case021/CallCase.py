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
            myvar1 = 55
            def method1(self):
                return 5555

        class MyClassABC2(MyClassABC, MyClassABC1):
            myvar2 = 66
            def method2(self):
                return 567


        class MyClass(MyClassABC):
            _fields = ('f01', 'f11', 'f21')
            def method(self):
                return 234


#        class MyClass2(MyClassABC2,MyClass):
#        class MyClass2(MyClassABC2, MyClass, MyClassABC1, MyClassABC):  # error MRO: order (MRO) for bases MyClassABC1, MyClassABC, object
        class MyClass2(MyClassABC2, MyClass, MyClassABC, MyClassABC1):
            _fields = ('f0', 'f1', 'f2')
            def method(self):
                return 234

        myinstance = MyClass2(1, 2, 3, 4 ,5 ,6)
        self.assertTrue(isinstance(myinstance, ABC))
        self.assertTrue(isinstance(myinstance, MyClassABC))
        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClass2))
        
        self.assertEqual(myinstance.myvar, 33)
        self.assertEqual(myinstance.myvar1, 55)
        self.assertEqual(myinstance.myvar2, 66)

        self.assertEqual(myinstance.method(), 234)
        self.assertEqual(myinstance.method1(), 5555)
        self.assertEqual(myinstance.method2(), 567)

        self.assertEqual(myinstance._asdict(), {"f0": 1, "f1": 2, "f2": 3, "f01": 4, "f11": 5, "f21": 6,})
            

if __name__ == '__main__':
    unittest.main()

