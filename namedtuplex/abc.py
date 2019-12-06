# -*- coding: utf-8 -*-
"""The package 'namedtuplex' provides an extended call interface and classes for *namedtuples*.
"""
from __future__ import absolute_import
from __future__ import print_function

from namedtupledefs import namedtuple as _namedtuple

from abc import ABCMeta, abstractproperty
from copy import copy, deepcopy

from pythonids import ISSTR, PYV27X

from namedtuplex import NamedTupleXParameterError


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez" \
                "@Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.1'
__uuid__ = "e3590f7b-2a97-4091-9534-d203d49a92ad"

__docformat__ = "restructuredtext en"


if PYV27X:
    # avoid nested exceptions for Python2
    class ModuleNotFoundError(Exception):
        """For compatibilty with Python3.
        """
        pass
    # for Jython use native python2 syntax - see later 


class NamedTupleXABCMeta(ABCMeta):
    """The metaclass for named tuples as an abstract base with support 
    for inheritance and mixin. 
    For the abstract class refer to :ref:`NamedTupleXABC <RETURN_NamedTupleXABC>`.
    """

    def __new__(cls, name, bases, namespace, **kargs):
        """Adds the symbolic field names for the indices and selected attributes
        as member variables.  
 
        Args:
            cls:
                The created class.
 
            name:
                The name of the created class.
             
            bases:
                List of base classes.
             
            namespace:
                The namespace, containing the *_fields* class variable.
             
            kargs:
                fields:
                    The *fields* parameter provides a list of alternate names 
                    for the contained *tuple* members. This in advance defines 
                    the required  mandatory number of items for the *tuple*.  
 
                        .. parsed-literal::
                         
                            fields := (
                                  '"' <index-names> '"' 
                                | '[' <index-list>  ']'
                                | '(' <index-list>  ')'
                            )
                             
                            index-names := <index-name>[[ ,] <index-names>]
                            index-list := <index-name>[, <index-list>]
                            index-name := "valid name for the field index of the tuple"
 
                fielddefaults:
                    Defines default values for the *fields* of the tuple. This 
                    allows for the variable length initialization of the created 
                    *namedtuple* class.
 
                        .. parsed-literal::
                         
                            fielddefaults := '(' <default-list> ')'
                             
                            default-list := '(' <key> ',' <value> ')'
                            key := (
                                  <field-index>
                                | <field-name>
                            ) 
                            field-index := "valid integer index of a present field"
                            field-name := "valid name from the list _fields"
                            value :=  "default value"
 
                    Default values are supported in accordance to the standard Python
                    behaviour of call parameters [PYFUNC]_.

                module
                    Sets *__module__* of the created class definition.
                    
                    Available beginning with *Python-3.6*.
                    See [namedtuple]_.
                
                tuplefactory:
                    The class factory to be used for the named tuple.
                    
                    default := *collections.namedtuple*

                rename:
                    If *True* replaces silently invalid field names by
                    '_<item-index>'.

                    default := *False*
                    
                    Available *Python-2.7* and in *Python-3.x* see manuals "...beginning with Python3.1".
                    See [namedtuple]_.
                    
                useslots:
                    Creates a member *__slots__*.

                    default := *True*
    
                    See [namedtuple]_.

                verbose:
                    Prints created class definition.

                    default := *False*
    
                    See [namedtuple]_.

        Returns:
            An abstract class derived from *namedtuple* with alternative
            symbolic names for the contained items. In addition predefined
            attributes are included.

        Raises:
            NamedTupleXParameterError
            
            pass-through
             
        """
        #
        # parameters by class members
        #
        
        #
        # defines the name of the created named tuple class
        # default is 'namedtuple_<classname>' 
        #
        _typename = namespace.get('_typename')
        if _typename != None:
            name = _typename

        #
        # defines the inheritance of _fields and _fielddefaults
        #
        try:
            _merge = kargs.pop('merge')
        except KeyError:
            _merge = namespace.get('_merge', True)

        #
        # The presence of the _fields attribute defines the used 
        # base for each set of attributes. This in particular
        # defines the related _fielddefaults
        #
        
        #
        # fieldnames - superpose parents
        #
        try:
            _fieldnames = kargs.pop('fields')
        except KeyError:
            _fieldnames = namespace.get('_fields', None)
        if isinstance(_fieldnames, abstractproperty):
            # it is abstract, so nothing more to do
            return ABCMeta.__new__(cls, name, bases, namespace)
        
        try:
            _fielddefaults = kargs.pop('fielddefaults')
        except KeyError:
            _fielddefaults = namespace.get('_fielddefaults', None)


        if _merge or (_fieldnames is None and _merge is not False):
            # if no fieldnames of merge is forced, merges the parent
            # classes fields and fielddefaults,
            # else the local definition superposes parent classes

            # is not abstract, and has no fieldname, thus possibly inherits
            for base in bases:
                _f = getattr(base, '_fields', ())
                if _f is None:
                    # check next
                    continue
                if isinstance(_f, abstractproperty):
                    # it is the ABC
                    continue

                _d = getattr(base, '_fielddefaults', None)
                if _d is not None:
                    
                    if _fielddefaults is not None:
                        if len(_f) != len(_d):
                            raise NamedTupleXParameterError(
                                "default values are right bound and must not be scattered")
                        _fielddefaults += _d
                    else:
                        # is the first set
                        _fielddefaults = _d
                elif _fielddefaults and _f:
                    # the previous left-hand mixins have defaults, so need for 
                    # all current _fields a default too 
                    raise NamedTupleXParameterError(
                        "default values are right bound and must not be scattered")                    
                
                if type(_f) in ISSTR:
                    # is sstring with space separated field names - normalize 
                    _f = _f.split(' ')
                if _fieldnames is None:
                    # is the first
                    _fieldnames = _f
                else:
                    # just concat
                    _fieldnames += _f

                if _merge == False:
                    break

        #
        # the following attributes are used from current namespace only 
        #
        try:
            _tuplefactory = kargs.pop('tuplefactory')
        except KeyError:
            _tuplefactory = namespace.get('_tuplefactory', None)

        try:
            _module = kargs.pop('module')
        except KeyError:
            _module = namespace.get('_module', None)

        try:
            _rename = kargs.pop('rename')
        except KeyError:
            _rename = namespace.get('_rename', None)

        try:
            _verbose = kargs.pop('verbose')
        except KeyError:
            _verbose = namespace.get('_verbose', None)


        if _tuplefactory == None:
            _tuplefactory = _namedtuple
        namespace['_tuplefactory'] = _tuplefactory

        if _module != None:
            kargs['module'] = _module
        if _rename != None:
            kargs['rename'] = _rename
        if _verbose != None:
            kargs['verbose'] = _verbose

        if _fielddefaults != None:
            kargs['fielddefaults'] = _fielddefaults

        if _fieldnames is not None and not isinstance(_fieldnames, abstractproperty):
            # is non-abstract class
            mytuple = _tuplefactory("%s_%s" % (_tuplefactory.__name__, name), _fieldnames, **kargs)
            bases = (mytuple,) + bases
            namespace.setdefault('__doc__', mytuple.__doc__)
            namespace.setdefault('__slots__', ())

            #
            # relies on the *tuplefactory*
            #
            if hasattr(mytuple, '_fields'):
                namespace.pop('_fields', None)
            if hasattr(mytuple, '_fielddefaults'):
                namespace.pop('_fielddefaults', None)

        return ABCMeta.__new__(cls, name, bases, namespace)


def with_metaclass(meta, *bases):
    """
    Function from future/utils.py License: BSD.
        Function from jinja2/_compat.py. License: BSD.

    Do need a wrapper only for the compilation-breaking 
    metaclass syntax of Python2/Python3. Require
    this on all platforms - including *Jython*.
    
    Original doc-string:
        
        Function from jinja2/_compat.py. License: BSD.
    
        Use it like this::
    
            class BaseForm(object):
                pass
    
            class FormType(type):
                pass
    
            class Form(with_metaclass(FormType, BaseForm)):
                pass
    
        This requires a bit of explanation: the basic idea is to make a
        dummy metaclass for one level of class instantiation that replaces
        itself with the actual metaclass.  Because of internal type checks
        we also need to make sure that we downgrade the custom metaclass
        for one level to something closer to type (that's why __call__ and
        __init__ comes back from type etc.).
    
        This has the advantage over six.with_metaclass of not introducing
        dummy classes into the final MRO.
    """
    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__
        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})


class NamedTupleXABC(with_metaclass(NamedTupleXABCMeta), object):
    """The abstract class for extended *tuple* classes.
    The metaclass syntax is based on *future.utils* [future.utils]_ with support for 
    both *Python* syntax variants of *Python2.7* and *Python3*.
    For the metaclass refer to :ref:`NamedTupleXABCMeta <RETURN_NamedTupleXABCMeta>`.
    """
      
    _fields = abstractproperty()  #: The abstract property, see abc.abstractproperty [abc]_, and :ref:`param_fieldnames`.
    _fielddefaults = None  #: Optional default values for _fields in function-paramater style see :ref:`param_fielddefaults`.

    def merge(self, *others, **kargs):
        """Creates a new instance by concatenating the *others* to the copy
        of current instance created with standard members. Additional 
        attributes, properties, and methods have to be processed by 
        derived classes.
        
        Args:
            others:
                Instances of tuples to be merged into this instance. The merge
                is processed by right-hand concatenation of *others*.
                
                The supported types are:
                    ::

                        NamedTupleXABC
                        OrderedDict      # same as from '_asdict()'
                        <namedtuple>     # the result of 'namedtuple()' 
                        tuple            # when 'rename' is 'True'

            kargs:
                deep:
                    If *True* merges a deep copy of all, else a swallow copy only.
                    
                    default := *False*
                
                module:
                    Optional parameter to be passed to the *tuplefactory*.
                    
                    default := *None*
                    
                rename:
                    Optional parameter to be passed to the *tuplefactory*.
                    
                    default := *None*
                
                tuplefactory:
                    The *tuplefactory* callable to be used for the new named tuple.
                    
                    default := *namedtupledefs.namedtuple*

                verbose:
                    Optional parameter to be passed to the *tuplefactory*.
                    
                    default := *None*
                
                
        Returns:
            A new instance of merged objects.
            
        Raises:
        
            ValueError
            
            pass-through
        """
        _kw = {}
        
        if kargs.get('deep'):
            _fn = deepcopy(self._fields)
            _fd = deepcopy(self._fielddefaults)  # spare None-check
        else:
            _fn = copy(self._fields)
            _fd = copy(self._fielddefaults)  # spare None-check


        if kargs.get('verbose'):
            _kw["verbose"] = kargs.get('verbose')
        elif hasattr(self, 'verbose'):
            _kw["verbose"] = self.verbose
        
        if kargs.get('rename'):
            _kw["rename"] = kargs.get('rename')
        elif hasattr(self, 'rename'):
            _kw["rename"] = self.rename
        
        if kargs.get('module'):
            _kw["module"] = kargs.get('module')
        elif hasattr(self, 'module'):
            _kw["module"] = self.module


        _t = ()
        for o in others:
            if not hasattr(o, '_fields') or not hasattr(o, '_fielddefaults'):
                raise ValueError(
                    "supports only classes from: namedtupledefs.namedtuple " + str(o))
        
            # check for non-scattered function style default values
            if _fd and (not o._fielddefaults or len(o._fielddefaults) != len(o._fields)):
                raise ValueError(
                    "default values are right bound and must not be scattered: %s / %s"
                    %(str(o._fields), str(o._fielddefaults))
                    )

            _fn += o._fields
            _fd += o._fielddefaults
            _t  += o  # want the tuple values without fiddling
            
        # resulting names have to be valid - the tuple will check finally 
        tp = self.__class__(self.__class__.__name__, _fn, fielddefaults=_fd, **_kw)
        return tp(*tuple.__add__(self, _t))


#: Reference to the abstract base class.
ABC = NamedTupleXABC #@UndefinedVariable   

#: Reference to the metaclass
ABCMETA = NamedTupleXABCMeta   
