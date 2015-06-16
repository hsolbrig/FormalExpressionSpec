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
from ECLparser.z.z import FreeType, Seq, Schema, CrossProduct, BasicType, Set, Forward, N, Seq_1

from ECLparser.sctid import sctid

# 1 Data Types
# 1.1 Atomic Data Types
sctId = sctid.SCTID
term = str
decimalValue = float
stringValue = str
groupId = int

is_a = sctId(116680003)  # Is a (attribute)
zero_group = groupId(0)  # Zero group identifier
attribute_concept = sctId(106237007)  # Linkage concept (linkage concept)
refset_concept = sctId(900000000000455006)  # Reference set (foundation metadata concept)

# 1.2 Composite Data Types
concreteValue = FreeType(cv_string=stringValue, cv_integer=int, cv_decimal=decimalValue)
target = FreeType(t_sctid=sctId, t_concrete=concreteValue)


# A Optional elements
class Optional(Seq):
    maxlen = 1


# 2.1.1 Quad
Quad = Schema(lambda q: q.a != is_a or (q.g == 0 and q.t.inran('t_sctid')),
              s=sctId, a=sctId, t=target, g=groupId)


# 2.1.2 ConceptReference
conceptId = sctId
conceptReference = CrossProduct(conceptId, Optional(term))
attributeName = FreeType(ancr=conceptReference, anwc=None)

# 4.6 focusConcept
crOrWildCard = FreeType(cr=conceptReference, wc=None)
focusConcept = FreeType(focusConcept_m=crOrWildCard, focusConcept_c=crOrWildCard)


# 3.1 Interpretation Output
class ERROR(BasicType): pass
unknownConceptReference = ERROR()
unknownAttributeId = ERROR()
unknownRefsetId = ERROR()

Sctids_or_Error = FreeType(ok=Set(sctId), error=ERROR)

# 3.5.2 expressionConstraintValue
simpleExpressionConstraint = Forward()
refinedExpressionConstraint = Forward()
compoundExpressionConstraint = Forward()
expressionConstraintValue = FreeType(expression_simple=simpleExpressionConstraint,
                                       expression_refined=refinedExpressionConstraint,
                                       expression_compound=compoundExpressionConstraint)

numericValue = FreeType(nv_decimal=decimalValue,
                          nv_integer=N)


# 4.3 expressionComparisonOperator
class expressionComparisonOperator(BasicType): pass
eco_eq = expressionComparisonOperator()
eco_neq = expressionComparisonOperator()


# 4.4 numericComparisonOperator
class numericComparisonOperator(BasicType): pass
nco_eq = numericComparisonOperator()
nco_neq = numericComparisonOperator()
nco_gt = numericComparisonOperator()
nco_ge = numericComparisonOperator()
nco_lt = numericComparisonOperator()
nco_le = numericComparisonOperator()


# 4.5 stringComparisonOperator
class stringComparisonOperator(BasicType): pass
sco_eq = stringComparisonOperator()
sco_neq = stringComparisonOperator()

attributeOperatorValue = FreeType(attrib_expr=CrossProduct(expressionComparisonOperator,
                                                               expressionConstraintValue),
                                    attrib_num=CrossProduct(numericComparisonOperator,
                                                              numericValue),
                                    attrib_str=CrossProduct(stringComparisonOperator,
                                                              stringValue))


# 3.5.1 attribue cardinality
unlimitedNat = FreeType(num=N, many=None)
many = unlimitedNat(many=None)
cardinality = Schema(min_=N, max_=unlimitedNat)


class reverseFlags(BasicType): pass
# TODO: Think about this
reverseFlag = reverseFlags()


class constraintOperator(BasicType): pass
descendantOrSelfOf = constraintOperator()
descendantOf = constraintOperator()
ancestorOrSelfOf = constraintOperator()
ancestorOf = constraintOperator()

attributeOperator = constraintOperator


# 3.5 attribute
attribute = Schema(card=Optional(cardinality), rf=Optional(reverseFlags),
                     attrOper=Optional(constraintOperator), name=attributeName, opValue=attributeOperatorValue)

# 3.4.3 subAttributeSet
attributeSet = Forward()
subAttributeSet = FreeType(subaset_attribute=attribute,
                             subaset_attset=attributeSet)

# 3.4.2 disjuncstionAttributeSet
disjunctionAttributeSet = Seq_1(subAttributeSet)

# 3.4.1 conjunctionAttributeSet
conjunctionAttributeSet = Seq_1(subAttributeSet)

# 3.4 attributeSet
conjunctionOrDisjunctionAttributeSet = FreeType(attset_conjattset=conjunctionAttributeSet,
                                                  attset_disjattset=disjunctionAttributeSet)
attributeSet << CrossProduct(subAttributeSet,
                               Optional(conjunctionOrDisjunctionAttributeSet))


# 3.6 attributeGroup
attributeGroup = CrossProduct(Optional(cardinality), attributeSet)

# 3.3.3 subRefinement
refinement = Forward()
subRefinement = FreeType(subrefine_attset=attributeSet,
                           subrefine_attgroup=attributeGroup,
                           subrefine_refinement=refinement)


# 3.3.1 conjunctionRefinementSet
conjunctionRefinementSet = Seq_1(subRefinement)

# 3.3.2 disjunctionRefinementSet
disjunctionRefinementSet = Seq_1(subRefinement)

# 3.3 refinement
refinementConjunctionOrDisjunction = FreeType(refine_conjset=conjunctionRefinementSet,
                                                refine_disjset=disjunctionRefinementSet)
refinement << CrossProduct(subRefinement, Optional(refinementConjunctionOrDisjunction))

# 3.2.8 subExpressionConstraint
subExpressionConstraint = Forward()
subExpressionConstraint << FreeType(subExpr_simple=simpleExpressionConstraint,
                                      subExpr_compound=compoundExpressionConstraint,
                                      subExpr_refined=refinedExpressionConstraint)

# 3.2.7 exclusionExpressionConstraint
exclusionExpressionConstraint = CrossProduct(subExpressionConstraint,
                                               subExpressionConstraint)

# 3.2.6 disjunctionExpressionConstraint
disjunctionExpressionConstraint = CrossProduct(subExpressionConstraint,
                                                 Seq_1(subExpressionConstraint))


# 3.2.5 conjunctionExpressionConstraint
conjunctionExpressionConstraint = CrossProduct(subExpressionConstraint,
                                                 Seq_1(subExpressionConstraint))

# 3.2.4 compoundExpressionConstraint
compoundExpressionConstraint << FreeType(compound_conj=conjunctionExpressionConstraint,
                                           compound_disj=disjunctionExpressionConstraint,
                                           compound_excl=exclusionExpressionConstraint,
                                           compound_nested=compoundExpressionConstraint)


# 3.2.3 simpleExpressionConstraint
simpleExpressionConstraint << CrossProduct(Optional(constraintOperator), focusConcept)

# 3.2.1 unrefinedExpressionConstraint
unrefinedExpressionConstraint = FreeType(unrefined_compound=compoundExpressionConstraint,
                                           unrefined_simple=simpleExpressionConstraint)

# 3.2.2 refinedExpressionConstraint
refinedExpressionConstraint << CrossProduct(unrefinedExpressionConstraint,
                                              refinement)

# 3.2 ExpressionConstraint
expressionConstraint = FreeType(expcons_refined=refinedExpressionConstraint,
                                  expcons_unrefined=unrefinedExpressionConstraint)


class direction(BasicType): pass
source_direction = direction()
targets_direction = direction()

Quads_or_Error = FreeType(quad_value=CrossProduct(Seq(Quad), direction), qerror=ERROR)


# 5.1.2 sctIdGroups
uniqueGroupId = FreeType(ug=groupId, zg=Quad)
sctIdGroup = CrossProduct(sctId, uniqueGroupId)
sctIdGroups_or_Error = FreeType(group_value=Seq(sctIdGroup), gerror=ERROR)
