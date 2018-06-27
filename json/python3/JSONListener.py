# Generated from JSON.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete listener for a parse tree produced by JSONParser.
class JSONListener(ParseTreeListener):

    # Enter a parse tree produced by JSONParser#json.
    def enterJson(self, ctx:JSONParser.JsonContext):
        pass

    # Exit a parse tree produced by JSONParser#json.
    def exitJson(self, ctx:JSONParser.JsonContext):
        pass


    # Enter a parse tree produced by JSONParser#AnObj.
    def enterAnObj(self, ctx:JSONParser.AnObjContext):
        pass

    # Exit a parse tree produced by JSONParser#AnObj.
    def exitAnObj(self, ctx:JSONParser.AnObjContext):
        pass


    # Enter a parse tree produced by JSONParser#EmptyObj.
    def enterEmptyObj(self, ctx:JSONParser.EmptyObjContext):
        pass

    # Exit a parse tree produced by JSONParser#EmptyObj.
    def exitEmptyObj(self, ctx:JSONParser.EmptyObjContext):
        pass


    # Enter a parse tree produced by JSONParser#PairGroup.
    def enterPairGroup(self, ctx:JSONParser.PairGroupContext):
        pass

    # Exit a parse tree produced by JSONParser#PairGroup.
    def exitPairGroup(self, ctx:JSONParser.PairGroupContext):
        pass


    # Enter a parse tree produced by JSONParser#ArrayOfValues.
    def enterArrayOfValues(self, ctx:JSONParser.ArrayOfValuesContext):
        pass

    # Exit a parse tree produced by JSONParser#ArrayOfValues.
    def exitArrayOfValues(self, ctx:JSONParser.ArrayOfValuesContext):
        pass


    # Enter a parse tree produced by JSONParser#EmptyArray.
    def enterEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        pass

    # Exit a parse tree produced by JSONParser#EmptyArray.
    def exitEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        pass


    # Enter a parse tree produced by JSONParser#String.
    def enterString(self, ctx:JSONParser.StringContext):
        pass

    # Exit a parse tree produced by JSONParser#String.
    def exitString(self, ctx:JSONParser.StringContext):
        pass


    # Enter a parse tree produced by JSONParser#Atom.
    def enterAtom(self, ctx:JSONParser.AtomContext):
        pass

    # Exit a parse tree produced by JSONParser#Atom.
    def exitAtom(self, ctx:JSONParser.AtomContext):
        pass


    # Enter a parse tree produced by JSONParser#ObjValue.
    def enterObjValue(self, ctx:JSONParser.ObjValueContext):
        pass

    # Exit a parse tree produced by JSONParser#ObjValue.
    def exitObjValue(self, ctx:JSONParser.ObjValueContext):
        pass


    # Enter a parse tree produced by JSONParser#ArrayValue.
    def enterArrayValue(self, ctx:JSONParser.ArrayValueContext):
        pass

    # Exit a parse tree produced by JSONParser#ArrayValue.
    def exitArrayValue(self, ctx:JSONParser.ArrayValueContext):
        pass


