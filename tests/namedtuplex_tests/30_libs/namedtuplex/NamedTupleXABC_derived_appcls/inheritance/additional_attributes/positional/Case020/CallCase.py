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
            myvar = 33
            def method(self):
                return 123

            def __new__(cls, *args, **kargs):
                return super(MyClassABC, cls).__new__(cls, *args[:3])
            
            def __init__(self, *args, **kargs):
                try:
                    self.typeid = args[3]
                except KeyError:
                    pass
                    
                super(MyClassABC,self).__init__()
                
        class MyClassABC2(MyClassABC):
            _fields = ('f0', 'f1', 'f2')
            def method(self):
                return 234

            def __new__(cls, *args, **kargs):
                return super(MyClassABC2, cls).__new__(cls, *args[:3])

            def __init__(self, *args, **kargs):
                lmax = len(args)
                try:
                    self.attr2 = args[4]
                    lmax -= 1
                except KeyError:
                    pass
                    
                super(MyClassABC2,self).__init__(*args[:lmax], **kargs)

#         x0 = type(MyClassABC2)
#         x1 = MyClassABC2.__bases__
#         x2 = MyClassABC2.__base__
# 
#         y0 = type(MyClassABC)
#         y1 = MyClassABC.__bases__
#         y2 = MyClassABC.__base__

        myinstance = MyClassABC2(1, 2, 3, 888, 999)
        
        self.assertTrue(isinstance(myinstance, MyClassABC2))
        self.assertEqual(myinstance.method(), 234)
        self.assertEqual(myinstance._asdict(), {"f0": 1, "f1": 2, "f2": 3,})
            
        self.assertEqual(myinstance.typeid, 888)
        self.assertEqual(myinstance.attr2, 999)


if __name__ == '__main__':
    unittest.main()

