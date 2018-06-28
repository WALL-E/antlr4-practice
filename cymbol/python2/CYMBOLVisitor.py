# Generated from CYMBOL.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by CYMBOLParser.

class CYMBOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CYMBOLParser#root.
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#chunk.
    def visitChunk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#varDecl.
    def visitVarDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#varType.
    def visitVarType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#functionDecl.
    def visitFunctionDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#formalParameters.
    def visitFormalParameters(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#formalParameter.
    def visitFormalParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#exprList.
    def visitExprList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#functioncall.
    def visitFunctioncall(self, ctx):
        return self.visitChildren(ctx)


