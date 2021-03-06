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
import re
from ECLparser.rf2_substrate.RF2_Substrate_Sctids import Sctids

_transitive_query = "SELECT DISTINCT tt1.%s AS id FROM transitive_ss AS tt1 JOIN (%s) AS tt2" \
                    " ON tt1.%s = tt2.id WHERE tt1.locked = 0"
_self_query = "SELECT t_u.id FROM ((%s) UNION (%s)) AS t_u"

def fmt(txt):
    return re.sub(r'\s+', ' ', str(txt))[:20]


def descendants_of(query: Sctids) -> Sctids:
    return Sctids(query=_transitive_query % ('child', query.as_sql(), 'parent'))


def descendantsOrSelf_of(query: Sctids) -> Sctids:
    return Sctids(query=_self_query % (_transitive_query % ('child', query.as_sql(), 'parent'), query.as_sql()))


def ancestors_of(query: Sctids) -> Sctids:
    return Sctids(query=_transitive_query % ('parent', query.as_sql(), 'child'))


def ancestorsOrSelf_of(query: Sctids) -> Sctids:
    return Sctids(query=_self_query % (_transitive_query % ('parent', query.as_sql(), 'child'), query.as_sql()))
