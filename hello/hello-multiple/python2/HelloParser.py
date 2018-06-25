# Generated from Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\5\22\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2")
        buf.write(u"\3\2\3\2\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\20\2\t\3\2\2")
        buf.write(u"\2\4\16\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2")
        buf.write(u"\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r")
        buf.write(u"\7\2\2\3\r\3\3\2\2\2\16\17\7\3\2\2\17\20\7\4\2\2\20\5")
        buf.write(u"\3\2\2\2\3\t")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'hello'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"ID", u"WS" ]

    RULE_prog = 0
    RULE_hi = 1

    ruleNames =  [ u"prog", u"hi" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    def __init__(self, input, output=sys.stdout):
        super(HelloParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(HelloParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

        def hi(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.HiContext)
            else:
                return self.getTypedRuleContext(HelloParser.HiContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_prog

        def enterRule(self, listener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = HelloParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.T__0:
                self.state = 4
                self.hi()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(HelloParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HiContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(HelloParser.HiContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_hi

        def enterRule(self, listener):
            if hasattr(listener, "enterHi"):
                listener.enterHi(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitHi"):
                listener.exitHi(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitHi"):
                return visitor.visitHi(self)
            else:
                return visitor.visitChildren(self)




    def hi(self):

        localctx = HelloParser.HiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(HelloParser.T__0)
            self.state = 13
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





