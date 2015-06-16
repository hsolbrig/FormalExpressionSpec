# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ECLVisitor import ECLVisitor
else:
    from ECLparser.parser.ECLVisitor import ECLVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3(")
        buf.write("\u0144\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\5\2]\n\2\3\3\3\3\5\3a\n\3\3\4\5\4d\n\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5o\n\5\3\6\3\6\3\6\3\6\6\6u\n")
        buf.write("\6\r\6\16\6v\3\7\3\7\3\7\3\7\6\7}\n\7\r\7\16\7~\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0089\n\t\3\t\3\t\5\t\u008d")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0097\n\n\3\13")
        buf.write("\5\13\u009a\n\13\3\13\3\13\5\13\u009e\n\13\3\f\3\f\3\r")
        buf.write("\3\r\5\r\u00a4\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00b0\n\21\3\22\3\22\3\23\3\23\3")
        buf.write("\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\5\31\u00c3\n\31\3\32\3\32\3\32\6\32\u00c8\n")
        buf.write("\32\r\32\16\32\u00c9\3\33\3\33\3\33\6\33\u00cf\n\33\r")
        buf.write("\33\16\33\u00d0\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u00d9")
        buf.write("\n\34\3\35\3\35\3\35\5\35\u00de\n\35\3\36\3\36\3\36\6")
        buf.write("\36\u00e3\n\36\r\36\16\36\u00e4\3\37\3\37\3\37\6\37\u00ea")
        buf.write("\n\37\r\37\16\37\u00eb\3 \3 \3 \3 \3 \5 \u00f3\n \3!\5")
        buf.write("!\u00f6\n!\3!\3!\3!\3!\3\"\5\"\u00fd\n\"\3\"\5\"\u0100")
        buf.write("\n\"\3\"\5\"\u0103\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u010f\n\"\3#\3#\3#\3#\3#\5#\u0116\n#\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\5&\u0120\n&\3\'\3\'\5\'\u0124\n\'")
        buf.write("\3(\3(\3(\3(\5(\u012a\n(\3(\3(\5(\u012e\n(\3)\3)\3*\3")
        buf.write("*\3*\3*\5*\u0136\n*\3*\3*\5*\u013a\n*\5*\u013c\n*\3+\3")
        buf.write("+\3,\3,\3-\3-\3-\2\2.\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\13\4\2")
        buf.write("\6\6\22\22\3\2\24\25\4\2\7\7\30\30\4\2\b\b\31\31\4\2\t")
        buf.write("\t\32\32\4\2\n\n\33\33\4\2\13\13\34\34\4\2\24\24!!\4\2")
        buf.write("\20\20##\u0143\2\\\3\2\2\2\4`\3\2\2\2\6c\3\2\2\2\bn\3")
        buf.write("\2\2\2\np\3\2\2\2\fx\3\2\2\2\16\u0080\3\2\2\2\20\u008c")
        buf.write("\3\2\2\2\22\u0096\3\2\2\2\24\u0099\3\2\2\2\26\u009f\3")
        buf.write("\2\2\2\30\u00a1\3\2\2\2\32\u00a5\3\2\2\2\34\u00a7\3\2")
        buf.write("\2\2\36\u00a9\3\2\2\2 \u00af\3\2\2\2\"\u00b1\3\2\2\2$")
        buf.write("\u00b3\3\2\2\2&\u00b5\3\2\2\2(\u00b7\3\2\2\2*\u00b9\3")
        buf.write("\2\2\2,\u00bb\3\2\2\2.\u00bd\3\2\2\2\60\u00bf\3\2\2\2")
        buf.write("\62\u00c7\3\2\2\2\64\u00ce\3\2\2\2\66\u00d8\3\2\2\28\u00da")
        buf.write("\3\2\2\2:\u00e2\3\2\2\2<\u00e9\3\2\2\2>\u00f2\3\2\2\2")
        buf.write("@\u00f5\3\2\2\2B\u00fc\3\2\2\2D\u0110\3\2\2\2F\u0119\3")
        buf.write("\2\2\2H\u011b\3\2\2\2J\u011f\3\2\2\2L\u0123\3\2\2\2N\u012d")
        buf.write("\3\2\2\2P\u012f\3\2\2\2R\u013b\3\2\2\2T\u013d\3\2\2\2")
        buf.write("V\u013f\3\2\2\2X\u0141\3\2\2\2Z]\5\22\n\2[]\5\4\3\2\\")
        buf.write("Z\3\2\2\2\\[\3\2\2\2]\3\3\2\2\2^a\5\b\5\2_a\5\6\4\2`^")
        buf.write("\3\2\2\2`_\3\2\2\2a\5\3\2\2\2bd\5 \21\2cb\3\2\2\2cd\3")
        buf.write("\2\2\2de\3\2\2\2ef\5\24\13\2f\7\3\2\2\2go\5\n\6\2ho\5")
        buf.write("\f\7\2io\5\16\b\2jk\7\3\2\2kl\5\b\5\2lm\7\4\2\2mo\3\2")
        buf.write("\2\2ng\3\2\2\2nh\3\2\2\2ni\3\2\2\2nj\3\2\2\2o\t\3\2\2")
        buf.write("\2pt\5\20\t\2qr\5*\26\2rs\5\20\t\2su\3\2\2\2tq\3\2\2\2")
        buf.write("uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\13\3\2\2\2x|\5\20\t\2")
        buf.write("yz\5,\27\2z{\5\20\t\2{}\3\2\2\2|y\3\2\2\2}~\3\2\2\2~|")
        buf.write("\3\2\2\2~\177\3\2\2\2\177\r\3\2\2\2\u0080\u0081\5\20\t")
        buf.write("\2\u0081\u0082\5.\30\2\u0082\u0083\5\20\t\2\u0083\17\3")
        buf.write("\2\2\2\u0084\u008d\5\6\4\2\u0085\u0088\7\3\2\2\u0086\u0089")
        buf.write("\5\b\5\2\u0087\u0089\5\22\n\2\u0088\u0086\3\2\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\7\4\2\2")
        buf.write("\u008b\u008d\3\2\2\2\u008c\u0084\3\2\2\2\u008c\u0085\3")
        buf.write("\2\2\2\u008d\21\3\2\2\2\u008e\u008f\5\4\3\2\u008f\u0090")
        buf.write("\7\5\2\2\u0090\u0091\5\60\31\2\u0091\u0097\3\2\2\2\u0092")
        buf.write("\u0093\7\3\2\2\u0093\u0094\5\22\n\2\u0094\u0095\7\4\2")
        buf.write("\2\u0095\u0097\3\2\2\2\u0096\u008e\3\2\2\2\u0096\u0092")
        buf.write("\3\2\2\2\u0097\23\3\2\2\2\u0098\u009a\5\26\f\2\u0099\u0098")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u009e\5\30\r\2\u009c\u009e\5\34\17\2\u009d\u009b\3\2")
        buf.write("\2\2\u009d\u009c\3\2\2\2\u009e\25\3\2\2\2\u009f\u00a0")
        buf.write("\t\2\2\2\u00a0\27\3\2\2\2\u00a1\u00a3\5\32\16\2\u00a2")
        buf.write("\u00a4\5\36\20\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4\3\2\2")
        buf.write("\2\u00a4\31\3\2\2\2\u00a5\u00a6\7\23\2\2\u00a6\33\3\2")
        buf.write("\2\2\u00a7\u00a8\t\3\2\2\u00a8\35\3\2\2\2\u00a9\u00aa")
        buf.write("\7\26\2\2\u00aa\37\3\2\2\2\u00ab\u00b0\5$\23\2\u00ac\u00b0")
        buf.write("\5\"\22\2\u00ad\u00b0\5(\25\2\u00ae\u00b0\5&\24\2\u00af")
        buf.write("\u00ab\3\2\2\2\u00af\u00ac\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00b0!\3\2\2\2\u00b1\u00b2\t\4\2")
        buf.write("\2\u00b2#\3\2\2\2\u00b3\u00b4\t\5\2\2\u00b4%\3\2\2\2\u00b5")
        buf.write("\u00b6\t\6\2\2\u00b6\'\3\2\2\2\u00b7\u00b8\t\7\2\2\u00b8")
        buf.write(")\3\2\2\2\u00b9\u00ba\t\b\2\2\u00ba+\3\2\2\2\u00bb\u00bc")
        buf.write("\7\35\2\2\u00bc-\3\2\2\2\u00bd\u00be\7\36\2\2\u00be/\3")
        buf.write("\2\2\2\u00bf\u00c2\5\66\34\2\u00c0\u00c3\5\62\32\2\u00c1")
        buf.write("\u00c3\5\64\33\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3\2\2")
        buf.write("\2\u00c2\u00c3\3\2\2\2\u00c3\61\3\2\2\2\u00c4\u00c5\5")
        buf.write("*\26\2\u00c5\u00c6\5\66\34\2\u00c6\u00c8\3\2\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\63\3\2\2\2\u00cb\u00cc\5,\27")
        buf.write("\2\u00cc\u00cd\5\66\34\2\u00cd\u00cf\3\2\2\2\u00ce\u00cb")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\65\3\2\2\2\u00d2\u00d9\58\35\2\u00d3")
        buf.write("\u00d9\5@!\2\u00d4\u00d5\7\3\2\2\u00d5\u00d6\5\60\31\2")
        buf.write("\u00d6\u00d7\7\4\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d2\3")
        buf.write("\2\2\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9\67")
        buf.write("\3\2\2\2\u00da\u00dd\5> \2\u00db\u00de\5:\36\2\u00dc\u00de")
        buf.write("\5<\37\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de9\3\2\2\2\u00df\u00e0\5*\26\2\u00e0")
        buf.write("\u00e1\5> \2\u00e1\u00e3\3\2\2\2\u00e2\u00df\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5;\3\2\2\2\u00e6\u00e7\5,\27\2\u00e7\u00e8\5> \2")
        buf.write("\u00e8\u00ea\3\2\2\2\u00e9\u00e6\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec=")
        buf.write("\3\2\2\2\u00ed\u00f3\5B\"\2\u00ee\u00ef\7\3\2\2\u00ef")
        buf.write("\u00f0\58\35\2\u00f0\u00f1\7\4\2\2\u00f1\u00f3\3\2\2\2")
        buf.write("\u00f2\u00ed\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f3?\3\2\2")
        buf.write("\2\u00f4\u00f6\5D#\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\7\f\2\2\u00f8\u00f9")
        buf.write("\58\35\2\u00f9\u00fa\7\r\2\2\u00faA\3\2\2\2\u00fb\u00fd")
        buf.write("\5D#\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff")
        buf.write("\3\2\2\2\u00fe\u0100\5H%\2\u00ff\u00fe\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u0103\5J&\2\u0102\u0101")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104")
        buf.write("\u010e\5L\'\2\u0105\u0106\5P)\2\u0106\u0107\5N(\2\u0107")
        buf.write("\u010f\3\2\2\2\u0108\u0109\5R*\2\u0109\u010a\5V,\2\u010a")
        buf.write("\u010f\3\2\2\2\u010b\u010c\5T+\2\u010c\u010d\5X-\2\u010d")
        buf.write("\u010f\3\2\2\2\u010e\u0105\3\2\2\2\u010e\u0108\3\2\2\2")
        buf.write("\u010e\u010b\3\2\2\2\u010fC\3\2\2\2\u0110\u0111\7\16\2")
        buf.write("\2\u0111\u0112\7\37\2\2\u0112\u0115\7 \2\2\u0113\u0116")
        buf.write("\7\37\2\2\u0114\u0116\5F$\2\u0115\u0113\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\17\2")
        buf.write("\2\u0118E\3\2\2\2\u0119\u011a\t\t\2\2\u011aG\3\2\2\2\u011b")
        buf.write("\u011c\7\"\2\2\u011cI\3\2\2\2\u011d\u0120\5$\23\2\u011e")
        buf.write("\u0120\5\"\22\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2")
        buf.write("\2\u0120K\3\2\2\2\u0121\u0124\5\30\r\2\u0122\u0124\5\34")
        buf.write("\17\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124M\3")
        buf.write("\2\2\2\u0125\u012e\5\6\4\2\u0126\u0129\7\3\2\2\u0127\u012a")
        buf.write("\5\22\n\2\u0128\u012a\5\b\5\2\u0129\u0127\3\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7\4\2\2")
        buf.write("\u012c\u012e\3\2\2\2\u012d\u0125\3\2\2\2\u012d\u0126\3")
        buf.write("\2\2\2\u012eO\3\2\2\2\u012f\u0130\t\n\2\2\u0130Q\3\2\2")
        buf.write("\2\u0131\u013c\7\20\2\2\u0132\u013c\7#\2\2\u0133\u0135")
        buf.write("\7\7\2\2\u0134\u0136\7\20\2\2\u0135\u0134\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u013c\3\2\2\2\u0137\u0139\7\t\2\2")
        buf.write("\u0138\u013a\7\20\2\2\u0139\u0138\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u0131\3\2\2\2\u013b")
        buf.write("\u0132\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0137\3\2\2\2")
        buf.write("\u013cS\3\2\2\2\u013d\u013e\t\n\2\2\u013eU\3\2\2\2\u013f")
        buf.write("\u0140\7$\2\2\u0140W\3\2\2\2\u0141\u0142\7%\2\2\u0142")
        buf.write("Y\3\2\2\2$\\`cnv~\u0088\u008c\u0096\u0099\u009d\u00a3")
        buf.write("\u00af\u00c2\u00c9\u00d0\u00d8\u00dd\u00e4\u00eb\u00f2")
        buf.write("\u00f5\u00fc\u00ff\u0102\u010e\u0115\u011f\u0123\u0129")
        buf.write("\u012d\u0135\u0139\u013b")
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

        def refinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.RefinedExpressionConstraintContext,0)


        def unrefinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.UnrefinedExpressionConstraintContext,0)


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
            self.state = 90
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.refinedExpressionConstraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.unrefinedExpressionConstraint()
                pass


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
            self.state = 94
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.compoundExpressionConstraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
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
            self.state = 97
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.T__4) | (1 << ECLParser.T__5) | (1 << ECLParser.T__6) | (1 << ECLParser.T__7) | (1 << ECLParser.DESCENDANTOF) | (1 << ECLParser.DESCENDANTORSELFOF) | (1 << ECLParser.ANCESTOROF) | (1 << ECLParser.ANCESTORORSELFOF))) != 0):
                self.state = 96
                self.constraintOperator()


            self.state = 99
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
            self.state = 108
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.conjunctionExpressionConstraint()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.disjunctionExpressionConstraint()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.exclusionExpressionConstraint()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(ECLParser.T__0)
                self.state = 105
                self.compoundExpressionConstraint()
                self.state = 106
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
            self.state = 110
            self.subExpressionConstraint()
            self.state = 114 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.conjunction()
                self.state = 112
                self.subExpressionConstraint()
                self.state = 116 
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
            self.state = 118
            self.subExpressionConstraint()
            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.disjunction()
                self.state = 120
                self.subExpressionConstraint()
                self.state = 124 
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
            self.state = 126
            self.subExpressionConstraint()
            self.state = 127
            self.exclusion()
            self.state = 128
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
            self.state = 138
            token = self._input.LA(1)
            if token in [ECLParser.T__3, ECLParser.T__4, ECLParser.T__5, ECLParser.T__6, ECLParser.T__7, ECLParser.MEMBEROF, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.ANCESTOROF, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.simpleExpressionConstraint()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(ECLParser.T__0)
                self.state = 134
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.compoundExpressionConstraint()
                    pass

                elif la_ == 2:
                    self.state = 133
                    self.refinedExpressionConstraint()
                    pass


                self.state = 136
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

        def unrefinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.UnrefinedExpressionConstraintContext,0)


        def refinement(self):
            return self.getTypedRuleContext(ECLParser.RefinementContext,0)


        def refinedExpressionConstraint(self):
            return self.getTypedRuleContext(ECLParser.RefinedExpressionConstraintContext,0)


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
            self.state = 148
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.unrefinedExpressionConstraint()
                self.state = 141
                self.match(ECLParser.T__2)
                self.state = 142
                self.refinement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(ECLParser.T__0)
                self.state = 145
                self.refinedExpressionConstraint()
                self.state = 146
                self.match(ECLParser.T__1)
                pass


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
            self.state = 151
            _la = self._input.LA(1)
            if _la==ECLParser.T__3 or _la==ECLParser.MEMBEROF:
                self.state = 150
                self.memberOf()


            self.state = 155
            token = self._input.LA(1)
            if token in [ECLParser.SCTID]:
                self.state = 153
                self.conceptReference()

            elif token in [ECLParser.STAR, ECLParser.ANY]:
                self.state = 154
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
            self.state = 157
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
            self.state = 159
            self.conceptId()
            self.state = 161
            _la = self._input.LA(1)
            if _la==ECLParser.TERM:
                self.state = 160
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
            self.state = 163
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
            self.state = 165
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
            self.state = 167
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
            self.state = 173
            token = self._input.LA(1)
            if token in [ECLParser.T__5, ECLParser.DESCENDANTORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.descendantOrSelfOf()

            elif token in [ECLParser.T__4, ECLParser.DESCENDANTOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.descendantOf()

            elif token in [ECLParser.T__7, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.ancestorOrSelfOf()

            elif token in [ECLParser.T__6, ECLParser.ANCESTOROF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
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
            self.state = 175
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
            self.state = 177
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
            self.state = 179
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
            self.state = 181
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
            self.state = 183
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
            self.state = 185
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
            self.state = 187
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
            self.state = 189
            self.subRefinement()
            self.state = 192
            token = self._input.LA(1)
            if token in [ECLParser.T__8, ECLParser.AND]:
                self.state = 190
                self.conjunctionRefinementSet()
                pass
            elif token in [ECLParser.DISJUNCTION]:
                self.state = 191
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
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.conjunction()
                self.state = 195
                self.subRefinement()
                self.state = 199 
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
            self.state = 204 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 201
                self.disjunction()
                self.state = 202
                self.subRefinement()
                self.state = 206 
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
            self.state = 214
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.attributeSet()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.attributeGroup()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(ECLParser.T__0)
                self.state = 211
                self.refinement()
                self.state = 212
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
            self.state = 216
            self.subAttributeSet()
            self.state = 219
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 217
                self.conjunctionAttributeSet()

            elif la_ == 2:
                self.state = 218
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
            self.state = 224 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 221
                    self.conjunction()
                    self.state = 222
                    self.subAttributeSet()

                else:
                    raise NoViableAltException(self)
                self.state = 226 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
            self.state = 231 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 228
                    self.disjunction()
                    self.state = 229
                    self.subAttributeSet()

                else:
                    raise NoViableAltException(self)
                self.state = 233 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 240
            token = self._input.LA(1)
            if token in [ECLParser.T__4, ECLParser.T__5, ECLParser.T__11, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.REVERSEFLAG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.attribute()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(ECLParser.T__0)
                self.state = 237
                self.attributeSet()
                self.state = 238
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
            self.state = 243
            _la = self._input.LA(1)
            if _la==ECLParser.T__11:
                self.state = 242
                self.cardinality()


            self.state = 245
            self.match(ECLParser.T__9)
            self.state = 246
            self.attributeSet()
            self.state = 247
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
            self.state = 250
            _la = self._input.LA(1)
            if _la==ECLParser.T__11:
                self.state = 249
                self.cardinality()


            self.state = 253
            _la = self._input.LA(1)
            if _la==ECLParser.REVERSEFLAG:
                self.state = 252
                self.reverseFlag()


            self.state = 256
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ECLParser.T__4) | (1 << ECLParser.T__5) | (1 << ECLParser.DESCENDANTOF) | (1 << ECLParser.DESCENDANTORSELFOF))) != 0):
                self.state = 255
                self.attributeOperator()


            self.state = 258
            self.attributeName()
            self.state = 268
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 259
                self.expressionComparisonOperator()
                self.state = 260
                self.expressionConstraintValue()
                pass

            elif la_ == 2:
                self.state = 262
                self.numericComparisonOperator()
                self.state = 263
                self.numericValue()
                pass

            elif la_ == 3:
                self.state = 265
                self.stringComparisonOperator()
                self.state = 266
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
            self.state = 270
            self.match(ECLParser.T__11)
            self.state = 271
            self.match(ECLParser.NONNEGATIVEINTEGERVALUE)
            self.state = 272
            self.match(ECLParser.TO)
            self.state = 275
            token = self._input.LA(1)
            if token in [ECLParser.NONNEGATIVEINTEGERVALUE]:
                self.state = 273
                self.match(ECLParser.NONNEGATIVEINTEGERVALUE)

            elif token in [ECLParser.STAR, ECLParser.MANY]:
                self.state = 274
                self.many()

            else:
                raise NoViableAltException(self)

            self.state = 277
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
            self.state = 279
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
            self.state = 281
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
            self.state = 285
            token = self._input.LA(1)
            if token in [ECLParser.T__5, ECLParser.DESCENDANTORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.descendantOrSelfOf()

            elif token in [ECLParser.T__4, ECLParser.DESCENDANTOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
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
            self.state = 289
            token = self._input.LA(1)
            if token in [ECLParser.SCTID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.conceptReference()

            elif token in [ECLParser.STAR, ECLParser.ANY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
            self.state = 299
            token = self._input.LA(1)
            if token in [ECLParser.T__3, ECLParser.T__4, ECLParser.T__5, ECLParser.T__6, ECLParser.T__7, ECLParser.MEMBEROF, ECLParser.SCTID, ECLParser.STAR, ECLParser.ANY, ECLParser.DESCENDANTOF, ECLParser.DESCENDANTORSELFOF, ECLParser.ANCESTOROF, ECLParser.ANCESTORORSELFOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.simpleExpressionConstraint()

            elif token in [ECLParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.match(ECLParser.T__0)
                self.state = 295
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 293
                    self.refinedExpressionConstraint()
                    pass

                elif la_ == 2:
                    self.state = 294
                    self.compoundExpressionConstraint()
                    pass


                self.state = 297
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
            self.state = 301
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
            self.state = 313
            token = self._input.LA(1)
            if token in [ECLParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(ECLParser.T__13)

            elif token in [ECLParser.NEQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(ECLParser.NEQ)

            elif token in [ECLParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.match(ECLParser.T__4)
                self.state = 307
                _la = self._input.LA(1)
                if _la==ECLParser.T__13:
                    self.state = 306
                    self.match(ECLParser.T__13)



            elif token in [ECLParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.match(ECLParser.T__6)
                self.state = 311
                _la = self._input.LA(1)
                if _la==ECLParser.T__13:
                    self.state = 310
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
            self.state = 315
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
            self.state = 317
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
            self.state = 319
            self.match(ECLParser.STRINGVALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




