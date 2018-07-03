# Generated from Cymbol.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by CymbolParser.

class CymbolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CymbolParser#root.
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#varDecl.
    def visitVarDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#varType.
    def visitVarType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#functionDecl.
    def visitFunctionDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#formalParameters.
    def visitFormalParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#formalParameter.
    def visitFormalParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Call.
    def visitCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Not.
    def visitNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Mult.
    def visitMult(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Equal.
    def visitEqual(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Var.
    def visitVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Index.
    def visitIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Negate.
    def visitNegate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Int.
    def visitInt(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#exprList.
    def visitExprList(self, ctx):
        return self.visitChildren(ctx)


