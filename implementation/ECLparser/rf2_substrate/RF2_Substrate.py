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
import os

from ECLparser.datatypes import sctId, Sctids_or_Error, conceptReference, unknownConceptReference, attributeName,\
    attribute_concept, unknownAttributeId, refset_concept, unknownRefsetId
from ECLparser.rf2_substrate import RF2_Substrate_Sctids, RF2_Substrate_Quads, RF2_Substrate_ConstraintOperators,\
    RF2_Substrate_SctidGroups
from rf2db.db.RF2FileCommon import rf2_values
from ECLparser.interpreter.substrate import Substrate

# If True, missing concepts are ignored.  If false, they are validated
permissive = True

class RF2_Substrate(Substrate):
    def __init__(self, configfile=None):
        if not configfile:
            _curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
            configfile = os.path.join(_curdir, 'settings.conf')
        rf2_values.set_configfile(configfile)
        self._concepts = RF2_Substrate_Sctids.Sctids()
        self._relationships = RF2_Substrate_Quads.Quads()

    @property
    def concepts(self) -> RF2_Substrate_Sctids.Sctids:
        return self._concepts

    @property
    def relationships(self) -> RF2_Substrate_Quads.Quads:
        return self._relationships

    def equivalent_concepts(self, s: sctId) -> RF2_Substrate_Sctids.Sctids:
        """
        :param s:
        :return:
        """
        return RF2_Substrate_Sctids.Sctids(s if permissive else RF2_Substrate_Sctids.Sctids(s))

    def refsets(self, _: sctId) -> RF2_Substrate_Sctids.Sctids:
        return []

    def descendants(self, s: sctId) -> RF2_Substrate_Sctids.Sctids:
        return RF2_Substrate_ConstraintOperators.descendants(RF2_Substrate_Sctids.Sctids(s))

    def ancestors(self, s: sctId) -> RF2_Substrate_Sctids.Sctids:
        return RF2_Substrate_ConstraintOperators.ancestors(RF2_Substrate_Sctids.Sctids(s))

    def i_conceptReference(self, cr: conceptReference) -> Sctids_or_Error:
        return Sctids_or_Error(ok=self.equivalent_concepts(cr.first)) if permissive or cr.first in self._concepts else \
               Sctids_or_Error(error=unknownConceptReference)

    def i_attributeName(self, an: attributeName) -> Sctids_or_Error:
        return Sctids_or_Error(ok=self.equivalent_concepts(an.ancr.first)) \
            if permissive or an.ancr.first in self.descendants(attribute_concept) else Sctids_or_Error(error=unknownAttributeId)

    def i_refsetId(self, rsid: conceptReference) -> Sctids_or_Error:
        return Sctids_or_Error(ok=self.equivalent_concepts(rsid.first)) \
            if permissive or rsid.first in self.descendants(refset_concept) else Sctids_or_Error(error=unknownRefsetId)
