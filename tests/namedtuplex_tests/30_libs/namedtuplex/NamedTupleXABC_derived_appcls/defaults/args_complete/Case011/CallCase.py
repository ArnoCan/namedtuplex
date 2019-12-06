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
            pass
        
        class MyClass(ABC):
            _fields = ('f0', 'f1', 'f2',)
            _fielddefaults = (11, 22, 33,)
            def _my_method(self):
                return 123

        myinstance = MyClass(1, 2, 3)
        self.assertTrue(isinstance(myinstance, ABC))
        self.assertTrue(isinstance(myinstance, MyClass))

        self.assertFalse(isinstance(myinstance, MyClassABC))
        
        print(type(myinstance.__class__))
        print(ABCMETA)

        self.assertEqual(type(myinstance.__class__), ABCMETA)
        self.assertEqual(type(myinstance), MyClass)

        self.assertEqual(myinstance._my_method(), 123)
        self.assertEqual(myinstance, (1, 2, 3))
            

if __name__ == '__main__':
    unittest.main()

