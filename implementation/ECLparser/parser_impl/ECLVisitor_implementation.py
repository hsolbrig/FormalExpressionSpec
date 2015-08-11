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

if not globals().get("__package__", None):
    from ECLParser import ECLParser
    from ECLVisitor import ECLVisitor
else:
    from ECLParser.parser.ECLParser import ECLParser
    from ECLparser.parser.ECLVisitor import ECLVisitor

from ECLparser.z import BasicType, CrossProduct, Seq_1
from ECLparser.datatypes import expressionConstraint, unrefinedExpressionConstraint, \
    simpleExpressionConstraint, focusConcept, conceptReference, conceptId, term, Optional, \
    sctId, crOrWildCard, constraintOperator, compoundExpressionConstraint, stringValue, numericValue, \
    numericComparisonOperator, expressionComparisonOperator, expressionConstraintValue, \
    subExpressionConstraint, descendantOf, descendantOrSelfOf, ancestorOf, ancestorOrSelfOf, subRefinement, \
    attributeSet, \
    subAttributeSet, sco_eq, sco_neq, nco_eq, nco_gt, nco_ge, nco_lt, nco_le, eco_eq, eco_neq, attributeName, \
    reverseFlag, cardinality, unlimitedNat, attribute, attributeGroup, disjunctionAttributeSet, \
    conjunctionAttributeSet, conjunctionRefinementSet, disjunctionRefinementSet, refinement, \
    refinementConjunctionOrDisjunction, attributeOperatorValue, refinedExpressionConstraint, \
    conjunctionOrDisjunctionAttributeSet, attributeOperator, disjunctionExpressionConstraint, \
    exclusionExpressionConstraint, conjunctionExpressionConstraint, reverseFlags, nco_neq

neq = BasicType()
wildCard = BasicType()
memberOf = BasicType()
conjunction = BasicType()
disjunction = BasicType()
exclusion = BasicType()


class ECLVisitor_implementation(ECLVisitor):

    def visitExpressionConstraint(self, ctx: ECLParser.ExpressionConstraintContext) -> expressionConstraint:
        # expressionConstraint = ws ( refinedExpressionConstraint / compoundExpressionConstraint
        #  / simpleExpressionConstraint ) ws
        if ctx.refinedExpressionConstraint():
            return expressionConstraint(expcons_refined=self.visit(ctx.refinedExpressionConstraint()))
        elif ctx.compoundExpressionConstraint():
            return expressionConstraint(expcons_compound=self.visit(ctx.compoundExpressionConstraint()))
        else:
            return expressionConstraint(expcons_simple=self.visit(ctx.simpleExpressionConstraint()))

    # Returns
    def visitUnrefinedExpressionConstraint(self, ctx: ECLParser.UnrefinedExpressionConstraintContext) \
            -> unrefinedExpressionConstraint:
        # unrefinedExpressionConstraint : compoundExpressionConstraint
        # 				  | simpleExpressionConstraint
        # 				  ;
        if ctx.compoundExpressionConstraint():
            return unrefinedExpressionConstraint(unrefined_compound=self.visit(ctx.compoundExpressionConstraint()))
        else:
            return unrefinedExpressionConstraint(unrefined_simple=self.visit(ctx.simpleExpressionConstraint()))

    def visitSimpleExpressionConstraint(self, ctx: ECLParser.SimpleExpressionConstraintContext) \
            -> simpleExpressionConstraint:
        # simpleExpressionConstraint : constraintOperator? focusConcept
        oco = self.visit(ctx.constraintOperator()) if ctx.constraintOperator() else None
        fc = self.visit(ctx.focusConcept())
        return simpleExpressionConstraint(Optional(constraintOperator)(oco), fc)

    def visitCompoundExpressionConstraint(self, ctx: ECLParser.CompoundExpressionConstraintContext):
        # compoundExpressionConstraint : conjunctionExpressionConstraint
        #                      | disjunctionExpressionConstraint
        #                      | exclusionExpressionConstraint
        #                      | '(' compoundExpressionConstraint ')'
        if ctx.compoundExpressionConstraint():
            return compoundExpressionConstraint(compound_nested=self.visit(ctx.compoundExpressionConstraint()))
        elif ctx.conjunctionExpressionConstraint():
            return compoundExpressionConstraint(compound_conj=self.visit(ctx.conjunctionExpressionConstraint()))
        elif ctx.disjunctionExpressionConstraint():
            return compoundExpressionConstraint(compound_disj=self.visit(ctx.disjunctionExpressionConstraint()))
        else:
            return compoundExpressionConstraint(compound_excl=self.visit(ctx.exclusionExpressionConstraint()))

    def visitConjunctionExpressionConstraint(self, ctx: ECLParser.ConjunctionExpressionConstraintContext) \
            -> conjunctionExpressionConstraint:
        # conjunctionExpressionConstraint : subExpressionConstraint (conjunction subExpressionConstraint)+ ;
        #
        # conjunctionExpressionConstraint == subExpressionConstraint × seq1(subExpressionConstraint)
        rval = [self.visit(sec) for sec in ctx.subExpressionConstraint()]
        return conjunctionExpressionConstraint(rval[0], Seq_1(subExpressionConstraint)(rval[1:]))

    def visitDisjunctionExpressionConstraint(self, ctx: ECLParser.DisjunctionExpressionConstraintContext) \
            -> disjunctionExpressionConstraint:
        # disjunctionExpressionConstraint = z.CrossProduct(subExpressionConstraint,
        #                                        z.Seq_1(subExpressionConstraint))
        #
        # disjunctionExpressionConstraint : subExpressionConstraint (disjunction subExpressionConstraint)+ ;
        rval = [self.visit(dec) for dec in ctx.subExpressionConstraint()]
        return disjunctionExpressionConstraint(rval[0], Seq_1(subExpressionConstraint)(rval[1:]))

    def visitExclusionExpressionConstraint(self, ctx: ECLParser.ExclusionExpressionConstraintContext) \
            -> exclusionExpressionConstraint:
        # exclusionExpressionConstraint : subExpressionConstraint exclusion subExpressionConstraint ;
        #      exclusion : MINUS ;
        #      MINUS : M I N U S ;
        #
        # exclusionExpressionConstraint == subExpressionConstraint × subExpressionConstraint
        return exclusionExpressionConstraint(self.visit(ctx.subExpressionConstraint(0)),
                                             self.visit(ctx.subExpressionConstraint(1)))

    def visitSubExpressionConstraint(self, ctx: ECLParser.SubExpressionConstraintContext) -> subExpressionConstraint:
        # subExpressionConstraint : simpleExpressionConstraint
        # 		    | '(' (compoundExpressionConstraint | refinedExpressionConstraint) ')'
        # 		    ;
        #
        # subExpressionConstraint ::=
        #   subExpr simple⟨⟨simpleExpressionConstraint⟩⟩ |
        #   subExpr compound⟨⟨compoundExpressionConstraint′⟩⟩ |
        #   subExpr refined⟨⟨refinedExpressionConstraint′⟩⟩
        if ctx.simpleExpressionConstraint():
            return subExpressionConstraint(subExpr_simple=self.visit(ctx.simpleExpressionConstraint()))
        elif ctx.compoundExpressionConstraint():
            return subExpressionConstraint(subExpr_compound=self.visit(ctx.compoundExpressionConstraint()))
        else:
            return subExpressionConstraint(subExpr_refined=self.visit(ctx.refinedExpressionConstraint()))

    def visitRefinedExpressionConstraint(self, ctx: ECLParser.RefinedExpressionConstraintContext) \
            -> refinedExpressionConstraint:
        # refinedExpressionConstraint : simpleExpressionConstraint ':' refinement ;
        #
        # refinedExpressionConstraint == simpleExpressionConstraint × refinement
        return refinedExpressionConstraint(self.visit(ctx.simpleExpressionConstraint()),
                                           self.visit(ctx.refinement()))

    def visitFocusConcept(self, ctx: ECLParser.FocusConceptContext) -> focusConcept:
        # focusConcept : memberOf? (conceptReference | wildCard) ;
        crorwc = crOrWildCard(wc=None) if ctx.wildCard() else crOrWildCard(cr=self.visit(ctx.conceptReference()))
        if ctx.memberOf():
            return focusConcept(focusConcept_m=crorwc)
        else:
            return focusConcept(focusConcept_c=crorwc)

    def visitMemberOf(self, ctx: ECLParser.MemberOfContext) -> memberOf:
        # memberOf : '^' | MEMBEROF ;
        # MEMBEROF : M E M B E R O F ;
        return memberOf

    def visitConceptReference(self, ctx: ECLParser.ConceptReferenceContext) -> conceptReference:
        # conceptReference : conceptId ( term )? ;
        return conceptReference(self.visit(ctx.conceptId()), Optional(term)(self.visit(ctx.term())))

    def visitConceptId(self, ctx: ECLParser.ConceptIdContext) -> conceptId:
        # conceptId : SCTID ;
        return conceptId(sctId(ctx.SCTID().getText()))

    def visitWildCard(self, ctx: ECLParser.WildCardContext) -> wildCard:
        # wildCard : STAR | ANY ;
        # STAR : '*' ;
        # ANY : A N Y ;
        return wildCard

    def visitTerm(self, ctx: ECLParser.TermContext) -> term:
        # term : TERM ;
        # TERM : '|' WS? ~[ |]+ (' ' ~[ |]+)* WS? '|';
        return term(re.sub(r"\s*\|\s*([^|]*?)\s*\|\s*$", '\\1', ctx.TERM().getText()))

    # Visit a parse tree produced by ECLParser#constraintOperator.
    def visitConstraintOperator(self, ctx: ECLParser.ConstraintOperatorContext) -> constraintOperator:
        # constraintOperator : descendantOrSelfOf
        #            | descendantOf
        #            | ancestorOrSelfOf
        #            | ancestorOf
        #            ;
        #
        # constraintOperator ::= descendantOrSelfOf | descendantOf | ancestorOrSelfOf | ancestorOf
        return self.visitChildren(ctx)

    def visitDescendantOf(self, ctx: ECLParser.DescendantOfContext) -> descendantOf:
        # descendantOf : '<' | DESCENDANTOF ;
        # DESCENDANTOF : '<' | D E S C E N D A N T O F ;
        return descendantOf

    def visitDescendantOrSelfOf(self, ctx: ECLParser.DescendantOrSelfOfContext) -> descendantOrSelfOf:
        # descendantOrSelfOf : '<<' | DESCENDANTORSELFOF ;
        # DESCENDANTORSELFOF : D E S C E N D A N T O R S E L F O F ;
        return descendantOrSelfOf

    def visitAncestorOf(self, ctx: ECLParser.AncestorOfContext) -> ancestorOf:
        # ancestorOf : '>' | ANCESTOROF ;
        # ANCESTOROF : A N C E S T O R O F ;
        return ancestorOf

    def visitAncestorOrSelfOf(self, ctx: ECLParser.AncestorOfContext) -> ancestorOrSelfOf:
        # ancestorOrSelfOf :  '>>' | ANCESTORORSELFOF ;
        # ANCESTORORSELFOF : A N C E S T O R O R S E L F O F ;
        return ancestorOrSelfOf

    def visitConjunction(self, ctx: ECLParser.ConjunctionContext) -> conjunction:
        # conjunction : ',' | AND ;
        # AND : A N D ;
        return conjunction

    def visitDisjunction(self, ctx: ECLParser.DisjunctionContext) -> disjunction:
        # disjunction : DISJUNCTION;
        # DISJUNCTION : O R ;
        return disjunction

    # Visit a parse tree produced by ECLParser#exclusion.
    def visitExclusion(self, ctx: ECLParser.ExclusionContext) -> exclusion:
        # exclusion : MINUS ;
        # MINUS : M I N U S ;
        return exclusion

    def visitRefinement(self, ctx: ECLParser.RefinementContext):
        # refinement : subRefinement (conjunctionRefinementSet | disjunctionRefinementSet)?
        #
        # refinement == subRefinement × refinementConjunctionOrDisjunction [0 . . 1]
        # refinementConjunctionOrDisjunction ::=
        #   refine_conjset⟨⟨conjunctionRefinementSet⟩⟩ | refine_disjset⟨⟨disjunctionRefinementSet⟩⟩
        if ctx.conjunctionRefinementSet():
            cordis = refinementConjunctionOrDisjunction(refine_conjset=self.visit(ctx.conjunctionRefinementSet()))
        elif ctx.disjunctionRefinementSet():
            cordis = refinementConjunctionOrDisjunction(refine_disjset=self.visit(ctx.disjunctionRefinementSet()))
        else:
            cordis = None
        return refinement(self.visit(ctx.subRefinement()), Optional(refinementConjunctionOrDisjunction)(cordis))

    def visitConjunctionRefinementSet(self, ctx: ECLParser.ConjunctionRefinementSetContext) -> conjunctionRefinementSet:
        # conjunctionRefinementSet : (conjunction subRefinement)+ ;
        return conjunctionRefinementSet([self.visit(sr) for sr in ctx.subRefinement()])

    def visitDisjunctionRefinementSet(self, ctx: ECLParser.DisjunctionRefinementSetContext):
        # disjunctionRefinementSet : (disjunction subRefinement)+ ;
        return disjunctionRefinementSet([self.visit(sr) for sr in ctx.subRefinement()])

    def visitSubRefinement(self, ctx: ECLParser.SubRefinementContext) -> subRefinement:
        # subRefinement : attributeSet
        #       | attributeGroup
        #       | '(' refinement ')'
        #       ;
        #
        # subRefinement ::=
        #     subrefine attset⟨⟨attributeSet⟩⟩ |
        #     subrefine attgroup⟨⟨attributeGroup⟩⟩ |
        #     subrefine refinement⟨⟨refinement′⟩⟩
        if ctx.attributeSet():
            return subRefinement(subrefine_attset=self.visit(ctx.attributeSet()))
        elif ctx.attributeGroup():
            return subRefinement(subrefine_attgroup=self.visit(ctx.attributeGroup()))
        else:
            return subRefinement(subrefine_refinement=self.visit(ctx.refinement()))

    def visitAttributeSet(self, ctx: ECLParser.AttributeSetContext) -> attributeSet:
        # attributeSet : subAttributeSet (conjunctionAttributeSet | disjunctionAttributeSet)? ;
        #
        # attributeSet == subAttributeSet × conjunctionOrDisjunctionAttributeSet [0 . . 1]
        if ctx.conjunctionAttributeSet():
            cOrDAttSet = \
                conjunctionOrDisjunctionAttributeSet(attset_conjattset=self.visit(ctx.conjunctionAttributeSet()))
        elif ctx.disjunctionAttributeSet():
            cOrDAttSet = \
                conjunctionOrDisjunctionAttributeSet(attset_disjattset=self.visit(ctx.disjunctionAttributeSet()))
        else:
            cOrDAttSet = None
        return attributeSet(self.visit(ctx.subAttributeSet()),
                            Optional(conjunctionOrDisjunctionAttributeSet)(cOrDAttSet))

    def visitConjunctionAttributeSet(self, ctx: ECLParser.ConjunctionAttributeSetContext) -> conjunctionAttributeSet:
        # conjunctionAttributeSet : (conjunction subAttributeSet)+ ;
        #
        # conjunctionAttributeSet == seq1 subAttributeSet
        return conjunctionAttributeSet([self.visit(sas) for sas in ctx.subAttributeSet()])

    def visitDisjunctionAttributeSet(self, ctx: ECLParser.DisjunctionAttributeSetContext) -> disjunctionAttributeSet:
        # disjunctionAttributeSet : (disjunction subAttributeSet)+ ;
        return disjunctionAttributeSet([self.visit(sas) for sas in ctx.subAttributeSet()])

    def visitSubAttributeSet(self, ctx: ECLParser.SubAttributeSetContext) -> subAttributeSet:
        # subAttributeSet : attribute
        #         | '(' attributeSet ')'
        #         ;
        #
        # subAttributeSet ::=
        #        subaset attribute⟨⟨attribute⟩⟩ |
        #        subaset attset⟨⟨attributeSet′⟩⟩

        if ctx.attributeSet():
            return subAttributeSet(subaset_attset=self.visit(ctx.attributeSet()))
        else:
            return subAttributeSet(subaset_attribute=self.visit(ctx.attribute()))

    def visitAttributeGroup(self, ctx: ECLParser.AttributeGroupContext) -> attributeGroup:
        # attributeGroup : cardinality? '{' attributeSet '}' ;
        #
        # attributeGroup == cardinality [0 . . 1] × attributeSet
        card = self.visit(ctx.cardinality()) if ctx.cardinality() else None
        return attributeGroup(Optional(cardinality)(card), self.visit(ctx.attributeSet()))

    def visitAttribute(self, ctx: ECLParser.AttributeContext) -> attribute:
        # attribute : cardinality? reverseFlag? attributeOperator? attributeName
        #   ( expressionComparisonOperator expressionConstraintValue
        #   | numericComparisonOperator numericValue
        #   | stringComparisonOperator stringValue )
        #   ;
        #
        # attributeOperatorValue ::=
        # attrib expr⟨⟨expressionComparisonOperator × expressionConstraintValue⟩⟩ |
        # attrib num⟨⟨numericComparisonOperator × numericValue⟩⟩ |
        # attrib str⟨⟨stringComparisonOperator × stringValue⟩⟩ numericValue ::= nv decimal⟨⟨decimalValue⟩⟩ | nv integer⟨⟨N⟩⟩
        card = self.visit(ctx.cardinality()) if ctx.cardinality() else None
        rf = self.visit(ctx.reverseFlag()) if ctx.reverseFlag() else None
        attOper = self.visit(ctx.attributeOperator()) if ctx.attributeOperator() else None
        if ctx.expressionComparisonOperator():
            cp = CrossProduct()(self.visit(ctx.expressionComparisonOperator()),
                                self.visit(ctx.expressionConstraintValue()))
            opValue = attributeOperatorValue(attrib_expr=cp)
        elif ctx.numericComparisonOperator():
            cp = CrossProduct()(self.visit(ctx.numericComparisonOperator()),
                                self.visit(ctx.numericValue()))
            opValue = attributeOperatorValue(attrib_num=cp)
        else:
            cp = CrossProduct()(self.visit(ctx.stringComparisonOperator()),
                                self.visit(ctx.stringValue()))
            opValue = attributeOperatorValue(attrib_str=cp)
        return attribute(card=Optional(cardinality)(card),
                         rf=Optional(reverseFlags)(rf),
                         attrOper=Optional(attributeOperator)(attOper),
                         name=self.visit(ctx.attributeName()),
                         opValue=opValue)

    def visitCardinality(self, ctx: ECLParser.CardinalityContext) -> cardinality:
        # cardinality : '[' NONNEGATIVEINTEGERVALUE TO (NONNEGATIVEINTEGERVALUE | many) ']' ;
        # NONNEGATIVEINTEGERVALUE : '0' | DIGITNONZERO DIGIT* ;
        #
        # min_ = int(str(ctxNONNEGATIVEINTEGERVALUE()))
        # max_ = self.visit(ctx.getChild(1))
        # max_ = unlimitedNat(num=N(int(str(max_v)))) if max_v != many else unlimitedNat(many=None)
        min_ = int(ctx.NONNEGATIVEINTEGERVALUE(0).getText())
        if ctx.many():
            max_ = unlimitedNat(many=None)
        else:
            max_ = unlimitedNat(num=int(ctx.NONNEGATIVEINTEGERVALUE(1).getText()))
        return cardinality(min_=min_, max_=max_)

    def visitReverseFlag(self, ctx: ECLParser.ReverseFlagContext) -> reverseFlag:
        # reverseFlag : REVERSEFLAG ;
        # REVERSEFLAG : (R E V E R S E O F) | 'R'  ;
        return reverseFlag

    def visitAttributeOperator(self, ctx: ECLParser.AttributeOperatorContext) -> attributeOperator:
        # attributeOperator : descendantOrSelfOf | descendantOf ;
        return self.visitChildren(ctx)

    def visitAttributeName(self, ctx: ECLParser.AttributeNameContext) -> attributeName:
        # attributeName : conceptReference | wildCard ;
        #
        # attributeName ::= ancr⟨⟨conceptReference⟩⟩ | anwc
        if ctx.conceptReference():
            return attributeName(ancr=self.visit(ctx.conceptReference()))
        else:
            return attributeName(anwc=None)

    def visitExpressionConstraintValue(self, ctx: ECLParser.ExpressionConstraintValueContext) \
            -> expressionConstraintValue:
        # expressionConstraintValue : simpleExpressionConstraint
        #                   | '(' (refinedExpressionConstraint | compoundExpressionConstraint) ')'
        #                   ;
        #
        # expressionConstraintValue ::=
        #        expression simple⟨⟨simpleExpressionConstraint⟩⟩ |
        #        expression refined⟨⟨refinedExpressionConstraint′⟩⟩ |
        #        expression compound⟨⟨compoundExpressionConstraint⟩⟩
        if ctx.simpleExpressionConstraint():
            return expressionConstraintValue(expression_simple=self.visit(ctx.simpleExpressionConstraint()))
        elif ctx.refinedExpressionConstraint():
            return expressionConstraintValue(expression_refined=self.visit(ctx.refinedExpressionConstraint()))
        else:
            return expressionConstraintValue(expression_compound=self.visit(ctx.compoundExpressionConstraint()))

    def visitExpressionComparisonOperator(self, ctx: ECLParser.ExpressionComparisonOperatorContext) \
            -> expressionComparisonOperator:
        # expressionComparisonOperator : '=' | NEQ ;
        # NEQ : '!=' | (N O T ' ' '=') | '<>' ;
        return eco_neq if ctx.NEQ() else eco_eq

    def visitNumericComparisonOperator(self, ctx: ECLParser.NumericComparisonOperatorContext) \
            -> numericComparisonOperator:
        # numericComparisonOperator : '=' | NEQ | '<' '='? | '>' '='? ;
        rval = ctx.getChild(0).getText()
        return nco_neq if ctx.NEQ() else \
            nco_eq if rval == '=' else \
            nco_ge if rval == '>=' else \
            nco_gt if rval == '>' else \
            nco_le if rval == "<=" else \
            nco_lt

    def visitStringComparisonOperator(self, ctx: ECLParser.StringComparisonOperatorContext):
        # stringComparisonOperator : '=' | NEQ ;
        return sco_neq if ctx.NEQ() else sco_eq

    def visitNumericValue(self, ctx: ECLParser.NumericValueContext) -> numericValue:
        # numericValue : NUMERICVALUE ;
        # NUMERICVALUE : '#' [-+]? [1-9] [0-9]* ('.' [0-9]+)? ;
        strval = ctx.NUMERICVALUE().getText()[1:]        # Remove the hash
        return numericValue(nv_decimal=float(strval)) if '.' in strval else \
            numericValue(nv_integer=int(strval))

    def visitStringValue(self, ctx: ECLParser.StringValueContext) -> stringValue:
        # stringValue : STRINGVALUE ;
        # STRINGVALUE : '"' ( ESCAPEDCHAR | .)*? '"' ;
        # ESCAPEDCHAR : '\\\\' | '\\"' ;
        return stringValue(ctx.STRINGVALUE().getText()[1:-1])
