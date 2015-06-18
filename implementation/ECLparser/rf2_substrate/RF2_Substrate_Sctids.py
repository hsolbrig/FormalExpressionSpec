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
from collections import Container, Sized

from rf2db.db.RF2ConceptFile import ConceptDB
from ECLparser.datatypes import sctid

from ECLparser.z.z import Set, _Instance

concdb = ConceptDB()


def _v(**kwargs):
    return kwargs

_countSTMT = "SELECT count(t.id) FROM (%s) AS t"
_andSTMT = "SELECT DISTINCT t1.id FROM (%s) AS t1 JOIN (%s) AS t2 ON t1.id = t2.id"
_orSTMT = "SELECT DISTINCT t.id FROM ((%s) UNION (%s)) as t"
_minusSTMT = "SELECT DISTINCT t1.id FROM (%s) AS t1 WHERE t1.id NOT IN (%s)"

class Set_Sctids(Set):
    def __init__(self):
        Set.__init__(self, Sctids)
        self._type = sctid

    def has_member(self, other):
        return isinstance(other, Sctids)


class Sctids(_Instance, Set):

    def __init__(self, filtr=None, query=None):
        """
        Construct a virtual sctid set
        :param filtr: One of a textual SQL filter, a generator for SCTID's or None (wild card)
        :param query: A complete query -- result of and, or or minus
        """
        Set.__init__(self, Sctids)
        _Instance.__init__(self, Sctids)
        self._val = self
        self._type = sctid
        self._len = None                # number of elements
        if query is not None:
            self._query = query
        else:
            if filtr is not None and not isinstance(filtr, str):
                sctid_list = filtr if isinstance(filtr, Container) else [filtr]
                filtr = 'id IN (' + ','.join(str(e) for e in sctid_list) + ')'
            self._query = concdb.buildQuery(**self._build_parms(filtr))

    @staticmethod
    def _build_parms(filtr):
        """ Build the parameters to pass to the RF2ConceptFile buildQuery
        :return:
        """
        return _v(maxtoreturn=-1, sort='none', id_only=True, filtr=filtr)

    @staticmethod
    def _execute_query(query):
        db = concdb.connect()
        db.execute(query)
        return db.ResultsGenerator(db)

    def as_sql(self):
        return '\n' + self._query + '\n'

    def __len__(self) -> int:
        """
        :return: the actual length of the set when resolved against the substrate
        """
        if self._len is None:
            self._len = int(list(self._execute_query(_countSTMT % self._query))[0])
        return self._len

    def __ge__(self, other) -> bool:
        """ Return true other is a subset of self
        :param other: a set of sctids
        :return:
        """
        return len(other) == len(self & other)

    def __gt__(self, other) -> bool:
        """ Return true if other is a proper subset of self
        :param other: a generator for a set of sctids
        :return:
        """
        return len(self) > len(other) and self >= other

    def __lt__(self, other) -> bool:
        """ Return true if self is a proper subset of other
        :param other: a generator for a set of sctids
        :return:
        """
        return other > self

    def __le__(self, other) -> bool:
        """ Return true if self is a subset of other
        :param other: a generator for a set of sctids
        :return:
        """
        return other >= self

    def __eq__(self, other) -> bool:
        """ Return true if self and other have the same members
        :param other: a generator for a set of sctids
        :return:
        """
        return len(self) == len(other) and self >= other

    def __contains__(self, item) -> bool:
        item_c = Sctids(item)
        return len(self & item_c) == (len(item) if isinstance(item, Sized) else 1)

    def isdisjoint(self, other):
        return len(self & other) == 0

    def __and__(self, other):
        """ Return a Sctids instance that represents the intersection of self and other
        :param other: Sctids object to intersect with self
        :return: Sctids object that represents intersection
        """
        return Sctids(query=_andSTMT % (self._query, other.as_sql()))

    def intersect(self, other):
        return self & other

    def __or__(self, other):
        """ Return the union of the sctids in self and other
        :param other: a generator for a set of sctids
        :return: Generator for sctids
        """
        return Sctids(query=_orSTMT % (self._query, other.as_sql()))

    def union(self, other):
        return self | other

    def __sub__(self, other):
        return Sctids(query=_minusSTMT % (self._query, other.as_sql()))

    def minus(self, other):
        return self - other

    def __xor__(self, other):
        return (self | other) - (self & other)

    def __iter__(self):
        return self.iter(self._execute_query(self._query))

    class iter:
        def __init__(self, q):
            self._v = q

        def __next__(self):
            return int(self._v.__next__())
