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


def _v(**kwargs):
    return kwargs


class RF2_Substrate_Common:
    _db = None
    _andSTMT = None
    _orSTMT = None
    _minusSTMT = None
    _data_type = int

    _countSTMT = "SELECT COUNT(t.id) FROM (%s) AS t"

    def __init__(self):
        self._len = None
        self._query = None
        self._cls = None

    def _execute_query(self, query):
        db = self._db.connect()
        db.execute(query)
        return db

    def as_sql(self):
        return self._query

    def __len__(self) -> int:
        """
        :return: the actual length of the set when resolved against the substrate
        """
        if self._len is None:
            self._len = int(list(self._execute_query(self._countSTMT % self._query))[0][0])
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

    def isdisjoint(self, other):
        return len(self & other) == 0

    def __and__(self, other):
        """ Return a Sctids instance that represents the intersection of self and other
        :param other: Sctids object to intersect with self
        :return: Sctids object that represents intersection
        """
        return type(self)(query=self._andSTMT % (self._query, other.as_sql()))

    def __or__(self, other):
        """ Return the union of the sctids in self and other
        :param other: a generator for a set of sctids
        :return: Generator for sctids
        """
        return type(self)(query=self._orSTMT % (self._query, other.as_sql()))

    def __sub__(self, other):
        return type(self)(query=self._minusSTMT % (self._query, other.as_sql()))

    def __xor__(self, other):
        return (self | other) - (self & other)

    def __iter__(self):
        return self.iter(self._execute_query(self._query), self._data_type)

    class iter:
        def __init__(self, q, typ):
            self._v = q
            self._t = typ

        def __next__(self):
            return self._t(self._v.__next__())
