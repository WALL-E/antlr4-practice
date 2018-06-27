# Generated from JSON.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSONParser import JSONParser
else:
    from JSONParser import JSONParser

# This class defines a complete generic visitor for a parse tree produced by JSONParser.

class JSONVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSONParser#json.
    def visitJson(self, ctx:JSONParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#AnObj.
    def visitAnObj(self, ctx:JSONParser.AnObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#EmptyObj.
    def visitEmptyObj(self, ctx:JSONParser.EmptyObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#PairGroup.
    def visitPairGroup(self, ctx:JSONParser.PairGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ArrayOfValues.
    def visitArrayOfValues(self, ctx:JSONParser.ArrayOfValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#EmptyArray.
    def visitEmptyArray(self, ctx:JSONParser.EmptyArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#String.
    def visitString(self, ctx:JSONParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#Atom.
    def visitAtom(self, ctx:JSONParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ObjValue.
    def visitObjValue(self, ctx:JSONParser.ObjValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSONParser#ArrayValue.
    def visitArrayValue(self, ctx:JSONParser.ArrayValueContext):
        return self.visitChildren(ctx)



del JSONParser