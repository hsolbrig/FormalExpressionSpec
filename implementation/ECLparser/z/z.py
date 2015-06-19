# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import sys

from _collections_abc import Sized
from collections import Iterable, OrderedDict

"""This module suports the basic Z types and operations. """


class _Z_Builtin:
    pass


class _Instance:
    def __init__(self, cls):
        self.cls = cls


# Built in types Z and N
class Z(int, _Z_Builtin):
    @staticmethod
    def has_member(v):
        return isinstance(v, int)


class N(Z):
    def __init__(self, val):
        super().__init__()
        assert N.has_member(val), "Type error"

    @staticmethod
    def has_member(v):
        return Z.has_member(v) and v >= 0


class N_1(N):
    def __init__(self, val):
        N.__init__(self, val)
        assert N_1.has_member(val), "Type error"

    @staticmethod
    def has_member(v):
        return N.has_member(v) and v > 0


# Basic Type
class BasicType:
    """ Basic Type declaration
    Z:       [Name, Date]
             today : Date

    Python:  Name = BasicType
             Date = BasicType
             today = BasicType()
    """

    def __str__(self):
        return "[" + self.__class__.__name__ + "]"

    @classmethod
    def has_member(cls, v):
        return type(v) is cls


class _MetaType:
    def __init__(self, instance_type):
        self._real_type = instance_type

    def __call__(self, *args, **kwargs):
        return self._real_type(self, *args, **kwargs)

    def has_member(self, other):
        assert False, "Must be implemented"  # Virtual function

    @staticmethod
    def is_instance(val, typ):
        """
        :param val: Value to test the type for
        :param typ: Type to be tested
        :return: True if typ is compatible with val
        """
        if isinstance(typ, Forward):
            typ = typ.ref
        return val is None if typ is None else \
               val.cls == typ if isinstance(val, _Instance) else \
               val in typ if isinstance(typ, Iterable) else \
               typ.has_member(val) if isinstance(typ, _MetaType) else \
               typ.has_member(val) if isinstance(typ, type) and issubclass(typ, _Z_Builtin) else \
               isinstance(val, typ)


# Free Type
class FreeType(_MetaType):
    """ Free type declaration
    Z:       Ans ::= ok<<Z>> | error
    Python:  Ans = FreeType(ok=int, error=None)
    Z:       Degree ::= status <<0..3>>
             ba = status 0
    Python:  Degree = FreeType(status=range(0,4))
             ba = Degree('status', 0)

    """

    def __init__(self, **options):
        """ Create a new free type
        :param options: collection of label:type or label:None if no associated data
        :return:
        """
        _MetaType.__init__(self, FreeType.FreeTypeInstance)
        # For any sort of deterministic behavior, our options need to be ordered.
        # We sort Forward references are sorted to the top to minimize recursion (see: has_member below
        keys = list(options.keys())
        keys.sort()
        orderedopts = [(k, options[k]) for k in keys if isinstance(options[k], Forward)] + \
                      [(k, options[k]) for k in keys if not isinstance(options[k], Forward)]
        self.options = OrderedDict(orderedopts)

    def assign(self, val):
        """ Determine the appropriate label given the type
        :param val: value
        :return: FreeTypeInstance with the appropriate type assigned
        """
        for key, value_type in self.options.items():
            if value_type is None and val is None:
                return self.__call__(**{key: None})
            elif isinstance(value_type, Iterable) and val in value_type:
                return self.__call__(**{key: val})
            elif value_type.has_member(val):
                return self.__call__(**{key: val})
        assert False, "Unknown value type"

    def has_member(self, other):
        """ Determine whether other is a member of this free type
        :param other: FreeType to be tested
        :return:
        """
        if isinstance(other, _Instance) and other.cls == self:
            return True
        for k, v in self.options.items():
            if (not isinstance(v, Forward) or v.ref != self) and _MetaType.is_instance(other, v):
                return True
        return False
        # return (isinstance(other, _Instance) and other.cls == self) or \
        #        any(_MetaType.is_instance(other, v) for v in self.options.values())

    def __eq__(self, other):
        return isinstance(other, FreeType) and other.options == self.options

    def __str__(self):
        return "\n\t" + '\n\t\t'.join(["%s= ⟨⟨ %s ⟩⟩" % e for e in self.options.items()])

    class FreeTypeInstance(_Instance):

        def __init__(self, cls, *args, **kwargs):
            _Instance.__init__(self, cls)
            assert len(args) == 0, "Must use a keyword for constructing a free type"
            assert len(kwargs) == 1, "Only one constructor allowed"
            key, val = kwargs.popitem()
            assert key in self.cls.options, "Unknown constructor type (%s)" % key
            self.__dict__['_key'] = key
            self._hash = hash(frozenset(self.__dict__))

            value_type = self.cls.options[key]
            # TODO: fix this
            # assert _MetaType.is_instance(val, value_type)
            self.__dict__['_value'] = val

        def __getattr__(self, item):
            if item.startswith('_'):
                return AttributeError
            assert self._key == item, "Wrong type (%s, %s)" % (self._key, item)
            return self._value

        def __eq__(self, other):
            if not isinstance(self, FreeType.FreeTypeInstance) or \
                    not isinstance(other, FreeType.FreeTypeInstance):
                return False
            return self._key == other._key and self._value == other._value

        def __hash__(self):
            return self._hash

        def inran(self, item):
            assert item in self.cls.options, "Unknown constructor type"
            return self._key == item

        def __str__(self):
            return self._key + ' ⟨⟨ ' + str(self._value) + " ⟩⟩\n"


setattr(sys.modules[__name__], 'FreeTypeInstance', FreeType.FreeTypeInstance)  # to enable pickling


# Sets
class Set(_MetaType):
    minlen = 0

    def __init__(self, typ):
        _MetaType.__init__(self, Set.SetInstance)
        self._type = typ

    def same_type_as(self, other):
        return self._type == other._type

    def __eq__(self, other):
        return isinstance(other, Set) and self.same_type_as(other)

    def has_member(self, other):
        if isinstance(other, Set.SetInstance):
            other = other.v
        # TODO: type checking loosened to prevent unnecessary queries
        # return ((isinstance(self._type, _MetaType) and all(self._type.has_member(v) for v in other)) or
        return (isinstance(self._type, _MetaType) or
                (isinstance(self._type, type) and issubclass(self._type, _Z_Builtin) and all(
                    self._type.has_member(v) for v in other)) or True)
                # all(isinstance(v, self._type) for v in other)) and len(other) >= self.minlen

    class SetInstance(_Instance):
        def __init__(self, cls, *val):
            _Instance.__init__(self, cls)
            if len(val) == 1 and isinstance(val[0], Iterable):
                val = val[0]
            assert self.cls.has_member(val)
            self._val = frozenset(list(val))

        @property
        def v(self):
            return self._val

        def __iter__(self):
            return self.v.__iter__()

        def subseteq(self, other) -> bool:
            assert self.cls.same_type_as(other.cls), "Types must match"
            return self.v <= other.v

        def subset(self, other) -> bool:
            assert self.cls.same_type_as(other.cls), "Types must match"
            return self.v < other.v

        def union(self, other):
            assert self.cls.same_type_as(other.cls), "Types must match"
            return self.cls(self.v | other.v)

        def intersect(self, other):
            assert self.cls.same_type_as(other.cls), "Types must match"
            return self.cls(self.v & other.v)

        def difference(self, other):
            assert self.cls.same_type_as(other.cls), "Types must match"
            return self.cls(self.v - other.v)

        def _bigcup(self, others):
            return (self.v | others[0]._bigcup(others[1:])) if others else self.v

        def _bigcap(self, others):
            return (self.v & others[0]._bigcup(others[1:])) if others else self.v

        def __str__(self):
            return " {" + ','.join(str(e) for e in self.v) + "} "

        def __contains__(self, item):
            return item in self.v

        @staticmethod
        def bigcup(typ, members):
            # TODO: Fix this
            # assert all([e.cls._type == typ for e in members]), "Sets must be the same type"
            return Set(typ)() if not len(members) else \
                   members[0] if len(members) == 1 else \
                   members[0]._bigcup(members[1:])

        @staticmethod
        def bigcap(typ, members):
            assert all([e.cls._type == typ for e in members]), "Sets must be the same type"
            return Set(typ)() if not len(members) else members[0]._bigcap(members[1:])


setattr(sys.modules[__name__], 'SetInstance', Set.SetInstance)  # to enable pickling

# Sequences
class Seq(_MetaType):
    minlen = 0
    maxlen = None

    def __init__(self, type_):
        _MetaType.__init__(self, Seq.SeqInstance)
        self._val = None
        self._type = type_

    def __eq__(self, other):
        return isinstance(other, Seq) and self._type == other._type

    def has_member(self, other:Sized):
        if isinstance(other, Seq.SeqInstance):
            other = other.v
        if other is None:
            other = []
        if not isinstance(other, Iterable):
            return False
        return len(other) >= self.minlen and (self.maxlen is None or len(other) <= self.maxlen) and \
               (all(self._type.has_member(v) for v in other) if isinstance(self._type, _MetaType) else \
                    all(isinstance(v, self._type) for v in other))

    class SeqInstance(_Instance):
        def __init__(self, cls, *val):
            _Instance.__init__(self, cls)
            if len(val) == 1 and isinstance(val[0], Iterable) and not isinstance(val[0], str):
                val = val[0]
            elif len(val) == 1 and val[0] is None:
                val = []
            if isinstance(self.cls._type, _MetaType) or \
                    (isinstance(self.cls._type, type) and issubclass(self.cls._type, _Z_Builtin)):
                assert all(self.cls._type.has_member(v) for v in val)
            else:
                assert all(isinstance(v, self.cls._type) for v in val)
            assert len(val) >= self.cls.minlen and \
                   (self.cls.maxlen is None or len(val) <= self.cls.maxlen), "Size violation"
            self._val = tuple(val)

        @property
        def v(self):
            return self._val

        @property
        def head(self):
            assert not self.is_empty, "Head undefiend for empty sequence"
            return self._val[0]

        @property
        def tail(self):
            assert not self.is_empty, "Tail undefined for empty sequence"
            return Seq(self.cls._type)(self._val[1:])

        @property
        def is_empty(self):
            return len(self._val) == 0

        def _eqtypes(self, other, f):
            assert self.cls._type == other.cls._type, "Sequences must be the same type"

        def concat(self, other):
            self._eqtypes(other, 'concat')
            return self.cls(self.v + other.v)

        def __eq__(self, other):
            self._eqtypes(other, 'eq')
            return self.v == other.v

        def __str__(self):
            return ("⟨ " + ', '.join([str(e) for e in self.v]) + "⟩ ") if len(self.v) else "∅"

        def __contains__(self, item):
            return item in self.v

        def filter(self, filtr):
            return self.cls([e for e in self.v if e in filtr])

        @property
        def card(self):
            return len(self.v)


setattr(sys.modules[__name__], 'SeqInstance', Seq.SeqInstance)  # to enable pickling


class Seq_1(Seq):
    minlen = 1


class CrossProduct(_MetaType):
    def __init__(self, t1=None, t2=None):
        _MetaType.__init__(self, CrossProduct.CrossProductInstance)
        self._type1 = t1
        self._type2 = t2
        self._val = None

    def assign(self, v1, v2):
        return self.__call__(v1, v2)

    def has_member(self, other):
        if isinstance(other, CrossProduct.CrossProductInstance):
            other = other.cls
        return isinstance(other, CrossProduct) and self._same_types(other)

    def _same_types(self, other):
        return (self._type1 is None or other._type1 is None or
                self._type1 == other._type1) and \
               (self._type2 is None or other._type2 is None or
                self._type2 == other._type2)

    def __eq__(self, other):
        return isinstance(other, CrossProduct) and self._same_types(other)

    class CrossProductInstance(_Instance):
        def __init__(self, cls, v1, v2):
            _Instance.__init__(self, cls)
            assert self.cls._type1 is None or \
                   (isinstance(self.cls._type1, _MetaType) and self.cls._type1.has_member(v1)) or \
                   (isinstance(self.cls._type1, type) and isinstance(v1,
                                                                     self.cls._type1)), "Wrong type for first element"
            assert self.cls._type2 is None or \
                   (isinstance(self.cls._type2, _MetaType) and self.cls._type2.has_member(v2)) or \
                   (isinstance(self.cls._type2, type) and isinstance(v2,
                                                                     self.cls._type2)), "Wrong type for second element"
            self._val = (v1, v2)

        def has_member(self, other):
            return self.cls.has_member(other)

        @property
        def first(self):
            return self._val[0]

        @property
        def second(self):
            return self._val[1]

        @property
        def v(self):
            return self._val

        def __eq__(self, other):
            if not isinstance(self, CrossProduct.CrossProductInstance) or \
                    not isinstance(other, CrossProduct.CrossProductInstance):
                return False
            assert self.cls._type1 == other.cls._type1 and self.cls._type2 == other.cls._type2, "incompatible types"
            return self.v == other.v

        def __str__(self):
            return "(" + str(self._val[0]) + " ⟼ " + str(self._val[1]) + ")"


setattr(sys.modules[__name__], 'CrosProductInstance', CrossProduct.CrossProductInstance)  # to enable pickling


class Forward(_MetaType):
    class unresolved:
        def __init__(self, *args, **kwargs):
            assert False, "Unresolved forward reference"

        def has_member(self, other):
            return False

    def __init__(self):
        _MetaType.__init__(self, None)
        self._ref = Forward.unresolved
        self._recursive = False

    def __lshift__(self, other:_MetaType):
        assert self._ref == Forward.unresolved, "Forward element already resolved"
        self._ref = other

    def __call__(self, *args, **kwargs):
        return self._ref(*args, **kwargs)

    def __eq__(self, other):
        # Forwards exist to prevent recursion, so we have to just return True if both sides are forwards...
        return isinstance(other, Forward) or self._ref == other

    @property
    def ref(self):
        return self._ref

    def assign(self, val):
        return self._ref.assign(val)

    def has_member(self, other):
        return self._ref.has_member(other)

    def __str__(self):
        rval = "(Fwd) "
        if not self._recursive:
            self._recursive = True
            rval += str(self._ref)
            self._recursive = False
        else:
            rval += "(Recursive definition)"
        return rval


# Schema type
class Schema(_MetaType):
    def __init__(self, *preds, **decls):
        _MetaType.__init__(self, Schema.SchemaInstance)
        self.preds = preds
        self.decls = decls  # Not order preserving

    def has_member(self, other):
        # TODO: this definition is too restrictive, but will work for now
        return isinstance(other, Schema.SchemaInstance) and other.cls == self

    def __eq__(self, other):
        return isinstance(other, Schema) and self.decls == other.decls

    class SchemaInstance(_Instance):
        def __init__(self, cls, **kwargs):
            """ Construct an instance of a schema
            :param cls: meta class for this class/type
            :param kwargs: name/value tuples for contents
            """
            _Instance.__init__(self, cls)
            missing_args = kwargs.copy()
            for key, val in kwargs.items():
                assert key in self.cls.decls, "Unknown attribute"
                value_type = self.cls.decls[key]
                assert _MetaType.is_instance(val, value_type), "Unknown value type"
                self.__dict__[key] = val
                missing_args.pop(key)
            assert not missing_args, "Missing arguments"
            for p in self.cls.preds:
                assert p(self)
            self._hash = hash(frozenset(self.__dict__))

        def __eq__(self, other):
            """ Two schemas are equal if they have the same names and types
            :param other: Other schema to test
            :return: True if they are both schemas with the same names, types and values
            """
            return isinstance(other, Schema.SchemaInstance) and \
                   set(self.cls.decls) == set(other.cls.decls) and \
                   all(getattr(self, v) == getattr(other, v) for v in self.cls.decls.keys())

        def __str__(self):
            return "[" + ', '.join(key + '=' + str(getattr(self, key)) for key in self.cls.decls) + "]"

        def __hash__(self):
            return self._hash


setattr(sys.modules[__name__], 'SchemaInstance', Schema.SchemaInstance)  # to enable pickling
