
/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
grammar JSON;

json
   : value
   ;

obj
   : '{' pair (',' pair)* '}'      #AnObj
   | '{' '}'                       #EmptyObj
   ;

pair
   : STRING ':' value              #PairGroup
   ;

array
   : '[' value (',' value)* ']'    #ArrayOfValues
   | '[' ']'                       #EmptyArray
   ;

value
   : STRING    #String
   | NUMBER    #Atom
   | obj       #ObjValue
   | array     #ArrayValue
   | 'true'    #Atom
   | 'false'   #Atom
   | 'null'    #Atom
   ;


STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;


fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;


fragment HEX
   : [0-9a-fA-F]
   ;


fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;


NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;
