
********
Abstract
********


The *namedtuplex* package provides extended named tuples with additional features
including an abstract base class, standard and extended class factories with
function-style default values and additional parameters.

.. figure:: _static/structure.png
   :figwidth: 650
   :align: center
   :target: _static/structure.png
   
   Figure: Class Diagram of namedtuples |structure_zoom| :ref:`more... <REFERENCE_ARCHITECTURE>`

.. |structure_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/structure.png
   :width: 16

The best application is for return values as tuples with a variable number 
of valid members. 
The provided *namedtuplex* class fabric could be used as a drop-in replacement of the standard
*namedtuple* [namedtuple]_.

The current release supports:

- **ineritance**:
   Inheritance of abstract and non-abstract classes.
- **mixin**:
   The use of the generated tuple class as mixin.
- **symbolic fieldnames**
   Alternative symbolic names for the fields of the tuple, see also [namedtuple]_.
- **default values**
   Default values for the fields, supports partial fields for the initialization
   of the generated class - similar to function arguments [PYFUNC]_.
- **attributes**:
   Additional non-field attributes for the created tuple including default values.
- **abstract tuple classes**
   Creates an abstract tuple class in accordance to [PEP3119]_, see also [abc]_     
- **performance impact**
   The performance impact of the created named tuple class is compared to the
   *collections.namedtuple* none, compared to the standard *tuple* negligible.
   The created named tuple class actually uses the *tuple* as it's base class,
   where the add-ons are performed for the customized creation only.  

For an overview with additional details refer to the following section :ref:`Blueprint <INDEX_BLUEPRINT>`.

For the extended *namedtupledefs.namedtuple* with *fielddefaults* see [namedtupledefs]_.
For the standard library *collections.namedtuple* see Python documentation [NAMEDTUPLEABCREF]_.
For the fast enumeration of the *Python* implementation and release refer to [pythonids]_.

