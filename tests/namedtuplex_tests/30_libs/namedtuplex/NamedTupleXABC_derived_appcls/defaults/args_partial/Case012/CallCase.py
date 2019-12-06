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
            _fields = ('f0', 'f1', 'f2',)
            _fielddefaults = (33, 11, )
            def _my_method(self):
                return 123

        myinstance = MyClassABC(1,)
        self.assertTrue(isinstance(myinstance, MyClassABC))

        self.assertEqual(myinstance._my_method(), 123)
        self.assertEqual(myinstance._my_method(), 123)
        self.assertEqual(myinstance, (1, 33, 11))


if __name__ == '__main__':
    unittest.main()

