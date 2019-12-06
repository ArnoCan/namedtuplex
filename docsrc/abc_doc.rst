
.. _DOC_namedtuplex_abc_doc:

Class Concept of namedtuplex.abc
********************************
The module *namedtuplex.abc* implements an abstract class for the creation named tuples.
The API is used as a replacement of the standard interface *collections.namedtupel*.
The current implementation extends actually the standard implementation. 
This includes beneath enhancements of the call parameters in particular the support of inheritance 
and mixin.

Inheritance and Mixin
=====================

The *collections.namedtuple* classes provide fast processing with acceptable little loss
compared to the pure *tuple*.
Thus the design goal was to keep the low resource requirement and performance impact, while
adding features like attributes/properties at the creation time.
The main data and inheretence design is hereby based on the creation of a data array as a *namedtuple*,
and add specific features including properties with read-out features to the data set.

A real example is here the representaiton of a file system path.
The physical file location, and thus the abstract logical lcation remains constant,
while the representation may vary by several specifications.
The representation may for example be in accordance to teh specification of a *URL*, *UNC*, *POSIX*,
or as a traditional *Windows* path, a long path, a long-UNC path, etc.
The fields of the path vector are here the same for all, while the assembly of the output varies.

The concept of a base data vector with the option to extend this class with features by inheritance 
implies the following rules:

#. The number and the fields are not inherited, neither changed in the parent class.
#. Due to the goal of keeping the performance impact low, no tree-walk algorithm for scattered processing
   is implemented.

As a result:

#. When inheriting the fields of the parent class could be integrated to the class manualy:

      .. parsed-literal::
      
         class BaseClass(NamedTupleXABC):
            _fields = ('a', 'b')
         
         class DerivedClass(BaseClass):
            _fields = BaseClass._fields + ('c')

   Or by recreation:
   
      .. parsed-literal::
      
         class DerivedClass(BaseClass):
            _fields = ('a', 'b', 'c')
   
#. This principle applies tho mixin classes as well.

      .. parsed-literal::
      
         class BaseClass0(NamedTupleXABC):
            _fields = ('a', 'b')
         
         class BaseClass1(NamedTupleXABC):
            _fields = ('c',)

         class DerivedClass(BaseClass0, BaseClass1):
            pass
          
          m =  DerivedClass()

   resulting in:
  
Inheritance of Members
======================
The inheritance and mixin of general members follows the standard *Python* rules. 

Attributes
----------
Simple member variables as attributes are handled in a standard manner.
These basically found a pool of values which are contained the resulting class
and will be processed by the common hierarchy.
Thus these are either hidden by a lower class or could be transparently accessed.

Properties
----------
Properties provide means for the dynamic creation of teh accessed data.
This is in particular helpful when a basic data set is accessed for multiple views, which
requires different formatting including different subsets.
The properties are inherited in accordance to the standard *Python* mechanisms, 
thus could be used without additional restrictions. 
 
 
Methods
-------
The characteristics of the methods due to the inheritance is basically the same as for the propereties.
Thus could be used without additional restrictions. 

The resulting Concept
---------------------
The concept implemented by *namedtuplex* targets mainly the creation of a data class as a named tuple
with a core set of features.
Than the add-on of additional features by derived classes and mixins.

The modification of the tuple with it's fields is still supported, but requires manual interaction
by code.

.. _DOC_NAMEDTUPLEX_ABSTRACT:

Inheritance of Abstract Classes
===============================
The inheritance of abstract classes is basically the same as of the non-abstract classes.
The difference is the absence of a *_field* class member, which is treated by the method 
:ref:`NamedTupleXABCMeta.__new__() <NamedTupleXABCMeta_new>`.


.. _namedtuplex_REFERENCES2:

Resources
=========

* [namedtuple]_  lib/collections

.. |smilecool| image:: _static/smiling-face-with-sunglasses-32x32.png
   :width: 16
   :alt: :-)
