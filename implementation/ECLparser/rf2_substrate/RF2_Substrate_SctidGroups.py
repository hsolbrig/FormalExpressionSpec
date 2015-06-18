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
from ECLparser.rf2_substrate.RF2_Substrate_Common import RF2_Substrate_Common
from ECLparser.rf2_substrate.RF2_Substrate_Sctids import Sctids
from rf2db.db.RF2RelationshipFile import RelationshipDB


class SctidGroup:
    def __init__(self, e):
        self.sctid = e[0]
        self.group = e[1]

    def __str__(self):
        return "[sctid: %s, gid: %s" % (self.sctid, self.group) + "]"


class SctidGroups(RF2_Substrate_Common):
    _db = RelationshipDB()
    _andSTMT = "SELECT DISTINCT sg1.id, sg1.gid FROM (%s) AS sg1 JOIN" \
               " (%s) AS sg2 ON sg1.id = sg2.id AND sg1.gid = sg2.gid"
    _orSTMT = "SELECT DISTINCT sg.id, sg.gid FROM ((%s) UNION (%s)) as sg"
    _minusSTMT = "SELECT DISTINCT sg1.id, sg1.gid FROM (%s) AS sg1 LEFT JOIN " \
                 "(%s) AS sg2 ON sg1.id = sg2.id AND sg1.gid = sg2.gid WHERE sg2.id IS NULL"
    _data_type = SctidGroup

    def __init__(self, query=None, rf: bool=None):
        """
        Construct a set sctidGroups from a set of quads
        :param query: quad query
        :param rf: reverse flag if source_quads is not supplied
        :return:

        Note: This function assumes that the following table has been created:
               relationship_ss_ext as:
               create table relationship_ss_ext as
                    select *, IF(relationshipGroup > 0, relationshipGroup, id) as gid from relationship_ss
               and it should have indices on source, type, dest, source+type, dest+type
        """
        super().__init__()
        assert rf is not None, "Reverse flag must be supplied"
        self._len = None                # number of elements
        self._rf = rf
        sord = 'destinationId' if rf else 'sourceId'

        if query is not None:
            self._query = "SELECT DISTINCT r.id, gid"
            self._query += " FROM (%s) AS r" % query
        else:
            self._query = "SELECT DISTINCT r.%s AS id, gid" % sord
            self._query += " FROM %s AS r WHERE active=1 AND locked=0" % RelationshipDB.fname() + '_ext'

    def to_sctids(self):
        return Sctids(filtr=("id in (select sg.id from (%s) as sg) " % self.as_sql()))

    def __contains__(self, item: SctidGroup) -> bool:
        query = self._countSTMT % self.as_sql()
        query += " WHERE sg.id = %s AND sg.gid = %s" % (item.sctid, item.group)
        return int(list(self._execute_query(self._countSTMT % query))[0]) > 0

    def __and__(self, other):
        """ Return a Sctids instance that represents the intersection of self and other
        :param other: Sctids object to intersect with self
        :return: Sctids object that represents intersection
        """
        return SctidGroups(query=self._andSTMT % (self._query, other.as_sql()), rf=self._rf)

    def __or__(self, other):
        """ Return the union of the sctids in self and other
        :param other: a generator for a set of sctids
        :return: Generator for sctids
        """
        return SctidGroups(query=self._orSTMT % (self._query, other.as_sql()), rf=self._rf)

    def __sub__(self, other):
        return SctidGroups(query=self._minusSTMT % (self._query, other.as_sql()), rf=self._rf)

    # Convert SctidGroups to Sctids
    def i_required_group_cardinality(self, min_, max_, rf):
        src = 'destinationId' if rf else 'sourceId'
        sql = self.as_sql()

        if min_ <= 1 and not max_:
            query = "SELECT DISTINCT rc.%s AS id FROM  " % src
            query += "(%s) " % sql
        else:
            query = "SELECT DISTINCT rc.id FROM  "
            query += "(SELECT id, count(gid) as cnt FROM (%s) " % sql
            query += "AS ig GROUP BY ig.id) as rc WHERE "
            query += "rc.cnt >= %s" % (min_ if min_ > 1 else "1")
            query += " AND ig.cnt <= %s" % max_ if max_ and max_.inran('num') else ''
        return Sctids(query=query)

    # Convert SctidGroups to Sctids
    def i_optional_group_cardinality(self, ss, max_, rf):
        # Return all concepts that don't fail the cardinality test
        return Sctids() - (self.to_sctids() - self.i_required_group_cardinality(0, max_, rf))
