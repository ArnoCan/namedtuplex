
.. _SWDESIGN:

The SW-Design of *namedtuplex*
******************************
The basic :ref:`Call Flow of Class Creation <CONCEPTS_CLASS_IMPLEMENTATION>` is
adapted here to the special requirements of the creation of named tuples.

.. _CREATIONOFTHENAMEDTUPLE:

Creation of the Named Tuple
===========================
The class provided by the call of the factory function *namedtupledefs.namedtuple*, or
alternatively by the :ref:`tuplefactory <param_tuplefactory>` *collections.namedtuple*, 
is extended by the abstract class *NamedTupleXABC*.
The fabrication of the class is processed by the metaclass *NamedTupleXABCMeta*, where
the provided named tuple class is set as a base class of the application interface *NamedTupleXABC*.
The abstract class *NamedTupleXABC* provides a base class for the feature extension implemented by
the class *AppClass* through inheritance.

.. _FIGURE_CLASSCONSTRUCTIONLAYERSNAMEDTUPLE:

.. figure:: _static/class-construction-layers-namedtuple.png
   :figwidth: 600
   :align: center
   :target: _static/class-construction-layers-namedtuple.png
   
   Figure: Class Construction Layers for namedtuple |classconstructionlayersnamedtuple_zoom|

.. |classconstructionlayersnamedtuple_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/class-construction-layers-namedtuple.png
   :width: 16

Creation by Inheritance
-----------------------
The class interfaces :ref:`namedtuplex.abc.NamedTupleXABC <DOC_RETURN_NamedTupleXABC>` 
and :ref:`namedtuplex.abc.ABC <DOC_RETURN_NamedTupleXABC>`
provide the creation of the named tuple by inheritance.
The parameters are designed to be passed as atributes in this case.  
E.g. the attribute *_fields* of the *namedtuple* contains the symbolic names of the fields of the *tuple*.
For the complete list refer to :ref:`API prameters <API_PARAMS_FULL>`.


Creation by the Factory
-----------------------
The class factory :ref:`namedtuplex.abc.namedtuplex <namedtuplex_APPPARTS>` provides a call interface with the dynamic creation
of the class.
The factory therefore supports more options, which are passed as call parameters to the function.

The field names are provided for the standard call of *namedtupledefs.namedtuple* as parameters,
for example with *fielddefaults*:

   .. parsed-literal::
   
      namedtupledefs.namedtuple('ClsName', ('field0', 'field1',), fielddefaults=(value1,))

or

   .. parsed-literal::
   
      namedtupledefs.namedtuple('ClsName', ('field0', 'field1',), fielddefaults=(value0, value1,))

For the standard library of *collections.namedtuple* without the *fielddefaults* feature, e.g.:

   .. parsed-literal::
   
      collections.namedtuple('ClsName', ('field0', 'field1',))
 

Resulting Class Structure
-------------------------

.. _FIGURE_DESIGN_STRUCTURE:

.. figure:: _static/structure.png
   :figwidth: 750
   :align: center
   :target: _static/structure.png
   
   Figure: Class Diagram of NamedTupleX |structure_zoom|

.. |structure_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/structure.png
   :width: 16


.. _INTERFACEPARAMETERSNAMEDTUPLEX:

Class Interface Parameters NamedTupleX
======================================

The *namedtuplex* package extends the standard interface.
This includes multiple parameters provided as class variables for
the class and the instance creation, see also [customclass]_.
For an example of the processing and inheretance of *namedtuple* see  
implementation by *Jan  Kaliszewski* [JANKALI]_ [NAMEDTUPLEABC]_.

The provided class variables of derived classes are processed by the *__new__* method of the
metaclass *NamedTupleXABCMeta*.

.. index::
   pair: parameters; fields
   pair: parameters; fielddefaults
   pair: parameters; _fields
   pair: parameters; _fielddefaults

.. _DESIGN_FIELDS:
.. _DESIGN_FIELDDEFAULTS:

_fields and _fielddefaults
--------------------------
The *namedtuplex* supports the parameters *_fields* and *_fielddefaults*.


The implementation is based on the namedtuple factory.
When default values are required, these are delegated to the factory class,
which in case of *namedtupledefs.namedtuple* generates the appropriate default
values for the call interface of the created class.
Thus the default based dynamic class creation is required by the *__new__* method of
the adaptation of the tuple fields at the creation time by the *__new__* method of
:ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>`.

In case of the factory *collections.namedtuple* default values are currently not
available.

.. _FIGURE_CLASSCONSTRUCTIONLAYERSNAMEDTUPLEX:

.. figure:: _static/class-construction-namedtuplex.png
   :figwidth: 700
   :align: center
   :target: _static/class-construction-namedtuplex.png
   
   Figure: Custom Class Construction NamedTupleX |classconstructionlayersnamedtuple1_zoom|

.. |classconstructionlayersnamedtuple1_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/class-construction-namedtuplex.png
   :width: 16

The following calls are processed interfaces in the given order. 
The index numbers *figure* refers to the marks at the previous figure.

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | interface  | figure | processed class/object                        | called method                                               | class param                                           | processed |
   +============+========+===============================================+=============================================================+=======================================================+===========+
   | *__new__*  | 1.     | :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>` | :ref:`NamedTupleXABCMeta.__new__ <NamedTupleXABCMeta_new>`  | :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>` | yes       |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__init__* | 2.     | *NamedTupleXABC*                              | *NamedTupleXABCMeta.__init__*                               | *NamedTupleXABC*                                      | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__new__*  | 1.     | *AppTupleClass*                               | :ref:`NamedTupleXABCMeta.__new__ <NamedTupleXABCMeta_new>`  | :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>` | yes       |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__init__* | 2.     | *AppTupleClass*                               | *NamedTupleXABCMeta.__init__*                               | *AppTupleClass*                                       | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__new__*  | 3.     | *AppTupleClass*                               | *AppTupleClass.__new__*                                     | *AppTupleClass*                                       | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__new__*  | 3.     | *NamedTupleXABC*                              | *NamedTupleXABC.__new__*                                    | *AppTupleClass*                                       | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__init__* | 4.     | *AppTupleClass* (obj)                         | *AppTupleClass.__init__*                                    | *object<AppTupleClass>*                               | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+
   | *__init__* | 4.     | *NamedTupleXABC* (obj)                        | *NamedTupleXABC.__init__*                                   | *object<AppTupleClass>*                               | no        |
   +------------+--------+-----------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------+-----------+

   .. raw:: html
   
      </div>
      </div>
      </div>


The application needs to define the marked "*A*" class member values :ref:`_fields <param_fieldnames>`
and optional the :ref:`_fielddefaults <param_fielddefaults>`.
The value :ref:`_fields <param_fieldnames>` defines the number of fields and their symbolic names for the named tuple,
while the :ref:`_fielddefaults <param_fielddefaults>`  member defines function interface style defaults [PYFUNC]_.
The :ref:`_fields <param_fieldnames>` value is processed at the marked inteface "*1.*", while 
the :ref:`_fielddefaults <param_fielddefaults>` value is processed at the marked interface "*3.*".

The following example demonstrates the partial default values:

   .. parsed-literal::
   
       class AppTupleClass(NamedTupleXABC):
          :ref:`_fields <param_fieldnames>` = ('a', 'b', 'c', 'd')
          :ref:`_fielddefaults <param_fielddefaults>` = (('c', 33), ('b', 22), ('d', 44))  # **order is irrelevant**
          
       myobj = AppTupleClass(11, 22)  # **allows partial calls**
       
       print(myobj)       

results in:

   .. parsed-literal::
   
      (11, 22, 33, 44)


The following example demonstrates the case default values only.
In this case the default values replace the *_fileds* parameter completely:

   .. parsed-literal::
   
       class AppTupleClass(NamedTupleXABC):
          :ref:`_fields <param_fieldnames>` = ()                                                   # when empty
          :ref:`_fielddefaults <param_fielddefaults>` = (('a', 11), ('c', 33), ('b', 22), ('d', 44))  # _fielddefaults is used - allows empty calls
                                                                         # **order is relevant**

       myobj = AppTupleClass()  # **allows empty calls**

       print(myobj)       

results in:

   .. parsed-literal::
   
      (11, 33, 22, 44)


See also :ref:`param_fieldnames` and :ref:`param_fielddefaults`. 


.. index::
   pair: parameters; _module
   pair: parameters; module

.. _DESIGN_MODULE:

_module
-------
The module name is available beginning with *Python-3.6*.
The value replaces the member variable *__module__* of the created tuple.

See also :ref:`param_module`. 

.. index::
   pair: parameters; _rename
   pair: parameters; rename

.. _DESIGN_RENAME:

_rename
-------

The *rename* defines the optional renaming of invalid field names.
This is transparently passed to the *namedtuple* class.

See also :ref:`param_rename`. 

.. index::
   pair: parameters; _tuplefactory
   pair: parameters; tuplefactory

.. _DESIGN_TUPLEFACTORY:

_tuplefactory
-------------

The *tuplefactory* defines the used factory function for the creation of the named tuple.
This is by default *namedtupledefs.namedtuple*, and could be changed to a compatible
alternativesuch as *collections.namedtuple*.

See also :ref:`param_tuplefactory`. 


.. index::
   pair: parameters; _verbose
   pair: parameters; verbose

.. _DESIGN_VERBOSE:

_verbose
--------

The *verbose* is processed by the *namedtuple* factory and prints the dynamic created
tuple class [namedtuple]_ and [namedtupledefs]_.
Thi parameter is for debugging only.

See also :ref:`param_verbose`. 

Parameters of namedtuple
========================
The following parameters are passed to the *collections.namedtuple* [namedtuple]_.

.. index::
   pair: parameters; rename

* :ref:`tuplefactory <param_tuplefactory>`
* :ref:`module <param_module>`
* :ref:`rename <param_rename>`
* :ref:`verbose <param_verbose>`

See also `usage of parameters <genindex.html#P>`_.

