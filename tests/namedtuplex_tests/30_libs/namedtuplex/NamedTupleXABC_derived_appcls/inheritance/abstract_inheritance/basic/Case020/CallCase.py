from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

from namedtuplex.abc import ABC, ABCMETA


class CallUnits(unittest.TestCase):

    def testCase000(self):

        class MyClassABC(ABC):
            myvar = 33
            def method(self):
                return 123
            
        class MyClassABC2(MyClassABC):
            myvar = 44
            def method(self):
                return 234

        class MyClass(MyClassABC2):
            _fields = ('f0', 'f1', 'f2')
            def method(self):
                return 234

        myinstance = MyClass(1, 2, 3)

        self.assertTrue(isinstance(myinstance, ABC))
        self.assertTrue(isinstance(myinstance, MyClassABC))
        self.assertTrue(isinstance(myinstance, MyClassABC2))

        self.assertEqual(type(myinstance), MyClass)
        self.assertEqual(type(myinstance.__class__), ABCMETA)

        self.assertEqual(myinstance.method(), 234)
        self.assertEqual(myinstance.myvar, 44)
        self.assertEqual(myinstance._asdict(), {"f0": 1, "f1": 2, "f2": 3,})
            

if __name__ == '__main__':
    unittest.main()

