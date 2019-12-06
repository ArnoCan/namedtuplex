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
            _fields = ('f3',)
            _fielddefaults = (33,)

        class MyClass1(object):
            _fields = ('f0', 'f1',)
            _fielddefaults = (11, 22,)
            

        class MyClass2(MyClass1, ABC,):
            _fields = ('f4',)
            _fielddefaults = (66,)
            _merge = False

        class MyClass3(MyMixIn, MyClass2, ABC,):
            _merge = True

#        class MyClass(MyClass3,):
        class MyClass(MyClass3, ABC,):
            _fields = ('f5',)
            _fielddefaults = (77,)            
            _merge = True

        myinstance1 = MyClass(1, 2,)
        self.assertEqual(myinstance1, (1, 2, 66))


if __name__ == '__main__':
    unittest.main()

