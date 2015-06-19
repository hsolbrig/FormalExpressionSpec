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

from ECLparser.z import BasicType, N, CrossProduct, Seq, Seq_1
from ECLparser.parser.ECLVisitor import ECLVisitor
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
    exclusionExpressionConstraint, conjunctionExpressionConstraint, reverseFlags

neq = BasicType()
wildCard = BasicType()
memberOf = BasicType()
conjunction = BasicType()
disjunction = BasicType()
exclusion = BasicType()


class ECLVisitor_implementation(ECLVisitor):
    class _child_visitor:
        def __init__(self, v, ctx):
            self._visitor = v
            self._ctx = ctx
            self._nxt_child = 0
            self._cur_child = None

        def __iter__(self):
            return self

        def __len__(self):
            return self._ctx.getChildCount() - self._nxt_child

        def __next__(self):
            if self._nxt_child >= self._ctx.getChildCount():
                raise StopIteration
            return self.getNext()

        def getNext(self, f=None):
            if self._nxt_child >= self._ctx.getChildCount():
                return None
            if self._cur_child is None:
                # TODO: recognize a terminal node and don't visit, just "str"
                self._cur_child = self._visitor.visit(self._ctx.getChild(self._nxt_child))
                if self._cur_child is None:
                    self._cur_child = str(self._ctx.getChild(self._nxt_child))
                self._nxt_child += 1

            if f is not None and not f(self._cur_child):
                return None
            rval = self._cur_child
            self._cur_child = None
            return rval

    def _simple_choice(self, expr, ctx):
        # TODO: Fix this
        rval = self.visitChildren(ctx)
        return expr.assign(rval)

    @staticmethod
    def _is_token(ctx, idx, val):
        return str(ctx.getChild(idx)) == val

    @staticmethod
    def _is_opren(ctx):
        return ECLVisitor_implementation._is_token(ctx, 0, '(')

    # Visit a parse tree produced by ECLParser#expressionConstraint.
    def visitExpressionConstraint(self, ctx):
        rval = self.visit(ctx.getChild(0))
        return expressionConstraint.assign(rval)

    # Visit a parse tree produced by ECLParser#unrefinedExpressionConstraint.
    def visitUnrefinedExpressionConstraint(self, ctx):
        # unrefinedExpressionConstraint : compoundExpressionConstraint
        # 				  | simpleExpressionConstraint
        # 				  ;
        return self._simple_choice(unrefinedExpressionConstraint, ctx)

    # Visit a parse tree produced by ECLParser#simpleExpressionConstraint.
    def visitSimpleExpressionConstraint(self, ctx):
        oco, fc = (self.visit(ctx.getChild(0)), self.visit(ctx.getChild(1))) if ctx.getChildCount() > 1 else \
            (None, self.visit(ctx.getChild(0)))
        return simpleExpressionConstraint(Optional(constraintOperator)(oco), fc)

    # Visit a parse tree produced by ECLParser#compoundExpressionConstraint.
    def visitCompoundExpressionConstraint(self, ctx):
        # ompoundExpressionConstraint ::=
        #       compound conj⟨⟨conjunctionExpressionConstraint⟩⟩ |
        #       compound disj⟨⟨disjunctionExpressionConstraint⟩⟩ |
        #       compound excl⟨⟨exclusionExpressionConstraint⟩⟩ |
        #       compound nested⟨⟨compoundExpressionConstraint⟩⟩
        if self._is_opren(ctx):
            return compoundExpressionConstraint(compound_nested=self.visit(ctx.getChild(1)))
        rval = self.visitChildren((ctx))
        if conjunctionExpressionConstraint.has_member(rval):
            return compoundExpressionConstraint(compound_conj=rval)
        elif disjunctionExpressionConstraint.has_member(rval):
            return compoundExpressionConstraint(compound_disj=rval)
        else:
            return compoundExpressionConstraint(compound_excl=rval)

    # Visit a parse tree produced by ECLParser#conjunctionExpressionConstraint.
    def visitConjunctionExpressionConstraint(self, ctx):
        # conjunctionExpressionConstraint : subExpressionConstraint (conjunction subExpressionConstraint)+ ;
        #
        # conjunctionExpressionConstraint == subExpressionConstraint × seq1(subExpressionConstraint)
        lhs = self.visit(ctx.getChild(0))
        rhs = [self.visit(ctx.getChild(i)) for i in range(2, ctx.getChildCount(), 2)]       # skipping conjunction
        return conjunctionExpressionConstraint(lhs, Seq_1(subExpressionConstraint)(rhs))

    # Visit a parse tree produced by ECLParser#disjunctionExpressionConstraint.
    def visitDisjunctionExpressionConstraint(self, ctx):
        # disjunctionExpressionConstraint = z.CrossProduct(subExpressionConstraint,
        #                                        z.Seq_1(subExpressionConstraint))
        #
        # disjunctionExpressionConstraint : subExpressionConstraint (disjunction subExpressionConstraint)+ ;
        lhs = self.visit(ctx.getChild(0))
        rhs = [self.visit(ctx.getChild(i)) for i in range(2, ctx.getChildCount(), 2)]       # skipping disjunctions
        return disjunctionExpressionConstraint(lhs, Seq_1(subExpressionConstraint)(rhs))

    # Visit a parse tree produced by ECLParser#exclusionExpressionConstraint.
    def visitExclusionExpressionConstraint(self, ctx):
        # exclusionExpressionConstraint : subExpressionConstraint exclusion subExpressionConstraint ;
        #      exclusion : MINUS ;
        #      MINUS : M I N U S ;
        #
        # exclusionExpressionConstraint == subExpressionConstraint × subExpressionConstraint
        return exclusionExpressionConstraint(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    # Visit a parse tree produced by ECLParser#subExpressionConstraint.
    def visitSubExpressionConstraint(self, ctx):
        # subExpressionConstraint : simpleExpressionConstraint
        # 		    | '(' (compoundExpressionConstraint | refinedExpressionConstraint) ')'
        # 		    ;
        #
        # subExpressionConstraint ::=
        #   subExpr simple⟨⟨simpleExpressionConstraint⟩⟩ |
        #   subExpr compound⟨⟨compoundExpressionConstraint′⟩⟩ |
        #   subExpr refined⟨⟨refinedExpressionConstraint′⟩⟩
        if self._is_opren(ctx):
            rval = self.visit(ctx.getChild(1))
            if compoundExpressionConstraint.has_member(rval):
                return subExpressionConstraint(subExpr_compound=rval)
            else:
                return subExpressionConstraint(subExpr_refined=rval)
        else:
            return subExpressionConstraint(subExpr_simple=self.visit(ctx.getChild(0)))

    # Visit a parse tree produced by ECLParser#refinedExpressionConstraint.
    def visitRefinedExpressionConstraint(self, ctx):
        # refinedExpressionConstraint : unrefinedExpressionConstraint ':' refinement
        # 			    | '(' refinedExpressionConstraint ')'
        # 			    ;
        #
        # refinedExpressionConstraint == unrefinedExpressionConstraint × refinement
        return self.visit(ctx.getChild(1)) if self._is_opren(ctx) else \
               refinedExpressionConstraint(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitFocusConcept(self, ctx):
        # focusConcept : memberOf? (conceptReference | wildCard) ;
        ref = self.visit(ctx.getChild(1)) if ctx.getChildCount() > 1 else self.visit(ctx.getChild(0))
        crorwc = crOrWildCard(wc=None) if ref == wildCard else crOrWildCard(cr=ref)
        return focusConcept(focusConcept_c=crorwc) if ctx.getChildCount() == 1 else \
            focusConcept(focusConcept_m=crorwc)

    # Visit a parse tree produced by ECLParser#memberOf.
    def visitMemberOf(self, ctx):
        return memberOf

    # Visit a parse tree produced by ECLParser#conceptReference.
    def visitConceptReference(self, ctx):
        v = self._child_visitor(self, ctx)
        return conceptReference(v.getNext(), Optional(term)(v.getNext()))

    # Visit a parse tree produced by ECLParser#conceptId.
    def visitConceptId(self, ctx):
        return conceptId(sctId(str(ctx.SCTID())))

    # Visit a parse tree produced by ECLParser#wildCard.
    def visitWildCard(self, ctx):
        return wildCard

    # Visit a parse tree produced by ECLParser#term.
    def visitTerm(self, ctx):
        return term(re.sub(r"\s*\|\s*([^|]*?)\s*\|\s*$", '\\1', str(ctx.TERM())))

    # Visit a parse tree produced by ECLParser#constraintOperator.
    def visitConstraintOperator(self, ctx):
        # constraintOperator : descendantOrSelfOf
        #            | descendantOf
        #            | ancestorOrSelfOf
        #            | ancestorOf
        #            ;
        #
        # constraintOperator ::= descendantOrSelfOf | descendantOf | ancestorOrSelfOf | ancestorOf
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECLParser#descendantOf.
    def visitDescendantOf(self, ctx):
        return descendantOf

    # Visit a parse tree produced by ECLParser#descendantOrSelfOf.
    def visitDescendantOrSelfOf(self, ctx):
        return descendantOrSelfOf

    # Visit a parse tree produced by ECLParser#ancestorOf.
    def visitAncestorOf(self, ctx):
        return ancestorOf

    # Visit a parse tree produced by ECLParser#ancestorOrSelfOf.
    def visitAncestorOrSelfOf(self, ctx):
        return ancestorOrSelfOf

    # Visit a parse tree produced by ECLParser#conjunction.
    def visitConjunction(self, ctx):
        return conjunction

    # Visit a parse tree produced by ECLParser#disjunction.
    def visitDisjunction(self, ctx):
        return disjunction

    # Visit a parse tree produced by ECLParser#exclusion.
    def visitExclusion(self, ctx):
        return exclusion

    # Visit a parse tree produced by ECLParser#refinement.
    def visitRefinement(self, ctx):
        # refinement : subRefinement (conjunctionRefinementSet | disjunctionRefinementSet)?
        #
        # refinement == subRefinement × refinementConjunctionOrDisjunction [0 . . 1]
        # refinementConjunctionOrDisjunction ::=
        #   refine_conjset⟨⟨conjunctionRefinementSet⟩⟩ | refine_disjset⟨⟨disjunctionRefinementSet⟩⟩
        lhs = self.visit(ctx.getChild(0))
        cordis = self._simple_choice(refinementConjunctionOrDisjunction, ctx) if ctx.getChildCount() > 1 else None
        return refinement(lhs, Optional(refinementConjunctionOrDisjunction)(cordis))

    # Visit a parse tree produced by ECLParser#conjunctionRefinementSet.
    def visitConjunctionRefinementSet(self, ctx):
        return conjunctionRefinementSet(self.visit(ctx.getChild(1)))

    # Visit a parse tree produced by ECLParser#disjunctionRefinementSet.
    def visitDisjunctionRefinementSet(self, ctx):
        return disjunctionRefinementSet(self.visit(ctx.getChild(1)))

    # Visit a parse tree produced by ECLParser#subRefinement.
    def visitSubRefinement(self, ctx):
        # subRefinement : attributeSet
        #       | attributeGroup
        #       | '(' refinement ')'
        #       ;
        #
        # subRefinement ::=
        #     subrefine attset⟨⟨attributeSet⟩⟩ |
        #     subrefine attgroup⟨⟨attributeGroup⟩⟩ |
        #     subrefine refinement⟨⟨refinement′⟩⟩
        if str(ctx.getChild(0)) == '(':
            return subRefinement(subrefine_refinement=self.visit(ctx.getChild(1)))
        else:
            return self._simple_choice(subRefinement, ctx)

    # Visit a parse tree produced by ECLParser#attributeSet.
    def visitAttributeSet(self, ctx):
        # attributeSet == subAttributeSet × conjunctionOrDisjunctionAttributeSet [0 . . 1]
        subAttSet = self.visit(ctx.getChild(0))
        if ctx.getChildCount() > 1:
            cont_ctx = ctx.getChild(1)
            cont = self.visit(cont_ctx)
            from ECLParser import ECLParser
            if isinstance(cont_ctx, ECLParser.ConjunctionAttributeSetContext):
                cOrDAttSet = conjunctionOrDisjunctionAttributeSet(attset_conjattset=cont)
            else:
                cOrDAttSet = conjunctionOrDisjunctionAttributeSet(attset_disjattset=cont)
        else:
            cOrDAttSet = None
        return attributeSet(subAttSet, Optional(conjunctionOrDisjunctionAttributeSet)(cOrDAttSet))

    # Visit a parse tree produced by ECLParser#conjunctionAttributeSet.
    def visitConjunctionAttributeSet(self, ctx):
        # conjunctionAttributeSet : (conjunction subAttributeSet)+ ;
        #
        # conjunctionAttributeSet == seq1 subAttributeSet
        parse_result = list(self._child_visitor(self, ctx))
        assert all(parse_result[i] == conjunction for i in range(0, len(parse_result), 2))
        return conjunctionAttributeSet([parse_result[i] for i in range(1, len(parse_result), 2)])

    # Visit a parse tree produced by ECLParser#disjunctionAttributeSet.
    def visitDisjunctionAttributeSet(self, ctx):
        parse_result = list(self._child_visitor(self, ctx))
        assert all(parse_result[i] == disjunction for i in range(0, len(parse_result), 2))
        return disjunctionAttributeSet([parse_result[i] for i in range(1, len(parse_result), 2)])

    # Visit a parse tree produced by ECLParser#subAttributeSet.
    def visitSubAttributeSet(self, ctx):
        # subAttributeSet : attribute
        #         | '(' attributeSet ')'
        #         ;
        #
        # subAttributeSet ::=
        #        subaset attribute⟨⟨attribute⟩⟩ |
        #        subaset attset⟨⟨attributeSet′⟩⟩

        if str(ctx.getChild(0)) == '(':
            return subAttributeSet(subaset_attset=self.visit(ctx.getChild(1)))
        else:
            return subAttributeSet(subaset_attribute=self.visit(ctx.getChild(0)))


    # Visit a parse tree produced by ECLParser#attributeGroup.
    def visitAttributeGroup(self, ctx):
        # attributeGroup == cardinality [0 . . 1] × attributeSet
        v = self._child_visitor(self, ctx)
        card = v.getNext(lambda e: cardinality.has_member(e))
        v.getNext()         # open braces
        attset = v.getNext()
        v.getNext()         # close braces
        return attributeGroup(Optional(cardinality)(card), attset)

    # Visit a parse tree produced by ECLParser#attribute.
    def visitAttribute(self, ctx):
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
        v = self._child_visitor(self, ctx)
        card = v.getNext(lambda e: cardinality.has_member(e))
        rf = v.getNext(lambda e: e == reverseFlag)
        # TODO: fix type checking for Seq and Set -- this is too loose
        attOper = v.getNext(lambda e: attributeOperator.has_member(e))
        name = v.getNext()
        op = v.getNext()
        targ = v.getNext()
        cp = CrossProduct()(op, targ)
        opValue = attributeOperatorValue(attrib_expr=cp) if expressionComparisonOperator.has_member(op) else \
                  attributeOperatorValue(attrib_num=cp) if numericComparisonOperator.has_member(op) else \
                  attributeOperatorValue(attrib_str=cp)
        arf = Optional(reverseFlags)(rf)
        acard = Optional(cardinality)(card)
        aattrOper = Optional(attributeOperator)(attOper)
        return attribute(card=Optional(cardinality)(card), rf=Optional(reverseFlags)(rf),
                         attrOper=Optional(attributeOperator)(attOper), name=name, opValue=opValue)

    # Visit a parse tree produced by ECLParser#cardinality.
    def visitCardinality(self, ctx):
        # cardinality : '[' NONNEGATIVEINTEGERVALUE TO (NONNEGATIVEINTEGERVALUE | MANY) ']' ;
        # NONNEGATIVEINTEGERVALUE : '0' | DIGITNONZERO DIGIT* ;
        # min_ = int(str(ctxNONNEGATIVEINTEGERVALUE()))
        # max_ = self.visit(ctx.getChild(1))
        # max_ = unlimitedNat(num=N(int(str(max_v)))) if max_v != many else unlimitedNat(many=None)
        min_ = int(str(ctx.getChild(1)))
        mx = str(ctx.getChild(3))
        max_ = unlimitedNat(num=int(mx)) if N.has_member(mx) else unlimitedNat(many=None)
        return cardinality(min_=min_, max_=max_)

    # Visit a parse tree produced by ECLParser#reverseFlag.
    def visitReverseFlag(self, ctx):
        return reverseFlag

    # Visit a parse tree produced by ECLParser#attributeOperator.
    def visitAttributeOperator(self, ctx):
        # attributeOperator : descendantOrSelfOf | descendantOf ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECLParser#attributeName.
    def visitAttributeName(self, ctx):
        # attributeName : conceptReference | wildCard ;
        # attributeName ::= ancr⟨⟨conceptReference⟩⟩ | anwc
        ref = self.visitChildren(ctx)
        return attributeName(anwc=None) if ref == wildCard else attributeName(ancr=ref)

    # Visit a parse tree produced by ECLParser#expressionConstraintValue.
    def visitExpressionConstraintValue(self, ctx):
        # expressionConstraintValue : simpleExpressionConstraint
        #                   | '(' (refinedExpressionConstraint | compoundExpressionConstraint) ')'
        #                   ;
        #
        # expressionConstraintValue ::=
        #        expression simple⟨⟨simpleExpressionConstraint⟩⟩ |
        #        expression refined⟨⟨refinedExpressionConstraint′⟩⟩ |
        #        expression compound⟨⟨compoundExpressionConstraint⟩⟩
        if self._is_opren(ctx):
            rval = self.visit(ctx.getChild(1))
            if refinedExpressionConstraint.has_member(rval):
                return expressionConstraintValue(expression_refined=rval)
            else:
                return expressionConstraintValue(expression_compound=rval)
        else:
            return expressionConstraintValue(expression_simple=self.visit(ctx.getChild(0)))

    # Visit a parse tree produced by ECLParser#expressionComparisonOperator.
    def visitExpressionComparisonOperator(self, ctx):
        # TODO: get this bit figured out
        # rval = str(self.visitChildren(ctx))
        return eco_eq if str(ctx.getChild(0)) == '=' else eco_neq

    # Visit a parse tree produced by ECLParser#neq.
    def visitNeq(self, ctx):
        return '!='

    # Visit a parse tree produced by ECLParser#numericComparisonOperator.
    def visitNumericComparisonOperator(self, ctx):
        # numericComparisonOperator : '=' | neq | '<' '='? | '>' '='? ;
        rval = str(self.visitChildren(ctx))
        return nco_eq if rval == '=' else \
               nco_gt if rval == '>' else \
               nco_ge if rval == '>=' else \
               nco_lt if rval == '<' else \
               nco_le if rval == '<=' else \
               nco_eq

    # Visit a parse tree produced by ECLParser#stringComparisonOperator.
    def visitStringComparisonOperator(self, ctx):
        # stringComparisonOperator : '=' | neq ;
        rval = self.visitChildren(ctx)
        return sco_eq if str(rval) == '=' else sco_neq

    # Visit a parse tree produced by ECLParser#numericValue.
    def visitNumericValue(self, ctx):
        # numericValue : NUMERICVALUE ;
        # NUMERICVALUE : '#' [-+]? [1-9] [0-9]* ('.' [0-9]+)? ;
        strval = str(ctx.NUMERICVALUE())[1:]        # Remove the hash
        return numericValue(nv_decimal=float(strval)) if '.' in strval else \
               numericValue(nv_integer=int(strval))

    # Visit a parse tree produced by ECLParser#stringValue.
    def visitStringValue(self, ctx):
        # stringValue : STRINGVALUE ;
        # STRINGVALUE : '"' ( ESCAPEDCHAR | .)*? '"' ;
        # ESCAPEDCHAR : '\\\\' | '\\"' ;
        return stringValue(str(ctx.STRINGVALUE())[1:-1])
