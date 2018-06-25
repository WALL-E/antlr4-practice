# Generated from CSV.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\6\2\r\n\2\r")
        buf.write("\2\16\2\16\3\3\3\3\3\4\3\4\3\4\7\4\26\n\4\f\4\16\4\31")
        buf.write("\13\4\3\4\5\4\34\n\4\3\4\3\4\3\5\3\5\3\5\5\5#\n\5\3\5")
        buf.write("\2\2\6\2\4\6\b\2\2\2%\2\n\3\2\2\2\4\20\3\2\2\2\6\22\3")
        buf.write("\2\2\2\b\"\3\2\2\2\n\f\5\4\3\2\13\r\5\6\4\2\f\13\3\2\2")
        buf.write("\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\3\3\2\2")
        buf.write("\2\20\21\5\6\4\2\21\5\3\2\2\2\22\27\5\b\5\2\23\24\7\3")
        buf.write("\2\2\24\26\5\b\5\2\25\23\3\2\2\2\26\31\3\2\2\2\27\25\3")
        buf.write("\2\2\2\27\30\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\32\34")
        buf.write("\7\4\2\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\36\7\5\2\2\36\7\3\2\2\2\37#\7\6\2\2 #\7\7\2\2!#\3\2\2")
        buf.write("\2\"\37\3\2\2\2\" \3\2\2\2\"!\3\2\2\2#\t\3\2\2\2\6\16")
        buf.write("\27\33\"")
        return buf.getvalue()


class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\r'", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "STRING" ]

    RULE_csvFile = 0
    RULE_hdr = 1
    RULE_row = 2
    RULE_field = 3

    ruleNames =  [ "csvFile", "hdr", "row", "field" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TEXT=4
    STRING=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class CsvFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hdr(self):
            return self.getTypedRuleContext(CSVParser.HdrContext,0)


        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_csvFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsvFile" ):
                listener.enterCsvFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsvFile" ):
                listener.exitCsvFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCsvFile" ):
                return visitor.visitCsvFile(self)
            else:
                return visitor.visitChildren(self)




    def csvFile(self):

        localctx = CSVParser.CsvFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csvFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.hdr()
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 9
                self.row()
                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSVParser.T__0) | (1 << CSVParser.T__1) | (1 << CSVParser.T__2) | (1 << CSVParser.TEXT) | (1 << CSVParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HdrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_hdr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHdr" ):
                listener.enterHdr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHdr" ):
                listener.exitHdr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHdr" ):
                return visitor.visitHdr(self)
            else:
                return visitor.visitChildren(self)




    def hdr(self):

        localctx = CSVParser.HdrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hdr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.FieldContext)
            else:
                return self.getTypedRuleContext(CSVParser.FieldContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.field()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVParser.T__0:
                self.state = 17
                self.match(CSVParser.T__0)
                self.state = 18
                self.field()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSVParser.T__1:
                self.state = 24
                self.match(CSVParser.T__1)


            self.state = 27
            self.match(CSVParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVParser.RULE_field

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TextContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXT(self):
            return self.getToken(CSVParser.TEXT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class EmptyContext(FieldContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVParser.FieldContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmpty" ):
                return visitor.visitEmpty(self)
            else:
                return visitor.visitChildren(self)



    def field(self):

        localctx = CSVParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_field)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVParser.TEXT]:
                localctx = CSVParser.TextContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(CSVParser.TEXT)
                pass
            elif token in [CSVParser.STRING]:
                localctx = CSVParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(CSVParser.STRING)
                pass
            elif token in [CSVParser.T__0, CSVParser.T__1, CSVParser.T__2]:
                localctx = CSVParser.EmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

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





