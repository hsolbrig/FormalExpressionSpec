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
from ECLparser.rf2_substrate.RF2_Substrate_Quads import Quads
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

    def __init__(self, source_quads: Quads):
        """
        Construct a set sctidGroups from a set of quads
        :param source_quads: generator for quads
        :return:
        """
        super().__init__()
        self._len = None                # number of elements
        self._query = "SELECT DISTINCT r.%s AS id, IF(r.relationshipGroup > 0, r.relationshipGroup, r.id) AS gid" \
                      " FROM (%s) as r" % ('sourceId' if source_quads.rf else 'destinationId', source_quads.as_sql())

    def to_sctids(self):
        return Sctids(filtr=("id in (select sg.id from (%s) as sg) " % self.as_sql()))

    def __contains__(self, item: SctidGroup) -> bool:
        query = self._countSTMT % self.as_sql()
        query += " WHERE sg.id = %s AND sg.gid = %s" % (item.sctid, item.group)
        return int(list(self._execute_query(self._countSTMT % query))[0]) > 0

