
.. _INDEX_BLUEPRINT:

*********
Blueprint
*********

.. _REFERENCE_ARCHITECTURE:


The *namedtuplex* package provides extended named tuples with inheritance and 
function-style defaults for fields.
The parameter passing is designed as member variables of the derived classes implemented 
by the meta class :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>`.
The application of the default values relies on the implementation of 
the actual factory - the optional parameter :ref:`tuplefactory <param_tuplefactory>`.
The default factory is *namedtupledefs.namedtuple* with support for default values.


.. _FIGURE_STRUCTURE:

.. figure:: _static/structure.png
   :figwidth: 800
   :align: center
   :target: _static/structure.png
   
   Figure: Class Diagram of NamedTupleX |structure_zoom| 

.. |structure_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/structure.png
   :width: 16

For details on the implemented design refer to
":ref:`The Implementation Basics of Classes <CONCEPTS_CLASS_IMPLEMENTATION>`"
and 
":ref:`The SW-Design of namedtuplex <SWDESIGN>`".

The provided function *namedtuplex* could be used as a drop-in replacement of the
*namedtupledefs* [namedtupledefs]_ and standard *namedtuple* [namedtuple]_ class factory 
as well as the *namedtuple_with_abc* implementation 
by *Jan  Kaliszewski* [JANKALI]_ [NAMEDTUPLEABC]_ - when used with the standard parameters only.
The receipt published by *Jan  Kaliszewski*  [NAMEDTUPLEABC]_ served as a base for 
the  *namedtuplex*.

Classes
-------
Just a reminder - in Python anything is a class.

Simple Named Tuple Class
^^^^^^^^^^^^^^^^^^^^^^^^
Create a simple class:

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
         
      class MyClass(NamedTupleXABC):
          _fields = ('a', 'b', )             # defines the fields of the *namedtuple*
          pass
      assert issubclass(MyClass, ABC)
      
      mynamedtuple = MyClass(11, 22)
      assert mynamedtuple[0] == 11
      assert mynamedtuple[1] == 22
      
      print("OK")

Symbolic Field Names
^^^^^^^^^^^^^^^^^^^^
Alternative symbolic names for the fields of the tuple.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
         
      class MyClass(NamedTupleXABC):
          _fields = ('a', 'b', )        # defines the symbolic names
          pass
      assert issubclass(MyClass, ABC)
      
      mynamedtuple = MyClass(11, 22)
      assert mynamedtuple[0] == 11
      assert mynamedtuple[1] == 22
      
      assert mynamedtuple[0] == mynamedtuple.a
      assert mynamedtuple[1] == mynamedtuple.b
      
      print("OK")

Inheritance
^^^^^^^^^^^
Inheritance of abstract and non-abstract classes.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
      
      class MyClass(NamedTupleXABC):
          _fields = ('a', 'b', )
          pass
      assert issubclass(MyClass, ABC)
      
      class MyClassDerived(MyClass):
          _fields = MyClass._fields + ('c',)           # the inheritance of fields requires manual coding
          pass
      assert issubclass(MyClassDerived, ABC)
      
      mynamedtuple0 = MyClass(11, 22)
      mynamedtuple01= MyClassDerived(11, 22, 33)
      
      print("OK")

For the concept see :ref:`Class Concept of namedtuplex.abc <DOC_namedtuplex_abc_doc>`.

Abstract Inheritance
^^^^^^^^^^^^^^^^^^^^
Creates an abstract tuple class in accordance to [PEP3119]_, see also [abc]_.

Example with inherited attribute from a custom abstract class.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
      
      
      class MyClassABC0(NamedTupleXABC):        # abstract class
          typeid = 4711                         # standard inheritance for *typeid*

      class MyClassABC1(MyClassABC0):           # abstract class
          formatid = 'xyz'                      # standard inheritance for *formid*
      
      class MyClass(MyClassABC1):               # non-abstract class
          _fields = ('a', 'b')                  # triggered by *_fields*
         
          def __str__(self):
              return "%d(%s): %s / %s" % (self.typeid, self.formatid, self[0], self[1])
      
      mynamedtuple0 = MyClass(11, 22)
      print(mynamedtuple0)


For the concept see :ref:`Inheritance of Abstract Classes <DOC_NAMEDTUPLEX_ABSTRACT>`.


Mixin
^^^^^
The use of the the generated tuple class as mixin.


   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC
      
      
      class MyClassABC(NamedTupleXABC):                 # abstract class
          typeid = 4711
      
      class MyBaseClass(MyClassABC):                    # non-abstract class
          _fields = ('a', 'b',)
      
      class MyOtherBaseClass(object):                   # non-abstract and non-tupel class
          def print(self):
              print(str(self._fields))
              print(str(self))
              
      class MyClassL(MyBaseClass, MyOtherBaseClass):
          pass
      
      class MyClassR(MyOtherBaseClass, MyBaseClass):
          pass
      
      
      mynamedtuple0 = MyClassL(11, 22,)
      mynamedtuple0.print()
      
      mynamedtuple1 = MyClassR(11, 22,)
      mynamedtuple1.print()


Default Values
^^^^^^^^^^^^^^
Default values for for the fields, supports partial fields for the initialization
of the generated class - similar to function arguments [PYFUNC]_.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
         
      class MyClass(NamedTupleXABC):
          _fields = ('a', 'b', 'c', )      # defines the fields and the symbolic names
      
      mynamedtuple0 = MyClass(11, 22,      fielddefaults=(('c', 33),)           )  # add dynamic defaults via metaclass
      mynamedtuple1 = MyClass(11,          fielddefaults=((  2, 33), ('b', 22),))  # add dynamic defaults via metaclass
      mynamedtuple2 = MyClass(11, 55, 66,  fielddefaults=(('c', 33), (  1, 22),))  # add dynamic defaults via metaclass

      assert mynamedtuple0[0] == 11
      assert mynamedtuple0[1] == 22
      assert mynamedtuple0[2] == 33
      
      assert mynamedtuple1[0] == 11
      assert mynamedtuple1[1] == 22
      assert mynamedtuple1[2] == 33
      
      assert mynamedtuple2[0] == 11
      assert mynamedtuple2[1] == 55
      assert mynamedtuple2[2] == 66

      print("OK")

Or the alternate static variant, which allows only one set of default values for each class:

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC, ABC
         
      class MyClass(NamedTupleXABC):
          _fields = ('a', 'b', 'c', )        # defines the symbolic names
          _item_defauls = (('c', 33), (1, 22),))

      mynamedtuple2 = MyClass(11, 55)

      assert mynamedtuple0[0] == 11
      assert mynamedtuple0[1] == 55
      assert mynamedtuple0[2] == 33

      print("OK")

