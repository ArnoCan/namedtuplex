from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest
import collections


from namedtupledefs import namedtuple

class CallUnits(unittest.TestCase):

    def testCase000(self):

        MyClass_collections = collections.namedtuple('MyClassABC', ('f0', 'f1', 'f2'))
        MyClass_namedtupledefs = namedtuple('MyClassABC', ('f0', 'f1', 'f2'))
        
        class MyClass_collections2(MyClass_collections): pass
        class MyClass_nametuplex2(MyClass_namedtupledefs): pass

        inst_collections = MyClass_collections2(1, 2, 3)
        inst_nametuplex = MyClass_nametuplex2(1, 2, 3)
        self.assertEqual(inst_collections, inst_nametuplex,)
            

if __name__ == '__main__':
    unittest.main()

