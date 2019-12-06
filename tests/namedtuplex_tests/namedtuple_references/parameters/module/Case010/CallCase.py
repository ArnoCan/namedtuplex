from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest
from pythonids import PYV36, PYVxyz

from namedtupledefs import namedtuple

class CallUnits(unittest.TestCase):

    def testCase000(self):
        if PYVxyz > PYV36:
            pass
        else:
            self.skipTest("requires >=3.1 or <3")

        res = namedtuple(
            'MyClassABC', 
            ('!f0', '_f1', '%f2'), 
            rename=True,
            module="mypackage.mymodule"
        )
        
        res_name = res.__name__
        self.assertEqual(res_name, 'MyClassABC')
        
        res_base_name = res.__class__.__name__
        self.assertEqual(res_base_name, 'type')

        res_fields = res._fields
        self.assertEqual(res_fields, ('_0', '_1', '_2'))

        res_module = res.__module__
        self.assertEqual(res_module, "mypackage.mymodule")

        self.assertTrue(isinstance(res, type))
            

if __name__ == '__main__':
    unittest.main()

