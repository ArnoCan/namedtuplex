
.. _namedtuplex_APPPARTS:

namedtuplex.abc
===============

The *namedtuplex.abc* module provides the enhanced replacement of *containers.namedtuple*.
The *namedtuplex.abc.namedtuple* is drop-in compatible with the *containers.namedtuple*
interface.
The contained public classes interfaces are:

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

   +-----------------------------------------------+-----------------------------------------------------------------+
   | :ref:`ABC <RETURN_abc>`                       | Alias for :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>`.        |
   +-----------------------------------------------+-----------------------------------------------------------------+
   | :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>` | Abtstract base class with support of inheritance and mixin.     |
   +-----------------------------------------------+-----------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>

The contained secondary public utility classes.
These serve as internal template and metaclass, which could be alternated by call interface parameters.

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

   +-------------------------------------------------------+------------------------------------------------------------------+
   | :ref:`ABCMETA <RETURN_NamedTupleXABCMeta>`            | Alias for :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>`. |
   +-------------------------------------------------------+------------------------------------------------------------------+
   | :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>` | Meta class for the parameterized creation.                       |
   +-------------------------------------------------------+------------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
      </div>


The common return value for the interfaces is a *namedtuple* class of the type  
defined by the  input parameter *typename*.
For a detailed overview refer to ":ref:`The namedtuplex API - Parameters <NAMEDTUPLEXAPI_PARAMETERS>`".

.. _DOC_COMMON_RETURN_TYPES:
.. _DOC_RETURN_NamedTupleXABC:



Inheritance
-----------
The class *NamedTupleXABC* supports the inheritance by derived classes.
The class itself is an abstract class based on the metaclass *NamedTupleXABCMeta*. 

.. raw:: html

   <div class="centerfigure" style="width:450px;">
   <div class="classdiagramhref">

.. inheritance-diagram:: 
      namedtuplex.abc.NamedTupleXABCMeta
      namedtuplex.abc.NamedTupleXABC
   :parts: 1

.. raw:: html

   </div>
   </div>

|

The class supports the inheritance from abstract classes as well as from non-abstract classes. 

Mixin
-----
The class *NamedTupleXABC* supports the mixin by derived classes.

.. role:: raw-html(raw)
   :format: html

Module
------

.. automodule:: namedtuplex.abc

Functions
---------

with_metaclass
^^^^^^^^^^^^^^
The function *with_metaclass* is copied from *future.utils* [future.utils]_.

.. autofunction:: with_metaclass

.. _RETURN_abc:

ABC
---
.. autoclass:: ABC

Same as *namedtuple.abc.NamedTupleXABC*.

.. _RETURN_NamedTupleXABC:

NamedTupleXABC
--------------
|

.. inheritance-diagram:: 
      namedtuplex.abc.ABC
   :parts: 1

|

.. autoclass:: namedtuplex.abc.NamedTupleXABC
   
   .. autoattribute:: _fields
   .. autoattribute:: _fielddefaults


merge
^^^^^

.. automethod:: NamedTupleXABC.merge

inherited tuple members
^^^^^^^^^^^^^^^^^^^^^^^

Inherited members from the parent *namedtuple*, by default *namedtupledefs.namedtuple*.

* *_make*
* *_asdict*
* *_replace*
* *__repr__*
* *__getnewargs__*
* *__getstate__*
* *merge*
    
.. _RETURN_NamedTupleXABCMeta:

NamedTupleXABCMeta
------------------
|

.. inheritance-diagram:: 
      namedtuplex.abc.NamedTupleXABCMeta
   :parts: 1

|

.. autoclass:: namedtuplex.abc.NamedTupleXABCMeta


.. index::
   pair: parameters; _fielddefaults
   pair: parameters; _fields
   pair: parameters; fielddefaults
   pair: parameters; fieldnames
   pair: parameters; fields
   pair: parameters; tuplefactory
   pair: parameters; typename
             
.. _NamedTupleXABCMeta_new:

__new__
^^^^^^^
.. automethod:: NamedTupleXABCMeta.__new__

|

   Examples:

      .. code-block::

         Python3:
      
            class _NamedTupleABC(metaclass=NamedTupleXABCMeta):
                _fields = abstractproperty()
                 
                attribute01 = default01
                attribute02 = default02
      
                # common part for Python3 and Python2
                 
                def __new__(cls, *args, **kargs):
                    try:
                        attribute01 = kargs.pop('attribute01')
                    except KeyError:
                        attribute01 = default01
      
                    try:
                        attribute02 = kargs.pop('attribute02')
                    except KeyError:
                        attribute02 = default02
      
                    return super(_NamedTupleABC, cls).__new__(cls, *args, **kargs)
      
         Python2:
      
            class _NamedTupleABC(object):
                __metaclass__ = NamedTupleXABCMeta
                _fields = abstractproperty()
      
                attribute01 = default01
                attribute02 = default02
      
                # common part - see Python3
                ...


Exceptions
----------



.. |bs| raw:: html

   <code>&#92;</code>

.. |dbs| raw:: html

   <code>&#92;&#92;</code>
