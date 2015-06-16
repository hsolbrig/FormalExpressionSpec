# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
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

from ECLparser.z import N, Set

from ECLparser.interpreter.base_types import applyToSequence, intersect, union, Quads_or_Error, result_sctids, many, \
    unlimitedNat, quad_direction, sctId, quads_for, sctIdGroups_or_Error, evalCardinality, minus, gintersect, gunion, \
    zero_group, quadGroup

from ECLparser.datatypes import source_direction, Optional, cardinality, expressionConstraint, \
    unrefinedExpressionConstraint, refinedExpressionConstraint, simpleExpressionConstraint, \
    compoundExpressionConstraint, conjunctionExpressionConstraint, disjunctionExpressionConstraint, \
    exclusionExpressionConstraint, subExpressionConstraint, refinement, conjunctionRefinementSet, \
    disjunctionRefinementSet, subRefinement, attributeSet, conjunctionAttributeSet, disjunctionAttributeSet, \
    subAttributeSet, attribute, expressionConstraintValue, attributeGroup, sctIdGroup

from ECLparser.test_substrate.substrate import Substrate, Sctids_or_Error

from ECLparser.interpreter.substrate_interpretations import i_attributeOperator, i_numericComparsionOperator, \
    i_expressionComparisonOperator, i_stringComparisonOperator, i_focusConcept, i_constraintOperator


def i_expressionConstraint(ss: Substrate, ec: expressionConstraint) -> Sctids_or_Error:
    return i_refinedExpressionConstraint(ss, ec.expcons_refined) if ec.inran('expcons_refined') else \
        i_unrefinedExpressionConstraint(ss, ec.expcons_unrefined)


# 3.2.1 unrefinedExpressionConstraint
def i_unrefinedExpressionConstraint(ss: Substrate, uec: unrefinedExpressionConstraint) -> Sctids_or_Error:
    return i_compoundExpressionConstraint(ss, uec.unrefined_compund) if uec.inran('unrefined_compound') else \
        i_simpleExpressionConstraint(ss, uec.unrefined_simple)


# 3.2.2 refinedExpressionConstraint
def i_refinedExpressionConstraint(ss: Substrate, rec: refinedExpressionConstraint) -> Sctids_or_Error:
    unref_interp = i_unrefinedExpressionConstraint(ss, rec.first)
    return intersect(unref_interp, i_refinement(ss, rec.second))


# 3.2.3 simpleExpressionConstraint
def i_simpleExpressionConstraint(ss: Substrate, sec: simpleExpressionConstraint) -> Sctids_or_Error:
    return i_constraintOperator(ss, sec.first, i_focusConcept(ss, sec.second))


# 3.2.4 compoundExpressionConstraint
def i_compoundExpressionConstraint(ss: Substrate, cec: compoundExpressionConstraint) -> Sctids_or_Error:
    return i_conjunctionExpressionConstraint(ss, cec.compound_conj) if cec.inran('compound_conj') else \
           i_disjunctionExpressionConstraint(ss, cec.compound_disj) if cec.inran('compound_disj') else \
           i_exclusionExpressionConstraint(ss, cec.compound_excl) if cec.inran('compound_excl') else \
           i_compoundExpressionConstraint(ss, cec.compound_nested)


# 3.2.5 conjunctionExpressionConstraint
def i_conjunctionExpressionConstraint(ss: Substrate, cecr: conjunctionExpressionConstraint) -> Sctids_or_Error:
    return applyToSequence(ss, i_subExpressionConstraint, intersect, cecr)


# 3.2.6 disjunctionExpressionConstraint
def i_disjunctionExpressionConstraint(ss: Substrate, decr: disjunctionExpressionConstraint) -> Sctids_or_Error:
    return applyToSequence(ss, i_subExpressionConstraint, union, decr)


# 3.2.7 exclusionExpressionConstraint
def i_exclusionExpressionConstraint(ss: Substrate, ecr: exclusionExpressionConstraint) -> Sctids_or_Error:
    first_sec = i_subExpressionConstraint(ss, ecr.first)
    second_sec = i_subExpressionConstraint(ss, ecr.second)
    return first_sec.minus(second_sec)


# 3.2.8 subExpressionConstraint
def i_subExpressionConstraint(ss: Substrate, sec: subExpressionConstraint) -> Sctids_or_Error:
    return i_simpleExpressionConstraint(ss, sec.subExpr_simple) if sec.inran('subExpr_simple') else \
           i_compoundExpressionConstraint(ss, sec.subExpr_compound) if sec.inran('subExpr_compound') else \
           i_refinedExpressionConstraint(ss, sec.subExpr_refined)


# 3.3 refinement
def i_refinement(ss: Substrate, rfnment: refinement) -> Sctids_or_Error:
    lhs = i_subRefinement(ss, rfnment.first)
    rhs = rfnment.second
    return lhs if rhs.is_empty else \
           intersect(lhs, i_conjunctionRefinementSet(ss, rhs.head.refine_conjset)) if rhs.head.inran('refine_conjset') else \
           union(lhs, i_disjunctionRefinementSet(ss, rhs.head.refine_disjset))


# 3.3.1 conjunctionRefinementSet
def i_conjunctionRefinementSet(ss: Substrate, conjset: conjunctionRefinementSet) -> Sctids_or_Error:
    return i_subRefinement(ss, conjset.head) if conjset.tail.is_empty else \
           intersect(i_subRefinement(ss, conjset.head), i_conjunctionRefinementSet(ss, conjset.tail))


# 3.3.1 conjunctionRefinementSet
def i_disjunctionRefinementSet(ss: Substrate, disjset: disjunctionRefinementSet) -> Sctids_or_Error:
    return i_subRefinement(ss, disjset.head) if disjset.tail.is_empty else \
           union(i_subRefinement(ss, disjset.head), i_conjunctionRefinementSet(ss, disjset.tail))


# 3.3.3 subRefinement
def i_subRefinement(ss: Substrate, subrefine: subRefinement) -> Sctids_or_Error:
    return i_attributeSet(ss, subrefine.subrefine_attset) if subrefine.inran('subrefine_attset') else \
           i_attributeGroup(ss, subrefine.subrefine_attgroup) if subrefine.inran('subrefine_attgroup') else \
           i_refinement(ss, subrefine.subrefine_refinement)


# 3.4 attributeSet
def i_attributeSet(ss: Substrate, attset: attributeSet) -> Sctids_or_Error:
    lhs = i_subAttributeSet(ss, attset.first)
    rhs = attset.second
    return lhs if rhs.is_empty or lhs.inran('error') else \
           intersect(lhs, i_conjunctionAttributeSet(ss, rhs.head.attset_conjattset)) \
               if rhs.head.inran('attset_conjattset') else \
           union(lhs, i_disjunctionAttributeSet(ss, rhs.head.attset.disjattset))


# 3.4.1 conjunctionAttributeSet
def i_conjunctionAttributeSet(ss: Substrate, conjset: conjunctionAttributeSet) -> Sctids_or_Error:
    return i_subAttributeSet(ss, conjset.head) if conjset.tail.is_empty else \
           intersect(i_subAttributeSet(ss, conjset.head), i_conjunctionAttributeSet(ss, conjset.tail))


# 3.4.2 disjuncstionAttributeSet
def i_disjunctionAttributeSet(ss: Substrate, disjset: disjunctionAttributeSet) -> Sctids_or_Error:
    return i_subAttributeSet(ss, disjset.head) if disjset.tail.is_empty else \
           union(i_subAttributeSet(ss, disjset.head), i_disjunctionAttributeSet(ss, disjset.tail))


# 3.4.3 subAttributeSet
def i_subAttributeSet(ss: Substrate, subaset: subAttributeSet) -> Sctids_or_Error:
    return i_attribute(ss, subaset.subaset_attribute) if subaset.inran('subaset_attribute') else \
           i_attributeSet(ss, subaset.subast_attset)


# 3.5 attribute
def i_attribute(ss: Substrate, att: attribute) -> Sctids_or_Error:
    att_sctids = i_attributeOperator(ss, att.attrOper, ss.i_attributeName(att.name))
    return att_sctids if att_sctids.inran('error') else \
        i_att_cardinality(ss, att.card, i_expressionComparisonOperator(ss,
                                                                       att.rf,
                                                                       result_sctids(att_sctids),
                                                                       att.opValue.attrib_expr)) if \
            att.opValue.inran('attrib_expr') else \
        i_att_cardinality(ss, att.card, i_numericComparsionOperator(ss,
                                                                    att.rf,
                                                                    result_sctids(att_sctids),
                                                                    att.opValue.attrib_num)) if \
            att.opValue.inran('attrib_num') else \
        i_att_cardinality(ss, att.card, i_stringComparisonOperator(ss,
                                                                   att.rf,
                                                                   result_sctids(att_sctids),
                                                                   att.opValue.attrib_str))


# 3.5.1 attribue cardinality
def i_att_cardinality(ss: Substrate, ocard: Optional(cardinality), qore: Quads_or_Error) -> Sctids_or_Error:
    if qore.inran('qerror'):
        rval = Sctids_or_Error(error = qore.qerror)
    elif ocard.is_empty:
        rval = Sctids_or_Error(ok = i_required_cardinality(N(1), many, qore))
    else:
        card = ocard.head
        rval = Sctids_or_Error(ok = i_required_cardinality(card.min, card.max, qore) if card.min > 0 else \
            i_optional_cardinality(ss, card.max, qore))
    return rval


def i_required_cardinality(min_: N, max_: unlimitedNat, qore: Quads_or_Error) -> Set(sctId):
    if quad_direction(qore) == source_direction:
        return Set(sctId)([q.s for q in quads_for(qore).v if
                           evalCardinality(min_, max_, [q2 for q2 in quads_for(qore).v if q2.s == q.s])])
    else:
        return Set(sctId)([q.t.t_sctid for q in quads_for(qore) if q.t.inran('t_sctid') and
                          evalCardinality(min_, max_, [q2 for q2 in quads_for(qore).v if q2.t.t_sctid == q.t.t_sctid])])


def i_optional_cardinality(ss: Substrate, max_: unlimitedNat, qore: Quads_or_Error) -> Set(sctId):
    if quad_direction(qore) == source_direction:
        minus(ss.concepts, minus(Set(sctId)([q.s for q in quads_for(qore).v]), i_required_cardinality(N(0), max_, qore)))
    else:
        minus(ss.concepts, minus(Set(sctId)([q.t.t_sctid for q in quads_for(qore).v
                                             if q.t.inran('t_sctid')]), i_required_cardinality(N(0), max_, qore)))


# 3.5.2 espressionConstraintValue
def i_expressionConstraintValue(ss: Substrate, ecv: expressionConstraintValue) -> Sctids_or_Error:
    return i_simpleExpressionConstraint(ss, ecv.expression_simple) if ecv.inran('expression_simple') else \
           i_refinedExpressionConstraint(ss, ecv.expression_refined) if ecv.inran('expression_refined') else \
           i_compoundExpressionConstraint(ss, ecv.expression_compound)


# 3.6 attributeGroup
def i_attributeGroup(ss: Substrate, ag: attributeGroup) -> Sctids_or_Error:
    return i_group_cardinality(ss, ag.first, i_groupAttributeSet(ss, ag.second))


# 3.6.1 attribute group cardinality
def i_group_cardinality(ss: Substrate, ocard: Optional(cardinality), idg: sctIdGroups_or_Error) -> Sctids_or_Error:
    return Sctids_or_Error(error=idg.gerror) if idg.inran('gerror') else \
           Sctids_or_Error(ok=i_required_group_cardinality(N(1), many, idg.group_value)) if ocard.is_empty else \
           Sctids_or_Error(ok=i_required_group_cardinality(ocard.head.min, ocard.head.max,
                                                            idg.group_value)) if ocard.head.min > 0 else \
           Sctids_or_Error(ok=i_optional_group_cardinality(ss, ocard.head.max, idg.group_value))


def i_required_group_cardinality(min_: N, max_: unlimitedNat, groups: Set(sctIdGroup)) -> Set(sctId):
    return Set(sctId)(
        [s.first for s in groups.v if evalCardinality(min_, max_, [g for g in groups.v if g.first == s.first])])


def i_optional_group_cardinality(ss: Substrate, max_: unlimitedNat, groups: Set(sctId)) -> Set(sctId):
    return Set(sctId)(
        minus(ss.concepts, minus(Set(sctId)([s.first for s in groups]),
                                 i_required_group_cardinality(N(0), max_, groups))))


# 3.6.2 attributeSet inside a group
def i_groupAttributeSet(ss: Substrate, attset: attributeSet) -> sctIdGroups_or_Error:
    lhs = i_groupSubAttributeSet(ss, attset.first)
    rhs = attset.second
    return lhs if rhs.is_empty else \
        gintersect(lhs, i_groupConjunctionAttributeSet(ss, rhs.head.attset_conjattset)) if rhs.head.inran(
            'attset_conjattset') else \
        gunion(lhs, i_groupDisjunctionAttributeSet(ss, rhs.head.attset_disjattset))


# 3.6.3 conjunctionAttributeSet inside a group
def i_groupConjunctionAttributeSet(ss: Substrate, conjset: conjunctionAttributeSet) -> sctIdGroups_or_Error:
    return i_groupSubAttributeSet(ss, conjset.head) if conjset.tail.is_empty else \
        gintersect(i_groupSubAttributeSet(ss, conjset.head), i_groupConjunctionAttributeSet(ss, conjset.tail))


# 3.6.4 disjunctionAttributeSet inside a group
def i_groupDisjunctionAttributeSet(ss: Substrate, disjset: disjunctionAttributeSet) -> sctIdGroups_or_Error:
    return i_groupSubAttributeSet(ss, disjset.head) if disjset.tail.is_empty else \
        gunion(i_groupSubAttributeSet(ss, disjset.head), i_groupConjunctionAttributeSet(ss, disjset.tail))


# 3.6.5 subAttributeSet inside a group
def i_groupSubAttributeSet(ss: Substrate, subaset: subAttributeSet) -> sctIdGroups_or_Error:
    return i_groupAttribute(ss, subaset.subaset_attribute) if subaset.inran('subaset_attribute') else \
        i_groupAttributeSet(ss, subaset.subaset_attset)


# 3.6.6 attribute inside a group
def i_groupAttribute(ss: Substrate, att: attribute) -> sctIdGroups_or_Error:
    att_sctids = i_attributeOperator(ss, att.attrOper, ss.i_attributeName(att.name))
    if att_sctids.inran('error'):
        return sctIdGroups_or_Error(gerror=att_sctids.error)
    elif att.opValue.inran('attrib_expr'):
        expr_interp = i_expressionComparisonOperator(ss, att.rf, result_sctids(att_sctids), att.opValue.attrib_expr)
        return i_att_group_cardinality(ss, att.card, expr_interp)
    elif att.opValue.inran('attrib_num'):
        num_interp = i_numericComparsionOperator(ss, att.rf, result_sctids(att_sctids), att.opValue.attrib_num)
        return i_att_group_cardinality(ss, att.card, num_interp)
    else:
        str_interp = i_stringComparisonOperator(ss, att.rf, result_sctids(att_sctids), att.opValue.attrib_str)
        return i_att_group_cardinality(ss, att.card, str_interp)


# 3.6.7 cardinality inside a group
def i_att_group_cardinality(ss: Substrate, ocard: Optional(cardinality), qore: Quads_or_Error) -> sctIdGroups_or_Error:
    return sctIdGroups_or_Error(gerror=qore.qerror) if qore.inran('qerror') else \
           sctIdGroups_or_Error(group_value=i_required_att_group_cardinality(N(1), many, qore)) if ocard.is_empty else \
           sctIdGroups_or_Error(group_value=i_required_att_group_cardinality(ocard.head.min, ocard.head.max,
                                                                              qore)) if ocard.head.min > 0 else \
           sctIdGroups_or_Error(group_value=i_optional_att_group_cardinality(ss, ocard.head.max, qore))


def i_required_att_group_cardinality(min_: N, max_: unlimitedNat, qore: Quads_or_Error) -> Set(sctIdGroup):
    if quad_direction(qore) == source_direction:
        nzg = set([q for q in quads_for(qore).v if q.g != zero_group])
        zg = set([q for q in quads_for(qore).v if q.g == zero_group])
        nzg_pass = [q_nz for q_nz in nzg
                    if evalCardinality(min_, max_, [q for q in quads_for(qore).v if q.s == q_nz.s and q.g == q_nz.g])]
        zg_pass = [q_zg for q_zg in zg if evalCardinality(min_, max_, set(q_zg))]
        return Set(sctIdGroup)([sctIdGroup(q.s, quadGroup(q)) for q in (nzg_pass + zg_pass)])
    else:
        nzg = set([q for q in quads_for(qore).v if q.g != zero_group and q.t.inran('t_sctid')])
        zg = set([(q.t, q) for q in quads_for(qore).v if q.g == zero_group and q.t.inran('t_sctid')])
        nzg_pass = [q_nz for q_nz in nzg
                    if evalCardinality(min_, max_, [q for q in quads_for(qore).v if q.t == q_nz.t and q.g == q_nz.g])]
        zg_pass = [q_zg for q_zg in zg if evalCardinality(min_, max_, set(q_zg))]
        return Set(sctIdGroup(nzg_pass + zg_pass))


def i_optional_att_group_cardinality(ss: Substrate, max_: unlimitedNat, qore: Quads_or_Error) -> Set(sctIdGroup):
    if quad_direction(qore) == source_direction:
        return Set(sctIdGroup)(minus([sctIdGroup(rel.s, quadGroup(rel)) for rel in ss.relationships],
                                     union([sctIdGroup(q.s, quadGroup(q)) for q in quads_for(qore).v],
                                           i_required_att_group_cardinality(N(0), max_, qore))))
    else:
        return Set(sctIdGroup)(
            minus([sctIdGroup(rel.t.t_sctid, quadGroup(rel)) for rel in ss.relationships if rel.t.inran('t_sctid')],
                  union([sctIdGroup(q.t.t_sctid, quadGroup(q)) for q in quads_for(qore).v],
                        i_required_att_group_cardinality(N(0), max_, qore))))
