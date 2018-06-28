grammar CYMBOL;

root: chunk*;

chunk: stat
    | functionDecl
    ;

varDecl
    : varType ID ('=' expr)? ';'
    ;

varType
    :    'float' | 'int' | 'void'
    ;

functionDecl
    : varType ID '(' formalParameters? ')' block // "void f(int x) {...}"
    ;

formalParameters  // 形参
    : formalParameter (',' formalParameter)*
    ;

formalParameter
    : varType ID
    ;

block: '{' stat* '}';  // 语句组成的代码块，可以为空

stat:  block
    |  varDecl
    |  'if' expr 'then' stat ('else' stat)?
    |  'return' expr? ';'
    |  expr '=' expr ';'  // 赋值
    |  expr ';'  // 函数调用
    ;

exprList: expr (',' expr)*; //形参列表

expr: functioncall
    | expr '[' expr ']'
    | '-' expr
    | '!' expr
    | expr '*' expr
    | expr ('+'|'-') expr
    | expr '==' expr
    | ID
    | FLOAT
    | INT
    | '(' expr ')'
    ;

functioncall: ID '(' exprList ')'; //类似f(), f(x), f(1,2)的函数调用表达式


// LEXER

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

FLOAT
    : '-'? INT ('.' [0-9]+)?
    ;

INT
    : '0' | '-'? [1-9] [0-9]*
    ;

WS  
    : [ \t\u000C\r\n]+ -> skip
    ;
