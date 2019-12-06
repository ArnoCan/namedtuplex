
.. _CONCEPTS_CLASS_IMPLEMENTATION:

The Implementation Basics of Classes
====================================

Repititorium Class Creation
---------------------------
 
Components of Classes
^^^^^^^^^^^^^^^^^^^^^
The classes are implemented as basic data structures containing data and references to functions
to proceed the data.
This basic concept is honed by various additional concepts for the actual implementation.
In case of *Python* the most implementation details are part of the language definition.
These are for example the magic functions and data members enclosed in double_underscores
*__<member-data-or-function>__*.  
The most prominent disclosed implementation details for the class definition and creation are
here the functions - or more approriate the methods -  *__new__* and *__init*, and the
data *__class__* and *__bases__*.
The class fabric is which has created the class is either referenced by a special member
*__metaclass__*, or could be evaluated dynamic by the call of the *type* function.  

The data members reflect the blueprint of the inheritance structure of the class design.
While in static compiled languages the blueprint has to be defined before compileation 
and is by default not foreseen to be altered, *Python* provides by concept the dynamic 
creation of classes at runtime.
In *Python* the classes are actually runtime instances, which serve as a dynamic instance
fabric.
The actual creation is performed by the so called *metaclass*, either the default *type*,
or a custom class.
Thus *Python* discloses the complete mechanism of class and data creation with standard 
callbacks for user defined procedures. 

Classes and Objects
^^^^^^^^^^^^^^^^^^^
The overall blueprint of the class definition, and the class and instance creation 
could be described in a model of three dimensions.

#. Class-Hierarcy
#. Type-Hierarchy
#. Instance-Containment

The Class-Hierarcy is defined by the abstraction model of the application.
It describes the data and process flow.

The type hierarcy provides the means to implement the Class-Hierarchy into real-world
programs.
In most programming languages these are hidden by the compiler and though not part of
the programming paradigm, *Python* discloses this as a standard part of the programming language.

.. _FIGURE_CLASSCONSTRUCTIONLAYERS:

.. figure:: _static/class-and-objects.png
   :figwidth: 700
   :align: center
   :target: _static/class-and-objects.png
   
   Figure: Class and Instance Elements |classandobjects_zoom|

.. |classandobjects_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/class-and-objects.png
   :width: 16

The Instance-Containment represents the runtime data structure to be used to
process the actual data and provides the workflow to the user.
The cental role in this contex is defined by the methods described in the following sections.

* *__init__* -  for the standard development
* *__new__* -  for the advanced development

Types of Classes and Objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The basic paradigma of *Python* is focused on the dynamic definition and creation of its entities.
This comprises the blueprint and the implementation, while the most other programming languages focus
on for the dynamic runtime environment on the implementation only.
The *Python* runtime environment provides for the dynamic class creation as well 
as the dynamic instance creation.
Thus the classes theirselves are runtime instances.

The basic categories of runtime entities are type instances and object instances.
Where the types are the fabrics for instances of type *object*.
The instances of type *object* provide the basic hooks of the instance items into the
the runtime framework of the *Python* implementation.

The actual implementation of *Python* has varied by different object types due to different
implementation concepts and frameworks.
This was finalized in the so called *new object* type, which also supports a specific runtime
method resolution order  - *MRO*.
This is in particular established as the so called *C3 linearization* [C3LIN]_.

Resulting in the standard items:

* *type* - as the common fabric for classes and and their instances
* *object* - as the top level class, providing the integration of 
  application instances into the runtime framework 

Refer to the *Python* documentation for further details [PYLANG]_.

Call Flow of Class Creation
---------------------------
The essential criteria for the parameter design of the dynamic named tuple extension
is the call flow of instance and though the custom class construction.
 
The basic class construction in Python comprises 3 layers of classes and objects.
The metaclass is only involved in the class construction, while the instanciation of the 
classes are worked out by their defined inheritance hierarchy.
The inheritance hierarchy serves also for the runtime resolution of method calls e.g.
by the "*C3 linearization*" [C3LIN]_ - which is applied for the new *object* types. 

This section provides yet another short overview as a reminder with some conrete example flows
as required for the design of the classes 
:ref:`RETURN_NamedTupleXABC` and :ref:`RETURN_NamedTupleXABCMeta`.
For a detailed overview refer to [customclass]_.
For a detailed article see "Understanding Python metaclasses" [IONELPYMETA]_.

Single Inheritance
^^^^^^^^^^^^^^^^^^
The basic process flow is pretty straight forward in case of single inheritance.

.. _FIGURE_CLASSCONSTRUCTIONLAYERSSINGLE:

.. figure:: _static/class-construction-layers.png
   :figwidth: 500
   :align: center
   :target: _static/class-construction-layers.png
   
   Figure: Class Construction Layers |classconstructionlayers_zoom|

.. |classconstructionlayers_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/class-construction-layers.png
   :width: 16


**Source**
 
   The following example code demonstrates the draft class structure with all *__new__* and *__init__*
   methods present. ::
      
         from __future__ import print_function
         
         import abc
         
         print("0------------------------------")
         print()
         
         class NamedTupleXABCMeta(abc.ABCMeta):
             
             def __new__(cls, *args, **kargs):
                 print("NamedTupleXABCMeta  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, cls).__new__(cls, *args, **kargs)
             
             def __init__(self, *args, **kargs):
                 print("NamedTupleXABCMeta  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, self).__init__(*args, **kargs)
             
             
         class NamedTupleXABC(object):
             __metaclass__ = NamedTupleXABCMeta
             
             def __new__(cls, *args, **kargs):
                 print("NamedTupleXABC      :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABC, cls).__new__(cls, *args, **kargs)
             
             def __init__(self, *args, **kargs):
                 print("NamedTupleXABC      :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABC, self).__init__(*args, **kargs)
         
         class AppTupleClass(NamedTupleXABC):
             _fields = ('a',)
             
             def __new__(cls, *args, **kargs):
                 print("AppTupleClass       :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, cls).__new__(cls, *args, **kargs)
             
             def __init__(self, *args, **kargs):
                 print("AppTupleClass       :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, self).__init__(*args, **kargs)
         
         
         print()
         print("1------------------------------")
         print()
         a = AppTupleClass()
         print()
         
         
         print("OK")


**Result**

   Results in the output:
   
      .. parsed-literal::
      
         0------------------------------
         
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('NamedTupleXABC', ...  # class creation parameters
         NamedTupleXABCMeta  :init   :<class '__main__.NamedTupleXABC'>  ('NamedTupleXABC',  ...
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('AppTupleClass', ... 
         NamedTupleXABCMeta  :init   :<class '__main__.AppTupleClass'>  ('AppTupleClass', ...
         
         1------------------------------
         
         AppTupleClass       :new    :<class '__main__.AppTupleClass'>  ()  {}                       # instance creation parameters
         NamedTupleXABC      :new    :<class '__main__.AppTupleClass'>  ()  {}
         AppTupleClass       :init   :<__main__.AppTupleClass object at 0x7f99d6daf6d0>  ()  {}
         NamedTupleXABC      :init   :<__main__.AppTupleClass object at 0x7f99d6daf6d0>  ()  {}
         
         OK

**Discussion**

   With the call flow:
   
      0. Create global class definitions as objects by themselfs.
         These are each created and initialized completeley, because of the order each is completely
         defined by itself and the eventually required previous already created classes.
      
         1. NamedTupleXABC:
         
            1. Create - __new__
            2. Initialize - __init__
      
         2. AppTupleClass:
      
            1. Create - __new__
            2. Initialize - __init__
            
      1. Create instances/objects.
         Each instance is created completely by walking through the upward hierarchy in the 
         inheritance hierarchy. Resulting in combined creation following combined initialization.
      
         1. Create - new
         
            1. AppTupleClass
            2. NamedTupleXABC
      
         2. Initialize - __init__
      
            1. AppTupleClass
            2. NamedTupleXABC
   
   As depicted, a metaclass itself is not created here by the applications metaclass but 
   provided by the systems *type*.
   The application defined metaclasses serve as the class factory and create and initialize
   all assigned classes by calling *__new__* and *__init__*.
   Here *AppTupleClass* and *NamedTupleXABC*.
   
   The instance creation is performed along the inheritance hierarchy starting at the derived class.
   The applications abstract metaclasses are not involved in the instance creation calls.
   The call hierarchy is first processed for the creation, second for the initialization.
   
   For the application by *namedtuplex* refer 
   to :ref:`Creation of the Named Tuple <CREATIONOFTHENAMEDTUPLE>`.

Multiple Inheritance - Mixin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The process flow changes when an instance of a named tuple class is taken into account.
The additional named tuple class in the actual implementation is hereby created by the
factory defined by :ref:`param_tuplefactory`.
The created *namedtuple* class is the first in the list of base classes *__bases__*, thus called by 
default by the *super* method.
The abstract class is the second in the list and is not requied to be called after 
instanciation anyhow.

.. _FIGURE_CLASSCONSTRUCTIONLAYERSMIXIN:

.. figure:: _static/class-construction-layers-namedtuple.png
   :figwidth: 650
   :align: center
   :target: _static/class-construction-layers-namedtuple.png
   
   Figure: Class Construction Layers with Mixin |classconstructionlayersnamedtuple_zoom|

.. |classconstructionlayersnamedtuple_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/class-construction-layers-namedtuple.png
   :width: 16

**Source**
 
   The following example code demonstrates the draft class structure with all *__new__* and *__init__*
   methods present. ::
      
         from __future__ import print_function
         
         import abc
         import namedtupledefs
         
         
         print("0------------------------------")
         print()
         
         _MyTuple = namedtupledefs.namedtuple('MyTuple', 'x y z', fielddefaults=(22,33))
         class MyTuple(_MyTuple):
             def __new__(cls, *args, **kargs):
                 print("MyTuple  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(MyTuple, cls).__new__(cls, *args, **kargs)
         
             def __init__(self, *args, **kargs):
                 print("MyTuple  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(MyTuple, self).__init__(*args, **kargs)
             
         class NamedTupleXABCMeta(abc.ABCMeta):
         
             def __new__(cls, *args, **kargs):
                 print("NamedTupleXABCMeta  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, cls).__new__(cls, *args, **kargs)
         
             def __init__(self, *args, **kargs):
                 print("NamedTupleXABCMeta  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, self).__init__(*args, **kargs)
         
         
         class NamedTupleXABC(object):
             __metaclass__ = NamedTupleXABCMeta
         
             def __new__(cls, *args, **kargs):
                 print("NamedTupleXABC      :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABC, cls).__new__(cls, *args, **kargs)
         
             def __init__(self, cls, *args, **kargs):
                 print("NamedTupleXABC      :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 
                 # the abc.ABC passes __init__ to type()
                 return super(NamedTupleXABC, self).__init__()
         
         
         class AppTupleClass(MyTuple, NamedTupleXABC):
             # 
             # The mixin is actually created by the metaclass, here defined static for demonstration
             #
             _fields = ('a',)
         
             def __new__(cls, *args, **kargs):
                 print("AppTupleClass  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, cls).__new__(cls, *args, **kargs)
          
             def __init__(self, *args, **kargs):
                 print("AppTupleClass  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, self).__init__(*args, **kargs)
         
         
         print()
         print("1------------------------------")
         print()
         a = AppTupleClass(11, 22)  # uses default for 'z'
         print()
         print(a)
         
         print("OK")


**Result**

   Results in the output:
   
      .. parsed-literal::
      
         warning: Debugger speedups using cython not found. Run '"/home/acue/venv/2.7.14/bin/python2.7" "/local/hd1/home1/env/ide/eclipse/eclipse-cpp-neon-3-linux-gtk-x86_64-20171019-devops_18/dropins/PyDev 7.0.3/plugins/org.python.pydev.core_7.0.3.201811082356/pysrc/setup_cython.py" build_ext --inplace' to build.
         pydev debugger: starting (pid: 2857)
         0------------------------------
         
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('NamedTupleXABC', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.NamedTupleXABCMeta'>, '__new__': <function __new__ at 0x7f5e2c1bee60>, '__init__': <function __init__ at 0x7f5e2c1beed8>})  {}
         NamedTupleXABCMeta  :init   :<class '__main__.NamedTupleXABC'>  ('NamedTupleXABC', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.NamedTupleXABCMeta'>, '__new__': <function __new__ at 0x7f5e2c1bee60>, '__init__': <function __init__ at 0x7f5e2c1beed8>})  {}
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('AppTupleClass', (<class '__main__.MyTuple'>, <class '__main__.NamedTupleXABC'>), {'__module__': '__main__', '_fields': ('a',), '__new__': <function __new__ at 0x7f5e2a742230>, '__init__': <function __init__ at 0x7f5e2a7422a8>})  {}
         NamedTupleXABCMeta  :init   :<class '__main__.AppTupleClass'>  ('AppTupleClass', (<class '__main__.MyTuple'>, <class '__main__.NamedTupleXABC'>), {'__module__': '__main__', '_fields': ('a',), '__new__': <function __new__ at 0x7f5e2a742230>, '__init__': <function __init__ at 0x7f5e2a7422a8>})  {}
         
         1------------------------------
         
         AppTupleClass  :new    :<class '__main__.AppTupleClass'>  (11, 22)  {}
         MyTuple  :new    :<class '__main__.AppTupleClass'>  (11, 22)  {}
         AppTupleClass  :init   :MyTuple(x=11, y=22, z=33)  (11, 22)  {}
         MyTuple  :init   :MyTuple(x=11, y=22, z=33)  (11, 22)  {}
         NamedTupleXABC      :init   :MyTuple(x=11, y=22, z=33)  (22,)  {}
         
         MyTuple(x=11, y=22, z=33)
         OK

**Discussion**

   With the call flow:
   
      0. Create global class definitions as objects by themselfs.
         These are each created and initialized completeley, because of the order each is completely
         defined by itself and the eventually required previous already created classes.
      
         1. NamedTupleXABC:
         
            1. Create - __new__
            2. Initialize - __init__
      
         2. AppTupleClass:
      
            1. Create - __new__
            2. Initialize - __init__
            
      1. Create instances/objects.
         Each instance is created completely by walking through the upward hierarchy in the 
         inheritance hierarchy. Resulting in combined creation following combined initialization.
      
         1. Create - new
         
            1. AppTupleClass
            2. NamedTupleXABC
      
         2. Initialize - __init__
      
            1. AppTupleClass
            2. NamedTupleXABC
   
   As depicted, a metaclass itself is not created here by the applications metaclass but 
   provided by the systems *type*.
   The application defined metaclasses serve as the class factory and create and initialize
   all assigned classes by calling *__new__* and *__init__*.
   Here *AppTupleClass* and *NamedTupleXABC*.
   
   The instance creation is performed along the inheritance hierarchy starting at the derived class.
   The applications abstract metaclasses are not involved in the instance creation calls.
   The call hierarchy is first processed for the creation, second for the initialization.
   
   For the application by *namedtuplex* refer 
   to :ref:`Creation of the Named Tuple <CREATIONOFTHENAMEDTUPLE>`.


The Structure of *namedtuplex*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Source**

   The following example code displays the structure as actually defined by *namedtuplex*.
   The implemented demonstration method stubs are at the same positions as the originals.
   The only adaptation is the callwrapper for the tuple class *MyTuple* of the demonstrator.
   Thus the callflow traces are the same. ::
      
         from __future__ import print_function
         
         import abc
         import namedtupledefs
         
         
         print("0------------------------------")
         print()
         
         _MyTuple = namedtupledefs.namedtuple('MyTuple', 'x y z', fielddefaults=(22,33))
         class MyTuple(_MyTuple):
             def __new__(cls, *args, **kargs):
                 print("MyTuple  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(MyTuple, cls).__new__(cls, *args, **kargs)
         
             def __init__(self, *args, **kargs):
                 print("MyTuple  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(MyTuple, self).__init__(*args, **kargs)
             
         class NamedTupleXABCMeta(abc.ABCMeta):
         
             def __new__(cls, *args, **kargs):
                 print("NamedTupleXABCMeta  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, cls).__new__(cls, *args, **kargs)
         
             def __init__(self, *args, **kargs):
                 print("NamedTupleXABCMeta  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(NamedTupleXABCMeta, self).__init__(*args, **kargs)
         
         
         class NamedTupleXABC(object):
             __metaclass__ = NamedTupleXABCMeta
             _fields = abc.abstractproperty()
         
         class AppTupleClass(MyTuple, NamedTupleXABC):
             # **The mixin is actually created by the metaclass, here defined static for demonstration**
             _fields = ('a',)
         
             def __new__(cls, *args, **kargs):
                 print("AppTupleClass  :new    :"  + str(cls) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, cls).__new__(cls, *args, **kargs)
          
             def __init__(self, *args, **kargs):
                 print("AppTupleClass  :init   :"  + str(self) + "  " + str(args) + "  " + str(kargs))
                 return super(AppTupleClass, self).__init__(*args, **kargs)
         
         
         print()
         print("1------------------------------")
         print()
         a = AppTupleClass(11, 22)  # uses default for 'z'
         print()
         print(a)
         
         print("OK")


**Result**

   Results in the output:
   
      .. parsed-literal::
      
         0------------------------------
         
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('NamedTupleXABC', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.NamedTupleXABCMeta'>})  {}
         NamedTupleXABCMeta  :init   :<class '__main__.NamedTupleXABC'>  ('NamedTupleXABC', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.NamedTupleXABCMeta'>})  {}
         NamedTupleXABCMeta  :new    :<class '__main__.NamedTupleXABCMeta'>  ('AppTupleClass', (<class '__main__.MyTuple'>, <class '__main__.NamedTupleXABC'>), {'__module__': '__main__', '_fields': ('a',), '__new__': <function __new__ at 0x7f2f5617c050>, '__init__': <function __init__ at 0x7f2f5617c140>})  {}
         NamedTupleXABCMeta  :init   :<class '__main__.AppTupleClass'>  ('AppTupleClass', (<class '__main__.MyTuple'>, <class '__main__.NamedTupleXABC'>), {'__module__': '__main__', '_fields': ('a',), '__new__': <function __new__ at 0x7f2f5617c050>, '__init__': <function __init__ at 0x7f2f5617c140>})  {}
         
         1------------------------------
         
         AppTupleClass  :new    :<class '__main__.AppTupleClass'>  (11, 22)  {}
         MyTuple  :new    :<class '__main__.AppTupleClass'>  (11, 22)  {}
         AppTupleClass  :init   :MyTuple(x=11, y=22, z=33)  (11, 22)  {}
         MyTuple  :init   :MyTuple(x=11, y=22, z=33)  (11, 22)  {}
         
         MyTuple(x=11, y=22, z=33)
         OK

**Discussion**

   The call flow is the same as before, while the new call of the application class *AppTupleClass*
   is eventually present in rare cases only.
     
   The call flow once again:
   
      0. Create global class definitions as objects by themselfs.
         These are each created and initialized completeley, because of the order each is completely
         defined by itself and the eventually required previous already created classes.
      
         1. NamedTupleXABC:
         
            1. Create - __new__
            2. Initialize - __init__
      
         2. AppTupleClass:
      
            1. Create - __new__
            2. Initialize - __init__
            
      1. Create instances/objects.
         Each instance is created completely by walking through the upward hierarchy in the 
         inheritance hierarchy. Resulting in combined creation following combined initialization.
      
         1. Create - new
         
            1. AppTupleClass
            2. NamedTupleXABC
      
         2. Initialize - __init__
      
            1. AppTupleClass
            2. NamedTupleXABC
   
   For the application by *namedtuplex* refer 
   to :ref:`Creation of the Named Tuple <CREATIONOFTHENAMEDTUPLE>`.

