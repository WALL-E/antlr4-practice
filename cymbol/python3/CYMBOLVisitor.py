# Generated from CYMBOL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CYMBOLParser import CYMBOLParser
else:
    from CYMBOLParser import CYMBOLParser

# This class defines a complete generic visitor for a parse tree produced by CYMBOLParser.

class CYMBOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CYMBOLParser#root.
    def visitRoot(self, ctx:CYMBOLParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#chunk.
    def visitChunk(self, ctx:CYMBOLParser.ChunkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#varDecl.
    def visitVarDecl(self, ctx:CYMBOLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#varType.
    def visitVarType(self, ctx:CYMBOLParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#functionDecl.
    def visitFunctionDecl(self, ctx:CYMBOLParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#formalParameters.
    def visitFormalParameters(self, ctx:CYMBOLParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#formalParameter.
    def visitFormalParameter(self, ctx:CYMBOLParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#block.
    def visitBlock(self, ctx:CYMBOLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#stat.
    def visitStat(self, ctx:CYMBOLParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#exprList.
    def visitExprList(self, ctx:CYMBOLParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#expr.
    def visitExpr(self, ctx:CYMBOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CYMBOLParser#functioncall.
    def visitFunctioncall(self, ctx:CYMBOLParser.FunctioncallContext):
        return self.visitChildren(ctx)



del CYMBOLParser