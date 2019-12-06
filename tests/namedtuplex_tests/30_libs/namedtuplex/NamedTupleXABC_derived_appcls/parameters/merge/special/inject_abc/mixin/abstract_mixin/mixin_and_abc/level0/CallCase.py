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

        class MyMixIn(ABC):
            _fields = ('mix',)
            _fielddefaults = (99,)


        class MyClass0(MyMixIn, ABC):
            _fields = ('f2', 'f3',)
            _fielddefaults = (11, 22,)
            
        class MyClass1(MyClass0,):
            _fields = ('f1',)
            _fielddefaults = (66,)

        class MyClass2(MyClass1,):
            _fields = ('f0',)
            _fielddefaults = (77,)


        class MyClass(MyClass2,):
            _merge = True

        myinstance1 = MyClass()
        self.assertEqual(myinstance1, (77, 66, 11, 22, 99))

        myinstance1 = MyClass(1,)
        self.assertEqual(myinstance1, (1, 66, 11, 22, 99))

        myinstance1 = MyClass(1, 2,)
        self.assertEqual(myinstance1, (1, 2, 11, 22, 99))

        myinstance1 = MyClass(1, 2, 3,)
        self.assertEqual(myinstance1, (1, 2, 3, 22, 99))

        myinstance1 = MyClass(1, 2, 3, 4,)
        self.assertEqual(myinstance1, (1, 2, 3, 4, 99))

        myinstance1 = MyClass(1, 2, 3, 4, 5,)
        self.assertEqual(myinstance1, (1, 2, 3, 4, 5))


if __name__ == '__main__':
    unittest.main()

