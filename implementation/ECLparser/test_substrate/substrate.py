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

from ECLparser.z.z import Set
from ECLparser.datatypes import attribute_concept, refset_concept, sctId, conceptReference, Quad, attributeName, \
    Sctids_or_Error, unknownConceptReference, unknownAttributeId, unknownRefsetId
from ECLparser.interpreter.substrate import Substrate as ss


class Substrate(ss):
    def __init__(self, concepts=None, relationships=None, parentsOf=None, equivalent_concepts=None, refsets=None):
        """
        Initialize a substrate
        :param concepts: a list of SCTID's
        :param relationships: a list of Quad's
        :param parentsOf: a dictionary of sctId to a set of sctIds
        :param equivalent_concepts: a dictionary of sctId to a set of sctIds
        :param refsets: a dictionary of sctId to a set of sctIds
        :return:
        """
        self._concepts = concepts
        self._relationships = relationships
        self._parentsOf = {} if parentsOf is None else parentsOf
        self._equivalent_concepts = {} if equivalent_concepts is None else equivalent_concepts
        self._refsets = {} if refsets is None else refsets
        self._childrenOf = {}
        for k, vs in self._parentsOf.items():
            for v in vs:
                self._childrenOf.setdefault(v, set()).add(k)

    @property
    def concepts(self) -> Set(sctId):
        return Set(sctId)(self._concepts)

    @property
    def relationships(self) -> Set(Quad):
        return Set(Quad)(self._relationships)

    def equivalent_concepts(self, s: sctId) -> Set(sctId):
        return Set(sctId)(self._equivalent_concepts.get(s, set()).union({s}))

    def refsets(self, s: sctId) -> Set(sctId):
        return Set(sctId)(self._refsets.get(s, []))

    def _descendants(self, s: sctId) -> set:
        return self._childrenOf.get(s, set()).union(*[self._descendants(c) for c in self._childrenOf.get(s, set())])

    def descendants(self, s: sctId) -> Set(sctId):
        return Set(sctId)(self._descendants(s))

    def _ancestors(self, s: sctId) -> set:
        return self._parentsOf.get(s, set()).union(*[self._ancestors(c) for c in self._parentsOf.get(s, set())])

    def ancestors(self, s: sctId) -> Set(sctId):
        return Set(sctId)(self._ancestors(s))

    def i_conceptReference(self, cr: conceptReference) -> Sctids_or_Error:
        return Sctids_or_Error(ok=self.equivalents(cr.first)) if cr.first in self._concepts else \
               Sctids_or_Error(error=unknownConceptReference)

    def i_attributeName(self, an: attributeName) -> Sctids_or_Error:
        return Sctids_or_Error(ok=self.equivalents(an.ancr.first)) \
            if an.ancr.first in self._descendants(attribute_concept) else \
               Sctids_or_Error(error=unknownAttributeId)

    def i_refsetId(self, rsid: conceptReference) -> Sctids_or_Error:
        print("HERE")
        return Sctids_or_Error(ok=self.equivalents(rsid.first)) \
             if rsid.first in self._descendants(refset_concept) else \
                Sctids_or_Error(error=unknownRefsetId)
