# Generated from JSON.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5&\n\5")
        buf.write("\f\5\16\5)\13\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\68\n\6\3\6\2\2\7\2\4\6\b\n\2\2\2>\2\f")
        buf.write("\3\2\2\2\4\33\3\2\2\2\6\35\3\2\2\2\b.\3\2\2\2\n\67\3\2")
        buf.write("\2\2\f\r\5\n\6\2\r\3\3\2\2\2\16\17\7\3\2\2\17\24\5\6\4")
        buf.write("\2\20\21\7\4\2\2\21\23\5\6\4\2\22\20\3\2\2\2\23\26\3\2")
        buf.write("\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26\24\3")
        buf.write("\2\2\2\27\30\7\5\2\2\30\34\3\2\2\2\31\32\7\3\2\2\32\34")
        buf.write("\7\5\2\2\33\16\3\2\2\2\33\31\3\2\2\2\34\5\3\2\2\2\35\36")
        buf.write("\7\f\2\2\36\37\7\6\2\2\37 \5\n\6\2 \7\3\2\2\2!\"\7\7\2")
        buf.write("\2\"\'\5\n\6\2#$\7\4\2\2$&\5\n\6\2%#\3\2\2\2&)\3\2\2\2")
        buf.write("\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7\b\2\2")
        buf.write("+/\3\2\2\2,-\7\7\2\2-/\7\b\2\2.!\3\2\2\2.,\3\2\2\2/\t")
        buf.write("\3\2\2\2\608\7\f\2\2\618\7\r\2\2\628\5\4\3\2\638\5\b\5")
        buf.write("\2\648\7\t\2\2\658\7\n\2\2\668\7\13\2\2\67\60\3\2\2\2")
        buf.write("\67\61\3\2\2\2\67\62\3\2\2\2\67\63\3\2\2\2\67\64\3\2\2")
        buf.write("\2\67\65\3\2\2\2\67\66\3\2\2\28\13\3\2\2\2\7\24\33\'.")
        buf.write("\67")
        return buf.getvalue()


class JSONParser ( Parser ):

    grammarFileName = "JSON.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_obj = 1
    RULE_pair = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames =  [ "json", "obj", "pair", "array", "value" ]

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
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class JsonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def getRuleIndex(self):
            return JSONParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = JSONParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_obj

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyObjContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObj" ):
                listener.enterEmptyObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObj" ):
                listener.exitEmptyObj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyObj" ):
                return visitor.visitEmptyObj(self)
            else:
                return visitor.visitChildren(self)


    class AnObjContext(ObjContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ObjContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.PairContext)
            else:
                return self.getTypedRuleContext(JSONParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObj" ):
                listener.enterAnObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObj" ):
                listener.exitAnObj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnObj" ):
                return visitor.visitAnObj(self)
            else:
                return visitor.visitChildren(self)



    def obj(self):

        localctx = JSONParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = JSONParser.AnObjContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(JSONParser.T__0)
                self.state = 13
                self.pair()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 14
                    self.match(JSONParser.T__1)
                    self.state = 15
                    self.pair()
                    self.state = 20
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 21
                self.match(JSONParser.T__2)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyObjContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(JSONParser.T__0)
                self.state = 24
                self.match(JSONParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PairContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_pair

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PairGroupContext(PairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.PairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)
        def value(self):
            return self.getTypedRuleContext(JSONParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPairGroup" ):
                listener.enterPairGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPairGroup" ):
                listener.exitPairGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPairGroup" ):
                return visitor.visitPairGroup(self)
            else:
                return visitor.visitChildren(self)



    def pair(self):

        localctx = JSONParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            localctx = JSONParser.PairGroupContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(JSONParser.STRING)
            self.state = 28
            self.match(JSONParser.T__3)
            self.state = 29
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSONParser.ValueContext)
            else:
                return self.getTypedRuleContext(JSONParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOfValues" ):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOfValues" ):
                listener.exitArrayOfValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayOfValues" ):
                return visitor.visitArrayOfValues(self)
            else:
                return visitor.visitChildren(self)


    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyArray" ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyArray" ):
                listener.exitEmptyArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyArray" ):
                return visitor.visitEmptyArray(self)
            else:
                return visitor.visitChildren(self)



    def array(self):

        localctx = JSONParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JSONParser.ArrayOfValuesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(JSONParser.T__4)
                self.state = 32
                self.value()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==JSONParser.T__1:
                    self.state = 33
                    self.match(JSONParser.T__1)
                    self.state = 34
                    self.value()
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 40
                self.match(JSONParser.T__5)
                pass

            elif la_ == 2:
                localctx = JSONParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(JSONParser.T__4)
                self.state = 43
                self.match(JSONParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JSONParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def obj(self):
            return self.getTypedRuleContext(JSONParser.ObjContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjValue" ):
                listener.enterObjValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjValue" ):
                listener.exitObjValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjValue" ):
                return visitor.visitObjValue(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JSONParser.STRING, 0)

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


    class ArrayValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(JSONParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayValue" ):
                return visitor.visitArrayValue(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JSONParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(JSONParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = JSONParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JSONParser.STRING]:
                localctx = JSONParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(JSONParser.STRING)
                pass
            elif token in [JSONParser.NUMBER]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(JSONParser.NUMBER)
                pass
            elif token in [JSONParser.T__0]:
                localctx = JSONParser.ObjValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.obj()
                pass
            elif token in [JSONParser.T__4]:
                localctx = JSONParser.ArrayValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.array()
                pass
            elif token in [JSONParser.T__6]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(JSONParser.T__6)
                pass
            elif token in [JSONParser.T__7]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.match(JSONParser.T__7)
                pass
            elif token in [JSONParser.T__8]:
                localctx = JSONParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(JSONParser.T__8)
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





