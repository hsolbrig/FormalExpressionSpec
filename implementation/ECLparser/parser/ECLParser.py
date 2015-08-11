# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECLVisitor import ECLVisitor
else:
    from ECLVisitor import ECLVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3(")
        buf.write("\u0141\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\2\5\2^\n\2\3\2\3\2\3\3\3\3\5\3d\n\3\3\4\5\4g\n\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3\6\3")
        buf.write("\6\3\6\6\6x\n\6\r\6\16\6y\3\7\3\7\3\7\3\7\6\7\u0080\n")
        buf.write("\7\r\7\16\7\u0081\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u008c\n\t\3\t\3\t\5\t\u0090\n\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\5\13\u0097\n\13\3\13\3\13\5\13\u009b\n\13\3\f\3\f\3\r")
        buf.write("\3\r\5\r\u00a1\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00ad\n\21\3\22\3\22\3\23\3\23\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\5\31\u00c0\n\31\3\32\3\32\3\32\6\32\u00c5\n")
        buf.write("\32\r\32\16\32\u00c6\3\33\3\33\3\33\6\33\u00cc\n\33\r")
        buf.write("\33\16\33\u00cd\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u00d6")
        buf.write("\n\34\3\35\3\35\3\35\5\35\u00db\n\35\3\36\3\36\3\36\6")
        buf.write("\36\u00e0\n\36\r\36\16\36\u00e1\3\37\3\37\3\37\6\37\u00e7")
        buf.write("\n\37\r\37\16\37\u00e8\3 \3 \3 \3 \3 \5 \u00f0\n \3!\5")
        buf.write("!\u00f3\n!\3!\3!\3!\3!\3\"\5\"\u00fa\n\"\3\"\5\"\u00fd")
        buf.write("\n\"\3\"\5\"\u0100\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u010c\n\"\3#\3#\3#\3#\3#\5#\u0113\n#\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\5&\u011d\n&\3\'\3\'\5\'\u0121\n\'")
        buf.write("\3(\3(\3(\3(\5(\u0127\n(\3(\3(\5(\u012b\n(\3)\3)\3*\3")
        buf.write("*\3*\3*\5*\u0133\n*\3*\3*\5*\u0137\n*\5*\u0139\n*\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\2\2.\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\13\4\2")
        buf.write("\6\6\22\22\3\2\24\25\4\2\7\7\30\30\4\2\b\b\31\31\4\2\t")
        buf.write("\t\32\32\4\2\n\n\33\33\4\2\13\13\34\34\4\2\24\24!!\4\2")
        buf.write("\20\20##\u0140\2]\3\2\2\2\4c\3\2\2\2\6f\3\2\2\2\bq\3\2")
        buf.write("\2\2\ns\3\2\2\2\f{\3\2\2\2\16\u0083\3\2\2\2\20\u008f\3")
        buf.write("\2\2\2\22\u0091\3\2\2\2\24\u0096\3\2\2\2\26\u009c\3\2")
        buf.write("\2\2\30\u009e\3\2\2\2\32\u00a2\3\2\2\2\34\u00a4\3\2\2")
        buf.write("\2\36\u00a6\3\2\2\2 \u00ac\3\2\2\2\"\u00ae\3\2\2\2$\u00b0")
        buf.write("\3\2\2\2&\u00b2\3\2\2\2(\u00b4\3\2\2\2*\u00b6\3\2\2\2")
        buf.write(",\u00b8\3\2\2\2.\u00ba\3\2\2\2\60\u00bc\3\2\2\2\62\u00c4")
        buf.write("\3\2\2\2\64\u00cb\3\2\2\2\66\u00d5\3\2\2\28\u00d7\3\2")
        buf.write("\2\2:\u00df\3\2\2\2<\u00e6\3\2\2\2>\u00ef\3\2\2\2@\u00f2")
        buf.write("\3\2\2\2B\u00f9\3\2\2\2D\u010d\3\2\2\2F\u0116\3\2\2\2")
        buf.write("H\u0118\3\2\2\2J\u011c\3\2\2\2L\u0120\3\2\2\2N\u012a\3")
        buf.write("\2\2\2P\u012c\3\2\2\2R\u0138\3\2\2\2T\u013a\3\2\2\2V\u013c")
        buf.write("\3\2\2\2X\u013e\3\2\2\2Z^\5\22\n\2[^\5\b\5\2\\^\5\6\4")
        buf.write("\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^_\3\2\2\2_`\7\2\2\3")
        buf.write("`\3\3\2\2\2ad\5\b\5\2bd\5\6\4\2ca\3\2\2\2cb\3\2\2\2d\5")
        buf.write("\3\2\2\2eg\5 \21\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\5\24")
        buf.write("\13\2i\7\3\2\2\2jr\5\n\6\2kr\5\f\7\2lr\5\16\b\2mn\7\3")
        buf.write("\2\2no\5\b\5\2op\7\4\2\2pr\3\2\2\2qj\3\2\2\2qk\3\2\2\2")
        buf.write("ql\3\2\2\2qm\3\2\2\2r\t\3\2\2\2sw\5\20\t\2tu\5*\26\2u")
        buf.write("v\5\20\t\2vx\3\2\2\2wt\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3")
        buf.write("\2\2\2z\13\3\2\2\2{\177\5\20\t\2|}\5,\27\2}~\5\20\t\2")
        buf.write("~\u0080\3\2\2\2\177|\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\r\3\2\2\2\u0083")
        buf.write("\u0084\5\20\t\2\u0084\u0085\5.\30\2\u0085\u0086\5\20\t")
        buf.write("\2\u0086\17\3\2\2\2\u0087\u0090\5\6\4\2\u0088\u008b\7")
        buf.write("\3\2\2\u0089\u008c\5\b\5\2\u008a\u008c\5\22\n\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008e\7\4\2\2\u008e\u0090\3\2\2\2\u008f\u0087\3")
        buf.write("\2\2\2\u008f\u0088\3\2\2\2\u0090\21\3\2\2\2\u0091\u0092")
        buf.write("\5\6\4\2\u0092\u0093\7\5\2\2\u0093\u0094\5\60\31\2\u0094")
        buf.write("\23\3\2\2\2\u0095\u0097\5\26\f\2\u0096\u0095\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u009b\5\30\r")
        buf.write("\2\u0099\u009b\5\34\17\2\u009a\u0098\3\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\25\3\2\2\2\u009c\u009d\t\2\2\2\u009d\27")
        buf.write("\3\2\2\2\u009e\u00a0\5\32\16\2\u009f\u00a1\5\36\20\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\31\3\2\2\2\u00a2")
        buf.write("\u00a3\7\23\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\t\3\2\2\u00a5")
        buf.write("\35\3\2\2\2\u00a6\u00a7\7\26\2\2\u00a7\37\3\2\2\2\u00a8")
        buf.write("\u00ad\5$\23\2\u00a9\u00ad\5\"\22\2\u00aa\u00ad\5(\25")
        buf.write("\2\u00ab\u00ad\5&\24\2\u00ac\u00a8\3\2\2\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("!\3\2\2\2\u00ae\u00af\t\4\2\2\u00af#\3\2\2\2\u00b0\u00b1")
        buf.write("\t\5\2\2\u00b1%\3\2\2\2\u00b2\u00b3\t\6\2\2\u00b3\'\3")
        buf.write("\2\2\2\u00b4\u00b5\t\7\2\2\u00b5)\3\2\2\2\u00b6\u00b7")
        buf.write("\t\b\2\2\u00b7+\3\2\2\2\u00b8\u00b9\7\35\2\2\u00b9-\3")
        buf.write("\2\2\2\u00ba\u00bb\7\36\2\2\u00bb/\3\2\2\2\u00bc\u00bf")
        buf.write("\5\66\34\2\u00bd\u00c0\5\62\32\2\u00be\u00c0\5\64\33\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3")
        buf.write("\2\2\2\u00c0\61\3\2\2\2\u00c1\u00c2\5*\26\2\u00c2\u00c3")
        buf.write("\5\66\34\2\u00c3\u00c5\3\2\2\2\u00c4\u00c1\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\63\3\2\2\2\u00c8\u00c9\5,\27\2\u00c9\u00ca\5\66")
        buf.write("\34\2\u00ca\u00cc\3\2\2\2\u00cb\u00c8\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\65\3\2\2\2\u00cf\u00d6\58\35\2\u00d0\u00d6\5@!\2\u00d1")
        buf.write("\u00d2\7\3\2\2\u00d2\u00d3\5\60\31\2\u00d3\u00d4\7\4\2")
        buf.write("\2\u00d4\u00d6\3\2\2\2\u00d5\u00cf\3\2\2\2\u00d5\u00d0")
        buf.write("\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d6\67\3\2\2\2\u00d7\u00da")
        buf.write("\5> \2\u00d8\u00db\5:\36\2\u00d9\u00db\5<\37\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("9\3\2\2\2\u00dc\u00dd\5*\26\2\u00dd\u00de\5> \2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00dc\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2;\3\2\2")
        buf.write("\2\u00e3\u00e4\5,\27\2\u00e4\u00e5\5> \2\u00e5\u00e7\3")
        buf.write("\2\2\2\u00e6\u00e3\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9=\3\2\2\2\u00ea\u00f0")
        buf.write("\5B\"\2\u00eb\u00ec\7\3\2\2\u00ec\u00ed\58\35\2\u00ed")
        buf.write("\u00ee\7\4\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00ea\3\2\2\2")
        buf.write("\u00ef\u00eb\3\2\2\2\u00f0?\3\2\2\2\u00f1\u00f3\5D#\2")
        buf.write("\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f5\7\f\2\2\u00f5\u00f6\58\35\2\u00f6\u00f7")
        buf.write("\7\r\2\2\u00f7A\3\2\2\2\u00f8\u00fa\5D#\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb")
        buf.write("\u00fd\5H%\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00ff\3\2\2\2\u00fe\u0100\5J&\2\u00ff\u00fe\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u010b\5L\'\2")
        buf.write("\u0102\u0103\5P)\2\u0103\u0104\5N(\2\u0104\u010c\3\2\2")
        buf.write("\2\u0105\u0106\5R*\2\u0106\u0107\5V,\2\u0107\u010c\3\2")
        buf.write("\2\2\u0108\u0109\5T+\2\u0109\u010a\5X-\2\u010a\u010c\3")
        buf.write("\2\2\2\u010b\u0102\3\2\2\2\u010b\u0105\3\2\2\2\u010b\u0108")
        buf.write("\3\2\2\2\u010cC\3\2\2\2\u010d\u010e\7\16\2\2\u010e\u010f")
        buf.write("\7\37\2\2\u010f\u0112\7 \2\2\u0110\u0113\7\37\2\2\u0111")
        buf.write("\u0113\5F$\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0115\7\17\2\2\u0115E\3\2\2\2\u0116")
        buf.write("\u0117\t\t\2\2\u0117G\3\2\2\2\u0118\u0119\7\"\2\2\u0119")
        buf.write("I\3\2\2\2\u011a\u011d\5$\23\2\u011b\u011d\5\"\22\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011dK\3\2\2\2\u011e")
        buf.write("\u0121\5\30\r\2\u011f\u0121\5\34\17\2\u0120\u011e\3\2")
        buf.write("\2\2\u0120\u011f\3\2\2\2\u0121M\3\2\2\2\u0122\u012b\5")
        buf.write("\6\4\2\u0123\u0126\7\3\2\2\u0124\u0127\5\22\n\2\u0125")
        buf.write("\u0127\5\b\5\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0129\7\4\2\2\u0129\u012b\3")
        buf.write("\2\2\2\u012a\u0122\3\2\2\2\u012a\u0123\3\2\2\2\u012bO")
        buf.write("\3\2\2\2\u012c\u012d\t\n\2\2\u012dQ\3\2\2\2\u012e\u0139")
        buf.write("\7\20\2\2\u012f\u0139\7#\2\2\u0130\u0132\7\7\2\2\u0131")
        buf.write("\u0133\7\20\2\2\u0132\u0131\3\2\2\2\u0132\u0133\3\2\2")
        buf.write("\2\u0133\u0139\3\2\2\2\u0134\u0136\7\t\2\2\u0135\u0137")
        buf.write("\7\20\2\2\u0136\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0139\3\2\2\2\u0138\u012e\3\2\2\2\u0138\u012f\3\2\2\2")
        buf.write("\u0138\u0130\3\2\2\2\u0138\u0134\3\2\2\2\u0139S\3\2\2")
        buf.write("\2\u013a\u013b\t\n\2\2\u013bU\3\2\2\2\u013c\u013d\7$\2")
        buf.write("\2\u013dW\3\2\2\2\u013e\u013f\7%\2\2\u013fY\3\2\2\2#]")
        buf.write("cfqy\u0081\u008b\u008f\u0096\u009a\u00a0\u00ac\u00bf\u00c6")
        buf.write("\u00cd\u00d5\u00da\u00e1\u00e8\u00ef\u00f2\u00f9\u00fc")
        buf.write("\u00ff\u010b\u0112\u011c\u0120\u0126\u012a\u0132\u0136")
        buf.write("\u0138")
        return buf.getvalue()


class ECLParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"':'", u"'^'", u"'<'", 
                     u"'<<'", u"'>'", u"'>>'", u"','", u"'{'", u"'}'", u"'['", 
                     u"']'", u"'='", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'*'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"WS", u"MEMBEROF", 
                      u"SCTID", u"STAR", u"ANY", u"TERM", u"COMMENT", u"DESCENDANTOF", 
                      u"DESCENDANTORSELFOF", u"ANCESTOROF", u"ANCESTORORSELFOF", 
                      u"AND", u"DISJUNCTION", u"MINUS", u"NONNEGATIVEINTEGERVALUE", 
                      u"TO", u"MANY", u"REVERSEFLAG", u"NEQ", u"NUMERICVALUE", 
                      u"STRINGVALUE", u"ESCAPEDCHAR", u"DIGITNONZERO", u"DIGIT" ]

    RULE_expressionConstraint = 0
    RULE_unrefinedExpressionConstraint = 1
    RULE_simpleExpressionConstraint = 2
    RULE_compoundExpressionConstraint = 3
    RULE_conjunctionExpressionConstraint = 4
    RULE_disjunctionExpressionConstraint = 5
    RULE_exclusionExpressionConstraint = 6
    RULE_subExpressionConstraint = 7
    RULE_refinedExpressionConstraint = 8
    RULE_focusConcept = 9
    RULE_memberOf = 10
    RULE_conceptReference = 11
    RULE_conceptId = 12
    RULE_wildCard = 13
    RULE_term = 14
    RULE_constraintOperator = 15
    RULE_descendantOf = 16
    RULE_descendantOrSelfOf = 17
    RULE_ancestorOf = 18
    RULE_ancestorOrSelfOf = 19
    RULE_conjunction = 20
    RULE_disjunction = 21
    RULE_exclusion = 22
    RULE_refinement = 23
    RULE_conjunctionRefinementSet = 24
    RULE_disjunctionRefinementSet = 25
    RULE_subRefinement = 26
    RULE_attributeSet = 27
    RULE_conjunctionAttributeSet = 28
    RULE_disjunctionAttributeSet = 29
    RULE_subAttributeSet = 30
    RULE_attributeGroup = 31
    RULE_attribute = 32
    RULE_cardinality = 33
    RULE_many = 34
    RULE_reverseFlag = 35
    RULE_attributeOperator = 36
    RULE_attributeName = 37
    RULE_expressionConstraintValue = 38
    RULE_expressionComparisonOperator = 39
    RULE_numericComparisonOperator = 40
    RULE_stringComparisonOperator = 41
    RULE_numericValue = 42
    RULE_stringValue = 43

    ruleNames =  [ "expressionConstraint", "unrefinedExpressionConstraint", 
                   "simpleExpressionConstraint", "compoundExpressionConstraint", 
                   "conjunctionExpressionConstraint", "disjunctionExpressionConstraint", 
                   "exclusionExpressionConstraint", "subExpressionConstraint", 
                   "refinedExpressionConstraint", "focusConcept", "memberOf", 
                   "conceptReference", "conceptId", "wildCard", "term", 
                   "constraintOperator", "descendantOf", "descendantOrSelfOf", 
                   "ancestorOf", "ancestorOrSelfOf", "conjunction", "disjunction", 
                   "exclusion", "refinement", "conjunctionRefinementSet", 
                   "disjunctionRefinementSet", "subRefinement", "attributeSet", 
                   "conjunctionAttributeSet", "disjunctionAttributeSet", 
                   "subAttributeSet", "attributeGroup", "attribute", "cardinality", 
                   "many", "reverseFlag", "attributeOperator", "attributeName", 
                   "expressionConstraintValue", "expressionComparisonOperator", 
                   "numericComparisonOperator", "stringComparisonOperator", 
                   "numericValue", "stringValue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    WS=15
    MEMBEROF=16
    SCTID=17
    STAR=18
    ANY=19
    TERM=20
    COMMENT=21
    DESCENDANTOF=22
    DESCENDANTORSELFOF=23
    ANCESTOROF=24
    ANCESTORORSELFOF=25
    AND=26
    DISJUNCTION=27
    MINUS=28
    NONNEGATIVEINTEGERVALUE=29
    TO=30
    MANY=31
    REVERSEFLAG=32
    NEQ=33
    NUMERICVALUE=34
    STRINGVALUE=35
    ESCAPEDCHAR=36
    DIGITNONZERO=37
    DIGIT=38

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ECLParser.EOF, 0)

        def refinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.RefinedExpressionConstraintContext,0)


        def compoundExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.CompoundExpressionConstraintContext,0)


        def simpleExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.SimpleExpressionConstraintContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_expressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def expressionConstraint(self):

        localctx = ECLParser.ExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expressionConstraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 88
                self.refinedExpressionConstraint()
                pass

            elif la_ == 2:
                self.state = 89
                self.compoundExpressionConstraint()
                pass

            elif la_ == 3:
                self.state = 90
                self.simpleExpressionConstraint()
                pass


            self.state = 93
            self.match(ECLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnrefinedExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compoundExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.CompoundExpressionConstraintContext,0)


        def simpleExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.SimpleExpressionConstraintContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_unrefinedExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitUnrefinedExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def unrefinedExpressionConstraint(self):

        localctx = ECLParser.UnrefinedExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_unrefinedExpressionConstraint)
        try:
            self.state = 97
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.compoundExpressionConstraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.simpleExpressionConstraint()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpleExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def focusConcept(self):
            return self.getTypedRuleContext(ECLParser.FocusConceptContext,0)


        def constraintOperator(self):
            return self.getTypedRuleContext(ECLParser.ConstraintOperatorContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_simpleExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitSimpleExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def simpleExpressionConstraint(self):

        localctx = ECLParser.SimpleExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simpleExpressionConstraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.T__4) | (1 << ECLParser.T__5) | (1 << ECLParser.T__6) | (1 << ECLParser.T__7) | (1 << ECLParser.DESCENDANTOF) | (1 << ECLParser.DESCENDANTORSELFOF) | (1 << ECLParser.ANCESTOROF) | (1 << ECLParser.ANCESTORORSELFOF))) != 0):
                self.state = 99
                self.constraintOperator()


            self.state = 102
            self.focusConcept()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunctionExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.ConjunctionExpressionConstraintContext,0)


        def disjunctionExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.DisjunctionExpressionConstraintContext,0)


        def exclusionExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.ExclusionExpressionConstraintContext,0)


        def compoundExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.CompoundExpressionConstraintContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_compoundExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitCompoundExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def compoundExpressionConstraint(self):

        localctx = ECLParser.CompoundExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compoundExpressionConstraint)
        try:
            self.state = 111
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.conjunctionExpressionConstraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.disjunctionExpressionConstraint()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.exclusionExpressionConstraint()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(ECLParser.T__0)
                self.state = 108
                self.compoundExpressionConstraint()
                self.state = 109
                self.match(ECLParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subExpressionConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubExpressionConstraintContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubExpressionConstraintContext,i)


        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.ConjunctionContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_conjunctionExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConjunctionExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def conjunctionExpressionConstraint(self):

        localctx = ECLParser.ConjunctionExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conjunctionExpressionConstraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.subExpressionConstraint()
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.conjunction()
                self.state = 115
                self.subExpressionConstraint()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECLParser.T__8 or _la==ECLParser.AND):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subExpressionConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubExpressionConstraintContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubExpressionConstraintContext,i)


        def disjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.DisjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.DisjunctionContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_disjunctionExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDisjunctionExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def disjunctionExpressionConstraint(self):

        localctx = ECLParser.DisjunctionExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_disjunctionExpressionConstraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.subExpressionConstraint()
            self.state = 125 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.disjunction()
                self.state = 123
                self.subExpressionConstraint()
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECLParser.DISJUNCTION):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExclusionExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subExpressionConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubExpressionConstraintContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubExpressionConstraintContext,i)


        def exclusion(self):
            return self.getTypedRuleContext(ECLParser.ExclusionContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_exclusionExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitExclusionExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def exclusionExpressionConstraint(self):

        localctx = ECLParser.ExclusionExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exclusionExpressionConstraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.subExpressionConstraint()
            self.state = 130
            self.exclusion()
            self.state = 131
            self.subExpressionConstraint()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.SimpleExpressionConstraintContext,0)


        def compoundExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.CompoundExpressionConstraintContext,0)


        def refinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.RefinedExpressionConstraintContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_subExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitSubExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def subExpressionConstraint(self):

        localctx = ECLParser.SubExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_subExpressionConstraint)
        try:
            self.state = 141
            token = self._input.LA(1)
            if token in [ECLParser.T__3, ECLParser.T__4, ECLParser.T__5, ECLParser.T__6, ECLParser.T__7, ECLParser.MEMBEROF, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.ANCESTOROF, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.simpleExpressionConstraint()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(ECLParser.T__0)
                self.state = 137
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 135
                    self.compoundExpressionConstraint()
                    pass

                elif la_ == 2:
                    self.state = 136
                    self.refinedExpressionConstraint()
                    pass


                self.state = 139
                self.match(ECLParser.T__1)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RefinedExpressionConstraintContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.SimpleExpressionConstraintContext,0)


        def refinement(self):
            return self.getTypedRuleContext(ECLParser.RefinementContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_refinedExpressionConstraint

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitRefinedExpressionConstraint(self)
            else:
                return visitor.visitChildren(self)




    def refinedExpressionConstraint(self):

        localctx = ECLParser.RefinedExpressionConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_refinedExpressionConstraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.simpleExpressionConstraint()
            self.state = 144
            self.match(ECLParser.T__2)
            self.state = 145
            self.refinement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FocusConceptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conceptReference(self):
            return self.getTypedRuleContext(ECLParser.ConceptReferenceContext,0)


        def wildCard(self):
            return self.getTypedRuleContext(ECLParser.WildCardContext,0)


        def memberOf(self):
            return self.getTypedRuleContext(ECLParser.MemberOfContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_focusConcept

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitFocusConcept(self)
            else:
                return visitor.visitChildren(self)




    def focusConcept(self):

        localctx = ECLParser.FocusConceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_focusConcept)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if _la==ECLParser.T__3 or _la==ECLParser.MEMBEROF:
                self.state = 147
                self.memberOf()


            self.state = 152
            token = self._input.LA(1)
            if token in [ECLParser.SCTID]:
                self.state = 150
                self.conceptReference()

            elif token in [ECLParser.STAR, ECLParser.ANY]:
                self.state = 151
                self.wildCard()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MemberOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEMBEROF(self):
            return self.getToken(ECLParser.MEMBEROF, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_memberOf

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitMemberOf(self)
            else:
                return visitor.visitChildren(self)




    def memberOf(self):

        localctx = ECLParser.MemberOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_memberOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__3 or _la==ECLParser.MEMBEROF):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConceptReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conceptId(self):
            return self.getTypedRuleContext(ECLParser.ConceptIdContext,0)


        def term(self):
            return self.getTypedRuleContext(ECLParser.TermContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_conceptReference

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConceptReference(self)
            else:
                return visitor.visitChildren(self)




    def conceptReference(self):

        localctx = ECLParser.ConceptReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_conceptReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.conceptId()
            self.state = 158
            _la = self._input.LA(1)
            if _la==ECLParser.TERM:
                self.state = 157
                self.term()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConceptIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCTID(self):
            return self.getToken(ECLParser.SCTID, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_conceptId

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConceptId(self)
            else:
                return visitor.visitChildren(self)




    def conceptId(self):

        localctx = ECLParser.ConceptIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conceptId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ECLParser.SCTID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WildCardContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ECLParser.STAR, 0)

        def ANY(self):
            return self.getToken(ECLParser.ANY, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_wildCard

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitWildCard(self)
            else:
                return visitor.visitChildren(self)




    def wildCard(self):

        localctx = ECLParser.WildCardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_wildCard)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not(_la==ECLParser.STAR or _la==ECLParser.ANY):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM(self):
            return self.getToken(ECLParser.TERM, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ECLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(ECLParser.TERM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstraintOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def descendantOrSelfOf(self):
            return self.getTypedRuleContext(ECLParser.DescendantOrSelfOfContext,0)


        def descendantOf(self):
            return self.getTypedRuleContext(ECLParser.DescendantOfContext,0)


        def ancestorOrSelfOf(self):
            return self.getTypedRuleContext(ECLParser.AncestorOrSelfOfContext,0)


        def ancestorOf(self):
            return self.getTypedRuleContext(ECLParser.AncestorOfContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_constraintOperator

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConstraintOperator(self)
            else:
                return visitor.visitChildren(self)




    def constraintOperator(self):

        localctx = ECLParser.ConstraintOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constraintOperator)
        try:
            self.state = 170
            token = self._input.LA(1)
            if token in [ECLParser.T__5, ECLParser.DESCENDANTORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.descendantOrSelfOf()

            elif token in [ECLParser.T__4, ECLParser.DESCENDANTOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.descendantOf()

            elif token in [ECLParser.T__7, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.ancestorOrSelfOf()

            elif token in [ECLParser.T__6, ECLParser.ANCESTOROF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                self.ancestorOf()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DescendantOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCENDANTOF(self):
            return self.getToken(ECLParser.DESCENDANTOF, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_descendantOf

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDescendantOf(self)
            else:
                return visitor.visitChildren(self)




    def descendantOf(self):

        localctx = ECLParser.DescendantOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_descendantOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__4 or _la==ECLParser.DESCENDANTOF):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DescendantOrSelfOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESCENDANTORSELFOF(self):
            return self.getToken(ECLParser.DESCENDANTORSELFOF, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_descendantOrSelfOf

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDescendantOrSelfOf(self)
            else:
                return visitor.visitChildren(self)




    def descendantOrSelfOf(self):

        localctx = ECLParser.DescendantOrSelfOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_descendantOrSelfOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__5 or _la==ECLParser.DESCENDANTORSELFOF):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AncestorOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANCESTOROF(self):
            return self.getToken(ECLParser.ANCESTOROF, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_ancestorOf

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAncestorOf(self)
            else:
                return visitor.visitChildren(self)




    def ancestorOf(self):

        localctx = ECLParser.AncestorOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ancestorOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__6 or _la==ECLParser.ANCESTOROF):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AncestorOrSelfOfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANCESTORORSELFOF(self):
            return self.getToken(ECLParser.ANCESTORORSELFOF, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_ancestorOrSelfOf

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAncestorOrSelfOf(self)
            else:
                return visitor.visitChildren(self)




    def ancestorOrSelfOf(self):

        localctx = ECLParser.AncestorOrSelfOfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ancestorOrSelfOf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__7 or _la==ECLParser.ANCESTORORSELFOF):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ECLParser.AND, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_conjunction

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)




    def conjunction(self):

        localctx = ECLParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__8 or _la==ECLParser.AND):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISJUNCTION(self):
            return self.getToken(ECLParser.DISJUNCTION, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_disjunction

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)




    def disjunction(self):

        localctx = ECLParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_disjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ECLParser.DISJUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExclusionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ECLParser.MINUS, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_exclusion

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitExclusion(self)
            else:
                return visitor.visitChildren(self)




    def exclusion(self):

        localctx = ECLParser.ExclusionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exclusion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ECLParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RefinementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subRefinement(self):
            return self.getTypedRuleContext(ECLParser.SubRefinementContext,0)


        def conjunctionRefinementSet(self):
            return self.getTypedRuleContext(ECLParser.ConjunctionRefinementSetContext,0)


        def disjunctionRefinementSet(self):
            return self.getTypedRuleContext(ECLParser.DisjunctionRefinementSetContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_refinement

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitRefinement(self)
            else:
                return visitor.visitChildren(self)




    def refinement(self):

        localctx = ECLParser.RefinementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_refinement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.subRefinement()
            self.state = 189
            token = self._input.LA(1)
            if token in [ECLParser.T__8, ECLParser.AND]:
                self.state = 187
                self.conjunctionRefinementSet()
                pass
            elif token in [ECLParser.DISJUNCTION]:
                self.state = 188
                self.disjunctionRefinementSet()
                pass
            elif token in [ECLParser.EOF, ECLParser.T__1]:
                pass
            else:
                raise NoViableAltException(self)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionRefinementSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.ConjunctionContext,i)


        def subRefinement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubRefinementContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubRefinementContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_conjunctionRefinementSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConjunctionRefinementSet(self)
            else:
                return visitor.visitChildren(self)




    def conjunctionRefinementSet(self):

        localctx = ECLParser.ConjunctionRefinementSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_conjunctionRefinementSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 191
                self.conjunction()
                self.state = 192
                self.subRefinement()
                self.state = 196 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECLParser.T__8 or _la==ECLParser.AND):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionRefinementSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.DisjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.DisjunctionContext,i)


        def subRefinement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubRefinementContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubRefinementContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_disjunctionRefinementSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDisjunctionRefinementSet(self)
            else:
                return visitor.visitChildren(self)




    def disjunctionRefinementSet(self):

        localctx = ECLParser.DisjunctionRefinementSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_disjunctionRefinementSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.disjunction()
                self.state = 199
                self.subRefinement()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ECLParser.DISJUNCTION):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubRefinementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeSet(self):
            return self.getTypedRuleContext(ECLParser.AttributeSetContext,0)


        def attributeGroup(self):
            return self.getTypedRuleContext(ECLParser.AttributeGroupContext,0)


        def refinement(self):
            return self.getTypedRuleContext(ECLParser.RefinementContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_subRefinement

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitSubRefinement(self)
            else:
                return visitor.visitChildren(self)




    def subRefinement(self):

        localctx = ECLParser.SubRefinementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_subRefinement)
        try:
            self.state = 211
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.attributeSet()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.attributeGroup()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(ECLParser.T__0)
                self.state = 208
                self.refinement()
                self.state = 209
                self.match(ECLParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subAttributeSet(self):
            return self.getTypedRuleContext(ECLParser.SubAttributeSetContext,0)


        def conjunctionAttributeSet(self):
            return self.getTypedRuleContext(ECLParser.ConjunctionAttributeSetContext,0)


        def disjunctionAttributeSet(self):
            return self.getTypedRuleContext(ECLParser.DisjunctionAttributeSetContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_attributeSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAttributeSet(self)
            else:
                return visitor.visitChildren(self)




    def attributeSet(self):

        localctx = ECLParser.AttributeSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_attributeSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.subAttributeSet()
            self.state = 216
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 214
                self.conjunctionAttributeSet()

            elif la_ == 2:
                self.state = 215
                self.disjunctionAttributeSet()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionAttributeSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.ConjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.ConjunctionContext,i)


        def subAttributeSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubAttributeSetContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubAttributeSetContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_conjunctionAttributeSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitConjunctionAttributeSet(self)
            else:
                return visitor.visitChildren(self)




    def conjunctionAttributeSet(self):

        localctx = ECLParser.ConjunctionAttributeSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_conjunctionAttributeSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 218
                    self.conjunction()
                    self.state = 219
                    self.subAttributeSet()

                else:
                    raise NoViableAltException(self)
                self.state = 223 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionAttributeSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.DisjunctionContext)
            else:
                return self.getTypedRuleContext(ECLParser.DisjunctionContext,i)


        def subAttributeSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ECLParser.SubAttributeSetContext)
            else:
                return self.getTypedRuleContext(ECLParser.SubAttributeSetContext,i)


        def getRuleIndex(self):
            return ECLParser.RULE_disjunctionAttributeSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitDisjunctionAttributeSet(self)
            else:
                return visitor.visitChildren(self)




    def disjunctionAttributeSet(self):

        localctx = ECLParser.DisjunctionAttributeSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_disjunctionAttributeSet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 225
                    self.disjunction()
                    self.state = 226
                    self.subAttributeSet()

                else:
                    raise NoViableAltException(self)
                self.state = 230 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubAttributeSetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(ECLParser.AttributeContext,0)


        def attributeSet(self):
            return self.getTypedRuleContext(ECLParser.AttributeSetContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_subAttributeSet

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitSubAttributeSet(self)
            else:
                return visitor.visitChildren(self)




    def subAttributeSet(self):

        localctx = ECLParser.SubAttributeSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_subAttributeSet)
        try:
            self.state = 237
            token = self._input.LA(1)
            if token in [ECLParser.T__4, ECLParser.T__5, ECLParser.T__11, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.REVERSEFLAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.attribute()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(ECLParser.T__0)
                self.state = 234
                self.attributeSet()
                self.state = 235
                self.match(ECLParser.T__1)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeGroupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeSet(self):
            return self.getTypedRuleContext(ECLParser.AttributeSetContext,0)


        def cardinality(self):
            return self.getTypedRuleContext(ECLParser.CardinalityContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_attributeGroup

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAttributeGroup(self)
            else:
                return visitor.visitChildren(self)




    def attributeGroup(self):

        localctx = ECLParser.AttributeGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_attributeGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if _la==ECLParser.T__11:
                self.state = 239
                self.cardinality()


            self.state = 242
            self.match(ECLParser.T__9)
            self.state = 243
            self.attributeSet()
            self.state = 244
            self.match(ECLParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeName(self):
            return self.getTypedRuleContext(ECLParser.AttributeNameContext,0)


        def expressionComparisonOperator(self):
            return self.getTypedRuleContext(ECLParser.ExpressionComparisonOperatorContext,0)


        def expressionConstraintValue(self):
            return self.getTypedRuleContext(ECLParser.ExpressionConstraintValueContext,0)


        def numericComparisonOperator(self):
            return self.getTypedRuleContext(ECLParser.NumericComparisonOperatorContext,0)


        def numericValue(self):
            return self.getTypedRuleContext(ECLParser.NumericValueContext,0)


        def stringComparisonOperator(self):
            return self.getTypedRuleContext(ECLParser.StringComparisonOperatorContext,0)


        def stringValue(self):
            return self.getTypedRuleContext(ECLParser.StringValueContext,0)


        def cardinality(self):
            return self.getTypedRuleContext(ECLParser.CardinalityContext,0)


        def reverseFlag(self):
            return self.getTypedRuleContext(ECLParser.ReverseFlagContext,0)


        def attributeOperator(self):
            return self.getTypedRuleContext(ECLParser.AttributeOperatorContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = ECLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            _la = self._input.LA(1)
            if _la==ECLParser.T__11:
                self.state = 246
                self.cardinality()


            self.state = 250
            _la = self._input.LA(1)
            if _la==ECLParser.REVERSEFLAG:
                self.state = 249
                self.reverseFlag()


            self.state = 253
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.T__4) | (1 << ECLParser.T__5) | (1 << ECLParser.DESCENDANTOF) | (1 << ECLParser.DESCENDANTORSELFOF))) != 0):
                self.state = 252
                self.attributeOperator()


            self.state = 255
            self.attributeName()
            self.state = 265
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 256
                self.expressionComparisonOperator()
                self.state = 257
                self.expressionConstraintValue()
                pass

            elif la_ == 2:
                self.state = 259
                self.numericComparisonOperator()
                self.state = 260
                self.numericValue()
                pass

            elif la_ == 3:
                self.state = 262
                self.stringComparisonOperator()
                self.state = 263
                self.stringValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CardinalityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NONNEGATIVEINTEGERVALUE(self, i:int=None):
            if i is None:
                return self.getTokens(ECLParser.NONNEGATIVEINTEGERVALUE)
            else:
                return self.getToken(ECLParser.NONNEGATIVEINTEGERVALUE, i)

        def TO(self):
            return self.getToken(ECLParser.TO, 0)

        def many(self):
            return self.getTypedRuleContext(ECLParser.ManyContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_cardinality

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitCardinality(self)
            else:
                return visitor.visitChildren(self)




    def cardinality(self):

        localctx = ECLParser.CardinalityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_cardinality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(ECLParser.T__11)
            self.state = 268
            self.match(ECLParser.NONNEGATIVEINTEGERVALUE)
            self.state = 269
            self.match(ECLParser.TO)
            self.state = 272
            token = self._input.LA(1)
            if token in [ECLParser.NONNEGATIVEINTEGERVALUE]:
                self.state = 270
                self.match(ECLParser.NONNEGATIVEINTEGERVALUE)

            elif token in [ECLParser.STAR, ECLParser.MANY]:
                self.state = 271
                self.many()

            else:
                raise NoViableAltException(self)

            self.state = 274
            self.match(ECLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ManyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MANY(self):
            return self.getToken(ECLParser.MANY, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_many

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitMany(self)
            else:
                return visitor.visitChildren(self)




    def many(self):

        localctx = ECLParser.ManyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_many)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not(_la==ECLParser.STAR or _la==ECLParser.MANY):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReverseFlagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REVERSEFLAG(self):
            return self.getToken(ECLParser.REVERSEFLAG, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_reverseFlag

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitReverseFlag(self)
            else:
                return visitor.visitChildren(self)




    def reverseFlag(self):

        localctx = ECLParser.ReverseFlagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_reverseFlag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ECLParser.REVERSEFLAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def descendantOrSelfOf(self):
            return self.getTypedRuleContext(ECLParser.DescendantOrSelfOfContext,0)


        def descendantOf(self):
            return self.getTypedRuleContext(ECLParser.DescendantOfContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_attributeOperator

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAttributeOperator(self)
            else:
                return visitor.visitChildren(self)




    def attributeOperator(self):

        localctx = ECLParser.AttributeOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_attributeOperator)
        try:
            self.state = 282
            token = self._input.LA(1)
            if token in [ECLParser.T__5, ECLParser.DESCENDANTORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.descendantOrSelfOf()

            elif token in [ECLParser.T__4, ECLParser.DESCENDANTOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.descendantOf()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conceptReference(self):
            return self.getTypedRuleContext(ECLParser.ConceptReferenceContext,0)


        def wildCard(self):
            return self.getTypedRuleContext(ECLParser.WildCardContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_attributeName

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitAttributeName(self)
            else:
                return visitor.visitChildren(self)




    def attributeName(self):

        localctx = ECLParser.AttributeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_attributeName)
        try:
            self.state = 286
            token = self._input.LA(1)
            if token in [ECLParser.SCTID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.conceptReference()

            elif token in [ECLParser.STAR, ECLParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.wildCard()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionConstraintValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.SimpleExpressionConstraintContext,0)


        def refinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.RefinedExpressionConstraintContext,0)


        def compoundExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.CompoundExpressionConstraintContext,0)


        def getRuleIndex(self):
            return ECLParser.RULE_expressionConstraintValue

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitExpressionConstraintValue(self)
            else:
                return visitor.visitChildren(self)




    def expressionConstraintValue(self):

        localctx = ECLParser.ExpressionConstraintValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expressionConstraintValue)
        try:
            self.state = 296
            token = self._input.LA(1)
            if token in [ECLParser.T__3, ECLParser.T__4, ECLParser.T__5, ECLParser.T__6, ECLParser.T__7, ECLParser.MEMBEROF, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.ANCESTOROF, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.simpleExpressionConstraint()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(ECLParser.T__0)
                self.state = 292
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 290
                    self.refinedExpressionConstraint()
                    pass

                elif la_ == 2:
                    self.state = 291
                    self.compoundExpressionConstraint()
                    pass


                self.state = 294
                self.match(ECLParser.T__1)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionComparisonOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEQ(self):
            return self.getToken(ECLParser.NEQ, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_expressionComparisonOperator

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitExpressionComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def expressionComparisonOperator(self):

        localctx = ECLParser.ExpressionComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expressionComparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__13 or _la==ECLParser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericComparisonOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEQ(self):
            return self.getToken(ECLParser.NEQ, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_numericComparisonOperator

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitNumericComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def numericComparisonOperator(self):

        localctx = ECLParser.NumericComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_numericComparisonOperator)
        self._la = 0 # Token type
        try:
            self.state = 310
            token = self._input.LA(1)
            if token in [ECLParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(ECLParser.T__13)

            elif token in [ECLParser.NEQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(ECLParser.NEQ)

            elif token in [ECLParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.match(ECLParser.T__4)
                self.state = 304
                _la = self._input.LA(1)
                if _la==ECLParser.T__13:
                    self.state = 303
                    self.match(ECLParser.T__13)



            elif token in [ECLParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 306
                self.match(ECLParser.T__6)
                self.state = 308
                _la = self._input.LA(1)
                if _la==ECLParser.T__13:
                    self.state = 307
                    self.match(ECLParser.T__13)



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringComparisonOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEQ(self):
            return self.getToken(ECLParser.NEQ, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_stringComparisonOperator

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitStringComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def stringComparisonOperator(self):

        localctx = ECLParser.StringComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stringComparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not(_la==ECLParser.T__13 or _la==ECLParser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumericValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERICVALUE(self):
            return self.getToken(ECLParser.NUMERICVALUE, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_numericValue

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitNumericValue(self)
            else:
                return visitor.visitChildren(self)




    def numericValue(self):

        localctx = ECLParser.NumericValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_numericValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ECLParser.NUMERICVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGVALUE(self):
            return self.getToken(ECLParser.STRINGVALUE, 0)

        def getRuleIndex(self):
            return ECLParser.RULE_stringValue

        def accept(self, visitor:ParseTreeVisitor):
            if isinstance( visitor, ECLVisitor ):
                return visitor.visitStringValue(self)
            else:
                return visitor.visitChildren(self)




    def stringValue(self):

        localctx = ECLParser.StringValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stringValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(ECLParser.STRINGVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




