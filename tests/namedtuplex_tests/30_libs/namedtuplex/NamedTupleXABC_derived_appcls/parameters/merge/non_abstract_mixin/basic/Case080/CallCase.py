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

    def testCase020(self):

        class MyClassABC1(object):
            _fields = ('f0',)
            def method1(self):
                return 1
            
        class MyClassABC2(object):
            _fields = ('f1',)
            def method2(self):
                return 12
    
        class MyClassABCAll(MyClassABC2, MyClassABC1, ABC):
            #_fields = ('f2',)
            _merge = True
            def method(self):
                return 567


        myinstance = MyClassABCAll(1, 2, )
        self.assertEqual(myinstance, (1, 2,))

        self.assertTrue(isinstance(myinstance, MyClassABC1))
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertTrue(isinstance(myinstance, MyClassABCAll))

        self.assertEqual(myinstance.method1(), 1)
        self.assertEqual(myinstance.method2(), 12)
        self.assertEqual(myinstance.method(), 567)

        
            

if __name__ == '__main__':
    unittest.main()

