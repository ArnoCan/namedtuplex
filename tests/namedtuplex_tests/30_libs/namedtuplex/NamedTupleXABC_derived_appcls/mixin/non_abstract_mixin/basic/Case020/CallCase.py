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
            _fields = ('f0', 'f1', 'f2')
            def _my_method(self):
                return 123
            
        class MyClassABC2(MyClassABC):
            _fields = ('f0', 'f1', 'f2')
            _merge = False
            def _my_method(self):
                return 234

        myinstance = MyClassABC2(1, 2, 3)
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance._my_method(), 234)
            
    def testCase020(self):

        class MyClassABC(ABC):
            _fields = ('f0', 'f1', 'f2')
            def _my_method(self):
                return 123
            
        class MyClassABC2(MyClassABC):
            _fields = MyClassABC._fields + ('f3',)
            _merge = False
            def _my_method(self):
                return 234

        myinstance = MyClassABC2(1, 2, 3, 4)
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance._my_method(), 234)
        self.assertEqual(myinstance._asdict(), {"f0": 1, "f1": 2, "f2": 3, "f3": 4,})

if __name__ == '__main__':
    unittest.main()

