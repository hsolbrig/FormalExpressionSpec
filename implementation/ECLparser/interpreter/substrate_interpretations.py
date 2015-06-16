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
from ECLparser.z.z import Set, CrossProduct, Seq

from ECLparser.datatypes import Optional, concreteValue, stringValue, refset_concept, \
    reverseFlag, source_direction, targets_direction, Quads_or_Error, constraintOperator, descendantOf, \
    descendantOrSelfOf, ancestorOrSelfOf, Sctids_or_Error, sctId, numericComparisonOperator, stringComparisonOperator, \
    eco_eq, eco_neq, focusConcept, crOrWildCard, Quad, direction
from ECLparser.test_substrate.substrate import Substrate
from ECLparser.interpreter.base_types import result_sctids, bigunion


def i_constraintOperator(ss: Substrate, oco: Optional(constraintOperator), input_: Sctids_or_Error) -> Sctids_or_Error:
    if input_.inran('error') or oco.is_empty:
        return input_
    if oco.head == descendantOrSelfOf:
        return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.descendants(id_) for id_ in result_sctids(input_)]).\
            union(result_sctids(input_)))
    elif oco.head == descendantOf:
        return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.descendants(id_) for id_ in result_sctids(input_)]))
    elif oco.head == ancestorOrSelfOf:
        return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.ancestors(id_) for id_ in result_sctids(input_)]).\
            union(result_sctids(input_)))
    else:
        return Sctids_or_Error(ok=Set.SetInstance.bigcup(Set(sctId), [ss.ancestors(id_) for id_ in result_sctids(input_)]))

# Completefun isn't used in this situation, as we leave it to the ancestors/descendants function to address this

i_attributeOperator = i_constraintOperator

# ec type is CrossProduct(expressionComparisonOperator, expressionConstraintValue
def i_expressionComparisonOperator(ss: Substrate, rf: Optional(reverseFlag), atts: Set(sctId),
                                   ec: CrossProduct()) -> Quads_or_Error:
    from ECLparser.interpreter import i_expressionConstraintValue
    ecv = i_expressionConstraintValue(ss, ec.second)
    return Quads_or_Error(qerror=ecv.error) if ecv.inran('error') else \
           Quads_or_Error(quad_value=CrossProduct(Seq(Quad), direction)(Seq(Quad)([q for q in ss.relationships.v if q.a in atts and q.t.inran('t_sctid') and
                                       q.t.t_sctid in result_sctids(ecv).v]), source_direction)) \
               if rf.is_empty and ec.first == eco_eq else \
           Quads_or_Error(quad_value=CrossProduct(Seq(Quad), direction)(Seq(Quad)([q for q in ss.relationships.v if q.a in atts.v and q.s in result_sctids(ecv).v]),
                                      targets_direction)) if rf.card > 0 and ec.first == eco_eq else \
           Quads_or_Error(quad_value=CrossProduct(Seq(Quad), direction)(Seq(Quad)([q for q in ss.relationships.v if q.a in atts and q.t.inran('t_sctid')
                                       and q.t.t_sctid not in result_sctids(ecv).v]), source_direction)) \
               if rf.is_empty and ec.first == eco_neq else \
           Quads_or_Error(quad_value=CrossProduct(Seq(Quad), direction)(Seq(Quad)([q for q in ss.relationships.v
                                       if q.a in atts and q.s not in result_sctids(ecv).v]), targets_direction))



#  type: ncv: CrossProduct(numericComparisonOperator, numericValue)
def i_numericComparsionOperator(ss: Substrate, rf:Optional(reverseFlag), atts: Set(sctId),
                                ncv: CrossProduct()) -> Quads_or_Error:
    return Quads_or_Error(quad_value=([], targets_direction)) if rf.is_empty else \
           Quads_or_Error(quad_value=([q for q in ss.relationships if q.a in atts and q.t.inran('t_concrete') and
                                       numericComparison(q.t.t_concrete, ncv.first) == ncv.second], source_direction))


# return is the numericValue
def numericComparison(cv: concreteValue, nco: numericComparisonOperator):
    return int(cv.cv_integer) if cv.inran('cv_integer') else cv.cv_decimal if cv.inran('cv_decimal') else int(cv.cv_string)



def i_stringComparisonOperator(ss: Substrate, rf: Optional(reverseFlag), atts:  Set(sctId),
                               scv: CrossProduct(stringComparisonOperator, stringValue)) -> Quads_or_Error:
    return Quads_or_Error(quad_value=([], targets_direction)) if rf.is_empty else \
           Quads_or_Error(quad_value=([q for q in ss.relationships if q.a in atts and q.t.inran('t_concrete') and
                                       stringComparison(q.t.t_concrete, scv.first) == scv.second], source_direction))

def stringComparison(cv: concreteValue, sco: stringComparisonOperator) -> stringValue:
    return str(cv.cv_integer) if cv.cv_integer('cv_integer') else str(cv.cv_decimal) if cv.inran('cv_decimal') else str(cv.cv_string)


def i_focusConcept(ss: Substrate, fc: focusConcept) -> Sctids_or_Error:
    return ss.i_conceptReference(fc.focusConcept_c.cr) if fc.inran('focusConcept_c') and fc.focusConcept_c.inran('cr') else \
           Sctids_or_Error(ok=ss.concepts) if fc.inran('focusConcept_c') and fc.focusConcept_c.inran('wc') else \
           i_memberOf(ss, fc.focusConcept_m)


def i_memberOf(ss: Substrate, crorwc: crOrWildCard) -> Sctids_or_Error:
    refsetids = ss.i_conceptReference(crorwc.cr) if crorwc.inran('cr') else \
                Sctids_or_Error(ok=ss.descendants(refset_concept))
    return refsetids if refsetids.inran('error') else \
           bigunion(([ss.i_refsetId(sctid) for sctid in result_sctids(refsetids)]))