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
from ECLparser.rf2_substrate.RF2_Substrate_ConstraintOperators import descendants_of, ancestors_of
from ECLparser.rf2_substrate.RF2_Substrate_Quads import Quads
from ECLparser.z.z import Set, CrossProduct, Seq

from ECLparser.datatypes import Optional, concreteValue, stringValue, refset_concept, \
    reverseFlag, source_direction, targets_direction, Quads_or_Error, constraintOperator, descendantOf, \
    descendantOrSelfOf, ancestorOrSelfOf, Sctids_or_Error, sctId, numericComparisonOperator, stringComparisonOperator, \
    eco_eq, focusConcept, crOrWildCard, direction, Quad, numericValue, nco_eq, nco_neq, nco_gt, nco_ge, nco_lt, sco_eq
from ECLparser.test_substrate.substrate import Substrate
from ECLparser.interpreter.base_types import result_sctids, bigunion


def i_constraintOperator(ss: Substrate, oco: Optional(constraintOperator), input_: Sctids_or_Error) -> Sctids_or_Error:
    if input_.inran('error') or oco.is_empty:
        return input_
    input_ = input_.ok
    # TODO: Because we aren't doing equivalence, we can be sure (?) that the targets are always a singleton
    if oco.head == descendantOrSelfOf:
        rval = input_ | descendants_of(input_)
        # return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.descendants(id_) for id_ in
        #                                                               result_sctids(input_)]).union(result_sctids(input_)))
    elif oco.head == descendantOf:
        rval = descendants_of(input_)
        # return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), ss.descendants(result_sctids(input_))))
    elif oco.head == ancestorOrSelfOf:
        rval = input_ | ancestors_of(input_)
        # return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.ancestors(id_) for id_ in
        #                                                               result_sctids(input_)]).union(result_sctids(input_)))
    else:
        rval = ancestors_of(input_)
        # return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.ancestors(id_) for id_ in result_sctids(input_)]))
    return Sctids_or_Error(ok=rval)

# Completefun isn't used in this situation, as we leave it to the ancestors/descendants function to address this

i_attributeOperator = i_constraintOperator

# ec type is CrossProduct(expressionComparisonOperator, expressionConstraintValue
def i_expressionComparisonOperator(ss: Substrate, rf: Optional(reverseFlag), atts: Set(sctId),
                                   ec: CrossProduct()) -> Quads_or_Error:
    from ECLparser.interpreter import i_expressionConstraintValue
    ecv = i_expressionConstraintValue(ss, ec.second)
    if ecv.inran('error'):
        return Quads_or_Error(qerror=ecv.error)
    else:
        a = Quads(not rf.is_empty, atts, ec.first == eco_eq, ecv.ok)
        b = CrossProduct(Set(Quad), direction)(a, source_direction if not rf.is_empty else targets_direction)
        c = Quads_or_Error(quad_value=b)
        return c


#  type: ncv: CrossProduct(numericComparisonOperator, numericValue)
def i_numericComparsionOperator(ss: Substrate, rf: Optional(reverseFlag), atts: Set(sctId),
                                ncv: CrossProduct()) -> Quads_or_Error:
    if not rf.is_empty:
        v = []
        dir_ = targets_direction
    else:
        v = [q for q in ss.relationships if q.a in atts and q.t.inran('t_concrete') and
             numericComparison(q.t.t_concrete, ncv.first, ncv.second)]
        dir_ = source_direction
    return Quads_or_Error(v, dir_)


# return is the numericValue
# numericValue = FreeType(nv_decimal=decimalValue,
#                         nv_integer=N)
# nco_eq = numericComparisonOperator()
# nco_neq = numericComparisonOperator()
# nco_gt = numericComparisonOperator()
# nco_ge = numericComparisonOperator()
# nco_lt = numericComparisonOperator()
# nco_le = numericComparisonOperator()
def numericComparison(cv: concreteValue, nco: numericComparisonOperator, nv: numericValue):
    v1 = int(cv.cv_integer) if cv.inran('cv_integer') else \
         cv.cv_decimal if cv.inran('cv_decimal') else \
         int(cv.cv_string)
    v2 = nv.nv_decimal if nv.inran('decimalValue') else int(nv.nv_integer)
    return v1 == v2 if nco == nco_eq else \
           v1 != v2 if nco == nco_neq else \
           v1 > v2 if nco == nco_gt else \
           v1 >= v2 if nco == nco_ge else \
           v1 < v2 if nco == nco_lt else \
           v1 <= v2


def i_stringComparisonOperator(ss: Substrate, rf: Optional(reverseFlag), atts:  Set(sctId),
                               scv: CrossProduct(stringComparisonOperator, stringValue)) -> Quads_or_Error:
    return Quads_or_Error(quad_value=([], targets_direction)) if rf.is_empty else \
           Quads_or_Error(quad_value=([q for q in ss.relationships if q.a in atts and q.t.inran('t_concrete') and
                                       stringComparison(q.t.t_concrete, scv.first, scv.second)], source_direction))


def stringComparison(cv: concreteValue, sco: stringComparisonOperator, sv: stringValue) -> stringValue:
    v1 = str(cv.cv_integer) if cv.inran('cv_integer') else \
         str(cv.cv_decimal) if sv.inran('cv_decimal') else \
         str(cv.cv_string)
    v2 = str(sv)
    return v1 == v2 if sco == sco_eq else v1 != v1


def i_focusConcept(ss: Substrate, fc: focusConcept) -> Sctids_or_Error:
    return ss.i_conceptReference(fc.focusConcept_c.cr) if fc.inran('focusConcept_c') and fc.focusConcept_c.inran('cr') else \
           Sctids_or_Error(ok=ss.concepts) if fc.inran('focusConcept_c') and fc.focusConcept_c.inran('wc') else \
           i_memberOf(ss, fc.focusConcept_m)


def i_memberOf(ss: Substrate, crorwc: crOrWildCard) -> Sctids_or_Error:
    # TODO -- this function executes queries - need to redo ?
    refsetids = ss.i_conceptReference(crorwc.cr) if crorwc.inran('cr') else \
        Sctids_or_Error(ok=ss.descendants(refset_concept))
    if refsetids.inran('error'):
        return refsetids
    refsets = result_sctids(refsetids)
    refset_members = [ss.i_refsetId(sctid) for sctid in refsets]
    rval = refset_members[0] if refset_members else ss.equivalent_concepts(None)
    for m in refset_members[1:]:
        rval = rval.union(m)
    return Sctids_or_Error(ok=rval)
    # refsetids = ss.i_conceptReference(crorwc.cr) if crorwc.inran('cr') else \
    #     Sctids_or_Error(ok=ss.descendants(refset_concept))
    # return refsetids if refsetids.inran('error') else \
    #   bigunion(([ss.i_refsetId(sctid) for sctid in result_sctids(refsetids)]))

