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
from ECLparser.datatypes import Quad, sctId, target, groupId

from ECLparser.rf2_substrate.RF2_Substrate_Sctids import Sctids
from ECLparser.rf2_substrate.RF2_Substrate_Common import *

from rf2db.db.RF2RelationshipFile import RelationshipDB
from ECLparser.z import Set
from ECLparser.z.z import _Instance



class RF2_Quad(Quad.SchemaInstance):
    def __init__(self, e):
        Quad.SchemaInstance.__init__(self, Quad, s=sctId(e[1]), a=sctId(e[2]), t=target(t_sctid=sctId(e[3])), g=groupId(e[4]))
        self.id = e[0]


    def __str__(self):
        return "[id:%s, s:%s, a:%s, t:%s, g:%s]" % (self.id, self.s, self.a, self.t, self.g)

# if #rf=0 ∧ (firstec=eco eq) then
# quad value({q : ss.relationships |
#      q.a ∈ atts ∧ q.t ∈ rant sctid ∧ (t sctid∼q.t) ∈ (result sctids ecv)}, source direction)
#
# if #rf>0 ∧ (firstec=eco eq) then
# quad value({q : ss.relationships |
#      q.a ∈ atts ∧ q.s ∈ (result sctids ecv)}, targets direction)
#
# if #rf=0 ∧ (firstec=eco neq)
# quad value({q : ss.relationships | q.a ∈ atts ∧ q.t ∈ rant sctid ∧ (t sctid∼q.t) ∈/
#                                     (result sctids ecv)}, source direction)
#
# else quad value({q : ss.relationships |
#     q.a ∈ atts ∧ q.s ∈/( result sctids ecv)},targets direction))


class Set_Quad(Set):
    def __init__(self):
        Set.__init__(self, Quads)
        self._type = Quads

    def has_member(self, other):
        return isinstance(other, Quads)


class Quads(RF2_Substrate_Common, _Instance, Set):
    _db = RelationshipDB()
    _andSTMT = "SELECT DISTINCT t1.id FROM (%s) AS t1 JOIN (%s) AS t2 ON t1.id = t2.id"
    _orSTMT = "SELECT DISTINCT t.id FROM ((%s) UNION (%s)) as t"
    _minusSTMT = "SELECT DISTINCT t1.id FROM (%s) AS t1 LEFT JOIN (%s) AS t2 ON t1.id = t2.id WHERE t2.id IS NULL"
    _data_type = RF2_Quad

    def __init__(self, rf: bool=False, atts: Sctids=None, eq: bool=True, ecv: Sctids=None):
        """
        Construct a set of quads from
        :param rf: reverse flag.  If true ecv applies to source.  If false, destination
        :param atts: attributes (types)
        :param eq: If true, test for equal, if false, for not equal
        :param ecv: sources / destinations for testing
        :return:
        """
        Set.__init__(self, Quads)
        _Instance.__init__(self, RF2_Quad)
        RF2_Substrate_Common.__init__(self)
        self._val = self
        self._type = Quads

        self._len = None                # number of elements
        self._query = "SELECT id, sourceId, typeId, destinationId, relationshipGroup FROM %s" % RelationshipDB.fname()
        self._query += " WHERE "
        if atts:
            self._query += (("typeId IN (%s)" % atts.as_sql()) if eq else
                            ("typeId NOT IN (%s)" % atts.as_sql())) + " AND "
        if ecv:
            self._query += (("sourceId IN (%s)" % ecv.as_sql()) if rf else
                            ("destinationId IN (%s)" % ecv.as_sql())) + " AND "
        self._query += "active=1 AND locked=0"
        self.rf = rf

    def to_sctids(self):
        return Sctids(filtr=("id IN (SELECT DISTINCT r.destinationId FROM (%s) AS r) " % self.as_sql()) if self.rf else
                            ("id IN (SELECT DISTINCT r.sourceId FROM (%s) AS r)" % self.as_sql()))

    def __contains__(self, item: RF2_Quad) -> bool:
        query = "SELECT count(t.id) FROM %s" % RelationshipDB.fname()
        query += " WHERE " + \
                 "t.sourceId = %s AND t.destinationId = %s AND t.typeId = %s and t.relationshipGroupId = %s" % \
                 (item.s, item.t, item.a, item.g)
        query += " FROM (%s) as t" % self.as_sql()
        return int(list(self._execute_query(self._countSTMT % query))[0]) > 0

    def i_required_cardinality(self, min_, max_, rf):
        src = 'destinationId' if rf else 'sourceId'
        sql = self.as_sql()
        query = "SELECT DISTINCT rc.%s AS id FROM  " % src
        if min_ <= 1 and not max_:
            query += "(%s) " % sql
        else:
            query += "(SELECT c.%s, COUNT(c.id) AS c FROM (%s) AS c " % (src, sql)
            query += "GROUP BY c.%s) WHERE "
            query += "COUNT(c.id) >= %s" % min_ if min_ > 1 else "1"
            query += " AND "
            query += "COUNT(c.id) <= %s" % max_ if max_ else "1"
        query += "AS rc"
        return Sctids(query=query)
