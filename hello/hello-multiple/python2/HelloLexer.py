# Generated from Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\5\33\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\3\6\3\21\n\3\r\3\16\3\22\3\4\6\4\26\n\4\r\4\16")
        buf.write(u"\4\27\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\4\3\2c|\5\2\13\f")
        buf.write(u"\17\17\"\"\2\34\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3")
        buf.write(u"\t\3\2\2\2\5\20\3\2\2\2\7\25\3\2\2\2\t\n\7j\2\2\n\13")
        buf.write(u"\7g\2\2\13\f\7n\2\2\f\r\7n\2\2\r\16\7q\2\2\16\4\3\2\2")
        buf.write(u"\2\17\21\t\2\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3")
        buf.write(u"\2\2\2\22\23\3\2\2\2\23\6\3\2\2\2\24\26\t\3\2\2\25\24")
        buf.write(u"\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30")
        buf.write(u"\31\3\2\2\2\31\32\b\4\2\2\32\b\3\2\2\2\5\2\22\27\3\b")
        buf.write(u"\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'hello'" ]

    symbolicNames = [ u"<INVALID>",
            u"ID", u"WS" ]

    ruleNames = [ u"T__0", u"ID", u"WS" ]

    grammarFileName = u"Hello.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(HelloLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


