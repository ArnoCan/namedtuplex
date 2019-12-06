from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"

import unittest

from namedtupledefs import namedtuple

class CallUnits(unittest.TestCase):

    def testCase000(self):

        res = namedtuple('MyClassABC', ('f0', 'f1', 'f2'))
        
        res_name = res.__name__
        self.assertEqual(res_name, 'MyClassABC')
        
        res_base_name = res.__class__.__name__
        self.assertEqual(res_base_name, 'type')

        res_fields = res._fields
        self.assertEqual(res_fields, ('f0', 'f1', 'f2'))

        self.assertEqual(type(res), type)
        self.assertTrue(isinstance(res, type))


if __name__ == '__main__':
    unittest.main()

