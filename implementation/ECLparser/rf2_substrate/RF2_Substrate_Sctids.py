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
from ECLparser.rf2_substrate.RF2_Substrate_Common import RF2_Substrate_Common, _v

from rf2db.db.RF2ConceptFile import ConceptDB
from ECLparser.datatypes import sctId

from ECLparser.z.z import Set, _Instance


class Set_Sctids(Set):
    def __init__(self):
        Set.__init__(self, Sctids)
        self._type = sctId

    def has_member(self, other):
        return isinstance(other, Sctids)


def _iter_typ(_, dbrec):
    return sctId(dbrec[0])  # Shim to pull the only column out of the record

class Sctids(RF2_Substrate_Common, _Instance, Set):
    _db = ConceptDB()
    _andSTMT = "SELECT DISTINCT and_sctid1.id FROM (%s) AS and_sctid1 JOIN (%s) AS and_sctid2 " \
               "ON and_sctid1.id = and_sctid2.id"
    _orSTMT = "SELECT DISTINCT or_sctid.id FROM ((%s) UNION (%s)) AS or_sctid"
    _minusSTMT = "SELECT DISTINCT minus_sctid.id FROM (%s) AS minus_sctid WHERE minus_sctid.id NOT IN (%s)"
    _data_type = _iter_typ

    def __init__(self, filtr=None, query=None):
        """
        Construct a virtual sctid set
        :param filtr: One of a textual SQL filter, a generator for SCTID's or None (wild card)
        :param query: A complete query -- result of and, or or minus
        """
        Set.__init__(self, Sctids)
        _Instance.__init__(self, Sctids)
        RF2_Substrate_Common.__init__(self)
        self._val = self
        self._type = sctId

        if query is not None:
            self._query = query
        else:
            if filtr is not None and not isinstance(filtr, str):
                sctid_list = filtr if isinstance(filtr, Container) else [filtr]
                if sctid_list:
                    filtr = 'id IN (' + ','.join(str(e) for e in sctid_list) + ')'
                else:
                    filtr = ' False '
            self._query = self._db.buildQuery(**self._build_parms(filtr))

    @staticmethod
    def _build_parms(filtr):
        """ Build the parameters to pass to the RF2ConceptFile buildQuery
        :return:
        """
        return _v(maxtoreturn=-1, sort='none', id_only=True, filtr=filtr)

    def __contains__(self, item) -> bool:
        item_c = Sctids(item)
        return len(self & item_c) == (len(item) if isinstance(item, Sized) else 1)

