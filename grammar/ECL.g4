grammar ECL;

// expressionConstraint = ws ( refinedExpressionConstraint / unrefinedExpressionConstraint ) ws
expressionConstraint : refinedExpressionConstraint
					 | unrefinedExpressionConstraint
					 ;

// unrefinedExpressionConstraint = compoundExpressionConstraint / simpleExpressionConstraint
unrefinedExpressionConstraint : compoundExpressionConstraint
							  | simpleExpressionConstraint
							  ;

// simpleExpressionConstraint =  [constraintOperator ws] focusConcept
simpleExpressionConstraint : constraintOperator? focusConcept ;


// compoundExpressionConstraint = conjunctionExpressionConstraint /
//        disjunctionExpressionConstraint / exclusionExpressionConstraint /
//        "(" ws compoundExpressionConstraint ws ")"
compoundExpressionConstraint : conjunctionExpressionConstraint
                             | disjunctionExpressionConstraint
                             | exclusionExpressionConstraint
                             | '(' compoundExpressionConstraint ')'
                             ;

// conjunctionExpressionConstraint = subExpressionConstraint 1*(ws conjunction ws subExpressionConstraint)
conjunctionExpressionConstraint : subExpressionConstraint (conjunction subExpressionConstraint)+ ;

// disjunctionExpressionConstraint = subExpressionConstraint 1*(ws disjunction ws subExpressionConstraint)
disjunctionExpressionConstraint : subExpressionConstraint (disjunction subExpressionConstraint)+ ;

// exclusionExpressionConstraint = subExpressionConstraint ws exclusion ws 	subExpressionConstraint
exclusionExpressionConstraint : subExpressionConstraint exclusion subExpressionConstraint ;

//subExpressionConstraint = simpleExpressionConstraint /
// 	"(" ws (compoundExpressionConstraint / refinedExpressionConstraint) ws ")"
subExpressionConstraint : simpleExpressionConstraint
					    | '(' (compoundExpressionConstraint | refinedExpressionConstraint) ')'
					    ;

// refinedExpressionConstraint = unrefinedExpressionConstraint ws ":" ws refinement / "(" ws refinedExpressionConstraint ws ")"
refinedExpressionConstraint : unrefinedExpressionConstraint ':' refinement
						    | '(' refinedExpressionConstraint ')'
						    ;

// focusConcept = [ memberOf ws] (conceptReference / wildCard)
focusConcept : memberOf? (conceptReference | wildCard) ;

// ws = *( SP / HTAB / CR / LF )  ; optional white space
WS : [ \n\r\t]+ -> skip;

// memberOf = "^" /  ("m"/"M") ("e"/"E") ("m"/"M") ("b"/"B") ("e"/"E") ("r"/"R") ("o"/"O") 	("f"/"F")
memberOf : '^' | MEMBEROF ;
MEMBEROF : M E M B E R O F ;

// conceptReference = conceptId [ws "|" ws term ws "|"]
// Note: we've included the bars in term because the lexer gets complicated otherwise
conceptReference : conceptId ( term )? ;

// conceptId = sctId
conceptId : SCTID ;

// sctId = digitNonZero 5*17( digit )
// The 5 to 17 digits will be covered in the code
SCTID : DIGITNONZERO DIGIT+ ;

// wildCard = "*" / ( ("a"/"A") ("n"/"N") ("y"/"Y") )
wildCard : STAR | ANY ;
STAR : '*' ;
ANY : A N Y ;

// term = 1*nonwsNonPipe *( 1*SP 1*nonwsNonPipe )
// Eliminating nonwsNonPipe eliminates the need for special UTF characters below
term : TERM ;
TERM : '|' WS? ~[ |]+ (' ' ~[ |]+)* WS? '|';

// COMMENT to allow annotation and test data
COMMENT : '//' ~[\r\n]* -> skip ;


// constraintOperator = descendantOrSelfOf / descendantOf /  ancestorOrSelfOf / ancestorOf
constraintOperator : descendantOrSelfOf
                   | descendantOf
                   | ancestorOrSelfOf
                   | ancestorOf
                   ;

// descendantOf = "<" / ( ("d"/"D") ("e"/"E") ("s"/"S") ("c"/"C") ("e"/"E") ("n"/"N") ("d"/"D") ("a"/"A") 	("n"/"N") ("t"/"T") ("o"/"O") ("f"/"F")  mws )
descendantOf : '<' | DESCENDANTOF ;
DESCENDANTOF : '<' | D E S C E N D A N T O F ;

// descendantOrSelfOf = "<<" / ( ("d"/"D") ("e"/"E") ("s"/"S") ("c"/"C") ("e"/"E") ("n"/"N") ("d"/"D") 	("a"/"A") ("n"/"N") ("t"/"T") ("o"/"O") ("r"/"R") ("s"/"S") ("e"/"E") ("l"/"L") ("f"/"F") 		 ("o"/"O") ("f"/"F")  mws )
descendantOrSelfOf : '<<' | DESCENDANTORSELFOF ;
DESCENDANTORSELFOF : D E S C E N D A N T O R S E L F O F ;

// ancestorOf = ">" / ( ("a"/"A") ("n"/"N") ("c"/"C") ("e"/"E") ("s"/"S") ("t"/"T") ("o"/"O")  	("r"/"R") ("o"/"O") ("f"/"F")  mws )
ancestorOf : '>' | ANCESTOROF ;
ANCESTOROF : A N C E S T O R O F ;

// ancestorOrSelfOf = ">>" / ( ("a"/"A") ("n"/"N") ("c"/"C") ("e"/"E") ("s"/"S") ("t"/"T") ("o"/"O") 	("r"/"R") ("o"/"O") ("r"/"R") ("s"/"S") ("e"/"E") ("l"/"L") ("f"/"F") ("o"/"O") ("f"/"F")  	mws )
ancestorOrSelfOf :  '>>' | ANCESTORORSELFOF ;
ANCESTORORSELFOF : A N C E S T O R O R S E L F O F ;

// conjunction = (("a"/"A") ("n"/"N") ("d"/"D") mws) / ","
conjunction : ',' | AND ;
AND : A N D ;

// disjunction = ("o"/"O") ("r"/"R") mws
disjunction : DISJUNCTION;
DISJUNCTION : O R ;

// exclusion = ("m"/"M") ("i"/"I") ("n"/"N") ("u"/"U") ("s"/"S") mws
exclusion : MINUS ;
MINUS : M I N U S ;

// refinement = subRefinement ws [conjunctionRefinementSet / disjunctionRefinementSet]
refinement : subRefinement (conjunctionRefinementSet | disjunctionRefinementSet)? ;

// conjunctionRefinementSet = 1*(ws conjunction ws subRefinement)
conjunctionRefinementSet : (conjunction subRefinement)+ ;

// disjunctionRefinementSet = 1*(ws disjunction ws subRefinement)
disjunctionRefinementSet : (disjunction subRefinement)+ ;

// subRefinement = attributeSet / attributeGroup / "(" ws refinement ws ")"
subRefinement : attributeSet
              | attributeGroup
              | '(' refinement ')'
              ;

// attributeSet = subAttributeSet ws [conjunctionAttributeSet / disjunctionAttributeSet]
attributeSet : subAttributeSet (conjunctionAttributeSet | disjunctionAttributeSet)? ;

// conjunctionAttributeSet = 1*(ws conjunction ws subAttributeSet)
conjunctionAttributeSet : (conjunction subAttributeSet)+ ;

// disjunctionAttributeSet = 1*(ws disjunction ws subAttributeSet)
disjunctionAttributeSet : (disjunction subAttributeSet)+ ;

// subAttributeSet = attribute / "(" ws attributeSet ws ")"
subAttributeSet : attribute
                | '(' attributeSet ')'
                ;

// attributeGroup = [cardinality ws] "{" ws attributeSet ws "}"
attributeGroup : cardinality? '{' attributeSet '}' ;


// attribute = [cardinality ws] [reverseFlag ws] [attributeOperator ws] attributeName ws
//             (expressionComparisonOperator ws expressionConstraintValue /
//              numericComparisonOperator ws numericValue /
//  			stringComparisonOperator ws stringValue )
attribute : cardinality? reverseFlag? attributeOperator? attributeName
          ( expressionComparisonOperator expressionConstraintValue
          | numericComparisonOperator numericValue
          | stringComparisonOperator stringValue )
          ;

// cardinality = "[" nonNegativeIntegerValue to (nonNegativeIntegerValue / many) "]"
cardinality : '[' NONNEGATIVEINTEGERVALUE TO (NONNEGATIVEINTEGERVALUE | many) ']' ;
NONNEGATIVEINTEGERVALUE : '0' | DIGITNONZERO DIGIT* ;

// to = ".." / (mws ("t"/"T") ("o"/"O") mws)
TO	:	'..' | (T O) ;

// many = "*" / ( ("m"/"M") ("a"/"A") ("n"/"N") ("y"/"Y"))
many : '*' | MANY ;
MANY : (M A N Y) ;

// reverseFlag =  ( ("r"/"R") ("e"/"E") ("v"/"V") ("e"/"E") ("r"/"R") ("s"/"S") ("e"/"E") ("o"/"O") ("f"/"F")) / "R"
reverseFlag : REVERSEFLAG ;
REVERSEFLAG : (R E V E R S E O F) | 'R'  ;

// attributeOperator = descendantOrSelfOf / descendantOf
attributeOperator : descendantOrSelfOf | descendantOf ;

// attributeName = conceptReference / wildCard
attributeName : conceptReference | wildCard ;

// expressionConstraintValue = simpleExpressionConstraint / "(" ws (refinedExpressionConstraint /
//                              compoundExpressionConstraint) ws ")"
expressionConstraintValue : simpleExpressionConstraint
                          | '(' (refinedExpressionConstraint | compoundExpressionConstraint) ')'
                          ;

// expressionComparisonOperator = "=" / "!=" / ("n"/"N") ("o"/"O") ("t"/"T") ws "=" / "<>"
expressionComparisonOperator : '=' | NEQ ;
NEQ : '!=' | (N O T ' ' '=') | '<>' ;

// numericComparisonOperator = "=" / "!=" / ("n"/"N") ("o"/"O") ("t"/"T") ws "=" / "<>" / "<=" / 	"<" / ">=" / ">"
numericComparisonOperator : '=' | NEQ | '<' '='? | '>' '='? ;


// stringComparisonOperator = "=" / "!=" / ("n"/"N") ("o"/"O") ("t"/"T") ws "=" / "<>"
stringComparisonOperator : '=' | NEQ ;

// numericValue =  "#" ( decimalValue / integerValue)
// integerValue = ( ["-"/"+"] digitNonZero *digit ) / zero
// decimalValue = integerValue "." 1*digit
numericValue : NUMERICVALUE ;
NUMERICVALUE : '#' [-+]? [1-9] [0-9]* ('.' [0-9]+)? ;

// stringValue =  QM 1*(anyNonEscapedChar / escapedChar) QM
stringValue : STRINGVALUE ;
STRINGVALUE : '"' ( ESCAPEDCHAR | .)*? '"' ;
ESCAPEDCHAR : '\\\\' | '\\"' ;


// nonNegativeIntegerValue = (digitNonZero *digit ) / zero
DIGITNONZERO : [1-9] ;
DIGIT : '0' | DIGITNONZERO ;


// mws = 1*( SP / HTAB / CR / LF )  ; mandatory white space
// TODO: What do we do with mws?

// http://techbus.safaribooksonline.com/book/programming/9781941222621/firstchapter#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE5NDEyMjI2MjElMkZmXzAwNDNfaHRtbCZxdWVyeT0=
// nonwsNonPipe = %x21-7B / %x7D-7E / UTF8-2 / UTF8-3 / UTF8-4
// None of the below is needed because TERM is a not X format

// UTF8-2 = %xC2-DF UTF8-ta˝il
// UTF82 : [\u00C2-\u00DF] UTF8TAIL ;

// UTF8-3 = %xE0 %xA0-BF UTF8-tail / %xE1-EC 2(UTF8-tail) / %xED %x80-9F UTF8-tail / %xEE-EF 2(UTF8-tail)
// UTF83 : [\u00E0] [\u00A0-\u00BF] UTF8TAIL
//                | [\u00e1-\u00eC] UTF8TAIL UTF8TAIL
//                | [\u00ED] [\u0080-\u009F] UTF8TAIL
//                | [\u00EE-\u00EF] UTF8TAIL UTF8TAIL
//                ;

// UTF8-4 = %xF0 %x90-BF 2(UTF8-tail) / %xF1-F3 3(UTF8-tail) / %xF4 %x80-8F 2(UTF8-tail)
// UTF84 : [\u00F0] [\u0090-\u00BF] UTF8TAIL UTF8TAIL
// 			   | [\u00F1-\u00F3] UTF8TAIL UTF8TAIL UTF8TAIL
// 			   | [\u00F4] [\u0080-\u008F] UTF8TAIL UTF8TAIL
// 			   ;

// UTF8-tail = %x80-BF
// UTF8TAIL : [\u0080-\u00BF] ;

// anyNonEscapedChar = HTAB / CR / LF / %x20-21 / %x23-5B / %x5D-7E / UTF8-2 / UTF8-3 / UTF8-4
// Not needed.  Parser alternative used above
fragment A:('a'|'A');
fragment B:('b'|'B');
fragment C:('c'|'C');
fragment D:('d'|'D');
fragment E:('e'|'E');
fragment F:('f'|'F');
fragment G:('g'|'G');
fragment H:('h'|'H');
fragment I:('i'|'I');
fragment J:('j'|'J');
fragment K:('k'|'K');
fragment L:('l'|'L');
fragment M:('m'|'M');
fragment N:('n'|'N');
fragment O:('o'|'O');
fragment P:('p'|'P');
fragment Q:('q'|'Q');
fragment R:('r'|'R');
fragment S:('s'|'S');
fragment T:('t'|'T');
fragment U:('u'|'U');
fragment V:('v'|'V');
fragment W:('w'|'W');
fragment X:('x'|'X');
fragment Y:('y'|'Y');
fragment Z:('z'|'Z');

