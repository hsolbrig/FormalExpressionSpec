# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ECLParser.

class ECLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ECLParser#expressionConstraint.
    def visitExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#unrefinedExpressionConstraint.
    def visitUnrefinedExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#simpleExpressionConstraint.
    def visitSimpleExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#compoundExpressionConstraint.
    def visitCompoundExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conjunctionExpressionConstraint.
    def visitConjunctionExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#disjunctionExpressionConstraint.
    def visitDisjunctionExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#exclusionExpressionConstraint.
    def visitExclusionExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#subExpressionConstraint.
    def visitSubExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#refinedExpressionConstraint.
    def visitRefinedExpressionConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#focusConcept.
    def visitFocusConcept(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#memberOf.
    def visitMemberOf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conceptReference.
    def visitConceptReference(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conceptId.
    def visitConceptId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#wildCard.
    def visitWildCard(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#term.
    def visitTerm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#constraintOperator.
    def visitConstraintOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#descendantOf.
    def visitDescendantOf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#descendantOrSelfOf.
    def visitDescendantOrSelfOf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#ancestorOf.
    def visitAncestorOf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#ancestorOrSelfOf.
    def visitAncestorOrSelfOf(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conjunction.
    def visitConjunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#disjunction.
    def visitDisjunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#exclusion.
    def visitExclusion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#refinement.
    def visitRefinement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conjunctionRefinementSet.
    def visitConjunctionRefinementSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#disjunctionRefinementSet.
    def visitDisjunctionRefinementSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#subRefinement.
    def visitSubRefinement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#attributeSet.
    def visitAttributeSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#conjunctionAttributeSet.
    def visitConjunctionAttributeSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#disjunctionAttributeSet.
    def visitDisjunctionAttributeSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#subAttributeSet.
    def visitSubAttributeSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#attributeGroup.
    def visitAttributeGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#attribute.
    def visitAttribute(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#cardinality.
    def visitCardinality(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#many.
    def visitMany(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#reverseFlag.
    def visitReverseFlag(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#attributeOperator.
    def visitAttributeOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#attributeName.
    def visitAttributeName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#expressionConstraintValue.
    def visitExpressionConstraintValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#expressionComparisonOperator.
    def visitExpressionComparisonOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#numericComparisonOperator.
    def visitNumericComparisonOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#stringComparisonOperator.
    def visitStringComparisonOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#numericValue.
    def visitNumericValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECLParser#stringValue.
    def visitStringValue(self, ctx):
        return self.visitChildren(ctx)


