# Generated from Cymbol.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CymbolParser import CymbolParser
else:
    from CymbolParser import CymbolParser

# This class defines a complete generic visitor for a parse tree produced by CymbolParser.

class CymbolVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CymbolParser#root.
    def visitRoot(self, ctx:CymbolParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#varDecl.
    def visitVarDecl(self, ctx:CymbolParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#varType.
    def visitVarType(self, ctx:CymbolParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#functionDecl.
    def visitFunctionDecl(self, ctx:CymbolParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#formalParameters.
    def visitFormalParameters(self, ctx:CymbolParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#formalParameter.
    def visitFormalParameter(self, ctx:CymbolParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#block.
    def visitBlock(self, ctx:CymbolParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#stat.
    def visitStat(self, ctx:CymbolParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Call.
    def visitCall(self, ctx:CymbolParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Not.
    def visitNot(self, ctx:CymbolParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Mult.
    def visitMult(self, ctx:CymbolParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#AddSub.
    def visitAddSub(self, ctx:CymbolParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Equal.
    def visitEqual(self, ctx:CymbolParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Var.
    def visitVar(self, ctx:CymbolParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Parens.
    def visitParens(self, ctx:CymbolParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Index.
    def visitIndex(self, ctx:CymbolParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Negate.
    def visitNegate(self, ctx:CymbolParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#Int.
    def visitInt(self, ctx:CymbolParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CymbolParser#exprList.
    def visitExprList(self, ctx:CymbolParser.ExprListContext):
        return self.visitChildren(ctx)



del CymbolParser