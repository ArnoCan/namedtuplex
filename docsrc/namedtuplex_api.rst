.. raw:: html

   <div class="shortcuttab">

.. _NAMEDTUPLEXAPI:

The namedtuplex API
===================
The *namedtuplex* API covers a variety of interfaces for the processing of 
resource path addresses, and the search of resources.
The initial set of interfaces forcusses on filesystem resources in a basic distributed
environment.
This covers in particular a basic set of call parameters, which are common for a
subset of the call interfaces. 

.. raw:: html
   
   <style>
      div.apisynopsislarge blockquote {
         font-size: 1.5ch;
      }
   </style>
   
   <div class="apisynopsislarge">
   <div class="apisynopsis">


.. _IF_CLASSES:

* **classes**
  
   .. parsed-literal::
   
      :ref:`ABC (alias of NamedTupleXABC) <RETURN_ABC>`
      :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>`
      
.. _IF_CLASSESHELPER:

* **helper classes**

   .. parsed-literal::
   
      :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>`

.. raw:: html

   </div>
   </div>


.. _API_PARAMS_BASIC:

.. _API_PARAMS_FULL:

The following table displays the standard parameters supported by the interfaces.

   .. raw:: html
   
      <div class="tabcolumncolor">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
         
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | interface                                      | factories              |                           | classes                                               |                                           |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   |                                                | collections.namedtuple | namedtupledefs.namedtuple | :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>` | :ref:`AppClass <CREATIONOFTHENAMEDTUPLE>` |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | parameter                                      | [namedtuple]_          | [namedtupledefs]_         | :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>`         |                                           |
   +================================================+========================+===========================+=======================================================+===========================================+
   | :ref:`fields <param_fieldnames>`               | c                      | c                         | :ref:`m+c <param_fieldnames>`                         | :ref:`m <param_fieldnames>`               |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`fielddefaults <param_fielddefaults>` (1) | --                     | c                         | :ref:`m+c <param_fielddefaults>`                      | :ref:`m <param_fielddefaults>`            |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`merge <param_merge>`                     | --                     | --                        | :ref:`m+c <param_merge>`                              | :ref:`m <param_merge>`                    |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`module <param_module>` (2) (3)           | c                      | c                         | :ref:`m+c <param_module>`                             | :ref:`m <param_module>`                   |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`rename <param_rename>` (3)               | c                      | c                         | :ref:`m+c <param_rename>`                             | :ref:`m <param_rename>`                   |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`tuplefactory <param_tuplefactory>`       | --                     | --                        | :ref:`m+c <param_tuplefactory>`                       | :ref:`m <param_tuplefactory>`             |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`typename <param_typename>`               | c                      | c                         | :ref:`s <param_typename>`                             | :ref:`s <param_typename>`                 |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+
   | :ref:`verbose <param_verbose>` (3)             | c                      | c                         | :ref:`m+c <param_verbose>`                            | :ref:`m <param_verbose>`                  |
   +------------------------------------------------+------------------------+---------------------------+-------------------------------------------------------+-------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
   
   **m**:
      Parameter as class member variable, which is processed byt the metaclass for class creation
      and/or instance creation. 
      In case of member variable these are prefixed by an underscore '_'.
      For example the members **_fields** and **_fielddefaults**:
      
         .. parsed-literal::
         
            class MyClassNonABC(namedtuplex.abc.NamedTupleXABC):
               **_fields** = ('a', 'b',)                      # processed during class creation
               **_fielddefaults** = (('a', 11), ('b', 22))        # processed during class creation and/or instance creation 
   
   **s**:
      Parameter by standard class definition, e.g. the mixin **MyMixinClass**:
      
         .. parsed-literal::
         
            class MyClassNonABC(**MyMixinClass**, namedtuplex.abc.NamedTupleXABC):
               _fields = ('a', 'b',)
   
   **c**:
   
      Parameter as call parameters, either for methods, or functions.
      The method interfaces provide here parameters to be interpreted by the methods of static
      defined class members, while the function interface provide parameters for the dynamic 
      creation of the assembled classes.
      
      For example the parameters **rename** and **fielddefaults** are used by
      the factory *namedtuplex.abc.namedtuplex()* for the creation of the extended tuple
      class template as well as for the creation of the class. 
      E.g.:
      
         .. parsed-literal::
         
            namedtuplex.abc.namedtuplex(
               'MyClass',                              # passed to *collections.namedtuple* 
               ('a', 'b',),                            # processed and passed to *collections.namedtuple*
               rename=True,                            # processed and passed to *collections.namedtuple*
               fielddefaults=(('a', 11), ('b', 22),)   # processed by **__new__** for class and instance creation
            )
   
   **(c)**:
      Call parameters provided by the system interface, e.g. for the *__new__* call.

   **(1)**:
      Depends on the actual *tuplefactory*.

   **(2)**:
      Depends on the implementation, *Python3.6+*.

   **(3)**:
      Optional parameters, these are venetually not available in all cases.


The inheritance  of the special class members *_fields* and *_fielddefaults* 
is based on two behaviour patterns controlled by the member *_merge*.
When the value of *_merge* is *True*, the values of *_fileds* and *_fielddefaults* 
are merged by *right-hand* concatenation to the values from the parent class.
In case of *mixin* the values are merged by *from-left-to-right*
concatenation to the values defined by the derived class.
The values of *_fielddefaults* are merged by the required
compliance to the behaviour of function defauls [PYFUNC]_.
Thus with a resulting right-hand side continous tuple of default values. 

The following table depicts the inheritance behaviour and the possiblity
of control by *_merge*.

   .. raw:: html
   
      <div class="tabcolumncolor">
      <div class="nonbreakheadtab">
      <div class="autocoltab">
         
   +---------------------------------------------+-----------+------------+-----------------------------+
   | class member                                | inherited | merge-ctrl | default                     |
   +=============================================+===========+============+=============================+
   | :ref:`_fields <param_fieldnames>`           | y         | y          | *None*                      |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_fielddefaults <param_fielddefaults>` | y         | y          | *None*                      |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_merge <param_merge>`                 | y         | n          | *True*                      |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_module <param_module>`               | y         | n          | *None*                      |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_rename <param_rename>`               | y         | n          | *False*                     |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_tuplefactory <param_tuplefactory>`   | n         | n          | *namedtupledefs.namedtuple* |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_typename <param_typename>`           | n         | n          | classname                   |
   +---------------------------------------------+-----------+------------+-----------------------------+
   | :ref:`_verbose <param_verbose>`             | y         | n          | *False*                     |
   +---------------------------------------------+-----------+------------+-----------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>
   
The *_fields* and *_fielddefaults* members are merged by default,
this could be prohibited by *_merge=False*.
The default behaviour seems to be appropriate due to the nature of tuples and the
most possible intention of inheritance for the extension of a previously defined
base pattern.
For example in order to extend the header of a protocol message with a message body. 
This makes sense, even though tuples are commonly not intended for inheritance.


.. _NAMEDTUPLEXAPI_PARAMETERS:

Parameters
----------

.. index::
   pair: parameters; fieldnames
   pair: parameters; _fields

.. _param_fieldnames:

fields and _fields
^^^^^^^^^^^^^^^^^^
Symbolic names of fields with identical semantics as the standard library *collections.namedtuple*.
When used in combination with the parameter *fielddefaults* the semantics changes to the behaviour
of function parameters with default values, see [PYFUNC]_.  

   .. parsed-literal::

      fields := '(' <field-name> [, <fields>] ')'
      field-name := <valid-character-one>[<field-name-tail>] 
      field-name-tail := <valid-character>[<field-name-tail>]
      valid-character-one := [a-zA-Z] 
      valid-character := [a-zA-Z_0-9] 

See also `usage of parameters <genindex.html#P>`_, 
:ref:`design _fields <DESIGN_FIELDS>`,
and [namedtuple]_.


.. index::
   pair: parameters; _fielddefaults
   pair: parameters; fielddefaults

.. _param_fielddefaults:

fielddefaults and _fielddefaults
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Optional support for default values of *fields*.
A list of key-value pairs.
Same semantics as the function call interfaces [PYFUNC]_,

   .. parsed-literal::

      fielddefaults := '(' <item-default> [, <fielddefaults>] ')'
      item-default := '(' <key>, <value> ')'
      key := (<item-index> | <item-name>)
      value := <default-value>

See also `usage of parameters <genindex.html#P>`_,
and
:ref:`design _fields <DESIGN_FIELDDEFAULTS>`.


.. index::
   pair: parameters; merge
   pair: parameters; _merge

.. _param_merge:

merge and _merge
^^^^^^^^^^^^^^^^
Sets the behaviour for the metaclass how to proceed with multiple base classes provided as
mixin.
The default behaviour is to merge the :ref:`_fields <param_fieldnames>` and the 
:ref:`_fielddefaults <param_fielddefaults>` attributes.
The merge requires the following prerequisites:

1. The *fieldnames* must be valid.
2. The merged *fielddefaults* has to comply to the Python function default options syntax [PYFUNC]_.
   This in particular requires right-hand non-scattered values for the merged tuples.

   For example:
   
     .. parsed-literal::
     
        class A:
            _fields = ('a', 'b', 'c',)
            _fielddefaults = (33,)

        class B:
            _fields = ('d', 'e', 'f',)
            _fielddefaults = (66,)
        
        class Merged(A, B):
            _merge = True
        

   This will not work, because the defaults for 'd' and 'e' are not determined:

     .. parsed-literal::

        class Merged(A, B):
            _merge = True

        # The meged fields: 
        #    _fields = ('a', 'b', 'c', 'd', 'e', 'f',)
        #    _fielddefaults = (33, ?, ?, 66,)      # **causes an error**
                                                   # c=33, d=?, e=?, f=66

   While the following will work:
       
     .. parsed-literal::
     
        class A:
            _fields = ('a', 'b', 'c',)
            _fielddefaults = (33,)

        class B:
            _fields = ('d', 'e', 'f',)
            _fielddefaults = (44, 55, 66,)

        class Merged(A, B):
            _merge = True

   Resulting in:

     .. parsed-literal::

        # The meged fields: 
        #    _fields = ('a', 'b', 'c', 'd', 'e', 'f',)
        #    _fielddefaults = (33, 44, 55, 66,)    # **this works**
                                                   # c=33, d=44, e=55, f=66

A typical example for this is to use it for protocol data units, e.g. assemble the message header and body.
Another example is to assemble a tuple for log entries with a line-prefix concatenated with the logged message.
       
default := *True*

See also `usage of parameters <genindex.html#P>`_,
and :ref:`INTERFACEPARAMETERSNAMEDTUPLEX`.

.. index::
   pair: parameters; module

.. _param_module:

module and _module
^^^^^^^^^^^^^^^^^^
Sets '*__module__*' of the created class definition.
Available beginning with *Python-3.6*.

See also `usage of parameters <genindex.html#P>`_,
:ref:`design module <DESIGN_MODULE>`,
and [namedtuple]_.

.. index::
   pair: parameters; rename

.. _param_rename:

rename and _rename
^^^^^^^^^^^^^^^^^^
If *True* replaces silently invalid field names by
'*_<item-index>*'.
Available beginning with *Python-2.7*, in *Python3* beginning with  *Python-3.1* - so not in *Python-3.0*.

See also `usage of parameters <genindex.html#P>`_, 
:ref:`design rename <DESIGN_RENAME>`,
and [namedtuple]_.

.. index::
   pair: parameters; typename

.. _param_typename:

typename
^^^^^^^^
Name of returned class of type *namedtuple*.
The actual registered top-level base class is *NamedTupleXABC* - underneath *object* of course.

See also `usage of parameters <genindex.html#P>`_, 
and [namedtuple]_.

.. index::
   pair: parameters; tuplefactory

.. _param_tuplefactory:

tuplefactory and _tuplefactory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The *tuplefactory* provides an alternative factory for the creation of a named tuple.
The *API* has to support the identical interface, but is free to support more.
The keyword parameters are passed through transparently after removing the 
template class specific options.
Current available standard factories are:

   .. parsed-literal::
   
      tuplefactory := (
         namedtupledefs.namedtuple   # patched version of *collections.namedtuple* with *fielddefaults* 
         collections.namedtuple      # standard library - no *fielddefaults*
      ) 

default := *namedtupledefs.namedtuple*

See also `usage of parameters <genindex.html#P>`_,
and :ref:`design tuplefactory <DESIGN_TUPLEFACTORY>`.

.. index::
   pair: parameters; verbose

.. _param_verbose:

verbose and _verbose
^^^^^^^^^^^^^^^^^^^^
Prints created class definition.

See also `usage of parameters <genindex.html#P>`_, 
:ref:`design verbose <DESIGN_VERBOSE>`,
and [namedtuple]_.




The call interface provides for groups of functions and classes with a set of 
common parameters and additional context specific modifications.

The provided function sets comprise the categories:

* Filesystem Positions and Navigation

* Canonical Node Address

Various common options are supported, which may not be available for each interface.

.. _NAMEDTUPLEX_REFERENCES:

Resources
---------

* [IONELPYMETA]_ Understanding Python metaclasses
* [NAMEDTUPLEABC]_ namedtuple.abc - abstract base class + mix-in for named tuples (Python recipe)
* [PEP3119]_  -- Abstract base classes according to PEP 3119
* [PYFUNC]_ The Python Language Reference - Function definitions
* [abc]_ lib/abc
* [customclass]_ reference/datamodel
* [namedtuple]_ lib/collections
* [type]_ lib/type



.. raw:: html

   </div>

.. |bs| raw:: html

   <code>&#92;</code>

.. |dbs| raw:: html

   <code>&#92;&#92;</code>
   