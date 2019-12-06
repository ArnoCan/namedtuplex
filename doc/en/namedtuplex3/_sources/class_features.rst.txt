
.. _FEATURES_CLASS_IMPLEMENTATION:

The Supported Class Features
****************************
The package *namedtuplex* provides the abstract base class
*NamedTupleXABC* of type *NamedTupleXABCMeta*
for factories of named tuples
with configurable inheritance features. 

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC
              
      class MyClass(NamedTupleXABC):
          _fields = ('name0', 'name1',)
      
      x = MyClass(11, 22)
      
      print(x.name0)
      print(x[0])
      
      print(x.name1)
      print(x[1])
      
The parameters for the control of the derivation could be simply set by class member variables.
The classes could serve as base classes and mixin-classes themself.


Abstract Inheritance
====================
The class *NamedTupleXABC*  could be used as a base class for abstract classes including the mixin
of multiple derived abstract classes.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC
      
              
      class MyClassABC(NamedTupleXABC):
          myvar0 = 4711 
          myvar1 = 815 
         
          @property
          def myvalue(self):
              return self.myvar0 + self.myvar1
      
      
      class MyClass(MyClassABC):      
          _fields = ('name0', 'name1',)  # chnages now to a non-abstract class
         
      
      x = MyClass(11, 22)
      
      print(x.name0)
      print(x[0])
      
      print(x.name1)
      print(x[1])
      
      print(x.myvalue)

The presence of the member variable *_fields* determines hereby the transformation of an abstract class 
into a non-abstract class.

Non-Abstract Inheritance
========================
The resulting non-abstract classes could serve as base classes again, 
including to be used as mixin-classes.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import ABC
      
              
      class MyMixin(object):      
          myvar = 4711 
      
      
      class MyClassABC(ABC):
          _fields = ('name2', 'name3',)  # chnages now to a non-abstract class
      
         
      class MyClass(MyClassABC, MyMixin):      
          _fields = ('name0', 'name1',)  # chnages now to a non-abstract class
      
      
      x = MyClass(11, 22, 33, 44)
      
      print(x)
   

The main difference of "*transformed*" non-abstract classes to the standard inheritance 
is here the optional control of the processing of the special class member variables
for the configuration of the named tuple factory.
The class member *_merge* controls, whether these will be superposed by derived classes,
or merged into the corresponding class variables of the derived class.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import ABC
      
              
      class MyMixin(ABC):      
          _fields = ('name2', 'name3',)  # chnages now to a non-abstract class
      
      
      class MyClassABC(object):
          myvar = 4711 
      
         
      class MyClass(MyClassABC, MyMixin,):      
          _fields = ('name0', 'name1',)  # chnages now to a non-abstract class
          _merge = False 
      
         
      x = MyClass(11, 22,)
      
      print(x)

This behaviour could be altered for each inheritance level separately.

Default Values
==============
The metaclass *NamedTupleXABCMeta* uses a variable as the reference to the 
factory for the named tuple.
The metaclass relies hereby for the feature of default values on the selected
factory.
The default factory is *namedtupledefs.namedtuple* [namedtupledefs]_, 
which is a patched version of the standard namedtuple *collections.namedtuple*
with support for default values.

   .. parsed-literal::
   
      from __future__ import print_function
      
      from namedtuplex.abc import NamedTupleXABC
      
              
      class MyMixin(NamedTupleXABC):
          _fields = ('name2', 'name3',)  # chnages now to a non-abstract class
          _fielddefaults = (22, 33)
      
      
      class MyClassABC(object):
          myvar = 4711
      
      class MyClass(MyClassABC, MyMixin,):
          _fields = ('name0', 'name1',)  # chnages now to a non-abstract class
      
      
      x = MyClass(11, 22,)
      
      print(x)
      

Inheritance Parameters
======================

The class **NamedTupleXABC** supports various parameters for the configuration of 
the class factory resulting in the inheritance behaviour.


   .. raw:: html

      <style>
         div.tmptab table td:nth-child(1) {
            width: 30ch;
         }
      </style>
   
      <div class="tmptab">
      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +---------------------------------------------+--------------------------------+
   | :ref:`_fields <param_fieldnames>`           | field names                    |
   +---------------------------------------------+--------------------------------+
   | :ref:`_fielddefaults <param_fielddefaults>` | default values for fields      |
   +---------------------------------------------+--------------------------------+
   | :ref:`_merge <param_merge>`                 | merge two objects              |
   +---------------------------------------------+--------------------------------+
   | :ref:`_module <param_module>`               | for Python-3.6+                |
   +---------------------------------------------+--------------------------------+
   | :ref:`_rename <param_rename>`               | replace silently faulty names  |
   +---------------------------------------------+--------------------------------+
   | :ref:`_tuplefactory <param_tuplefactory>`   | alternative factory            |
   +---------------------------------------------+--------------------------------+
   | :ref:`_typename <param_typename>`           | name of type for created class |
   +---------------------------------------------+--------------------------------+
   | :ref:`_verbose <param_verbose>`             | raise display level            |
   +---------------------------------------------+--------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>


For details see :ref:`NAMEDTUPLEXAPI`.




