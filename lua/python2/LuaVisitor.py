# Generated from Lua.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by LuaParser.

class LuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LuaParser#chunk.
    def visitChunk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat1.
    def visitStat1(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat2.
    def visitStat2(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat3.
    def visitStat3(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat4.
    def visitStat4(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat5.
    def visitStat5(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat6.
    def visitStat6(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat7.
    def visitStat7(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat8.
    def visitStat8(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat9.
    def visitStat9(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat10.
    def visitStat10(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat11.
    def visitStat11(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat12.
    def visitStat12(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat13.
    def visitStat13(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat14.
    def visitStat14(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#Stat15.
    def visitStat15(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#retstat.
    def visitRetstat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#label.
    def visitLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcname.
    def visitFuncname(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varlist.
    def visitVarlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#namelist.
    def visitNamelist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#explist.
    def visitExplist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#exp.
    def visitExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#prefixexp.
    def visitPrefixexp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functioncall.
    def visitFunctioncall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varOrExp.
    def visitVarOrExp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#var.
    def visitVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#varSuffix.
    def visitVarSuffix(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#nameAndArgs.
    def visitNameAndArgs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#args.
    def visitArgs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#functiondef.
    def visitFunctiondef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#funcbody.
    def visitFuncbody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#parlist.
    def visitParlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#tableconstructor.
    def visitTableconstructor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldlist.
    def visitFieldlist(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#field.
    def visitField(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#fieldsep.
    def visitFieldsep(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorOr.
    def visitOperatorOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorAnd.
    def visitOperatorAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorComparison.
    def visitOperatorComparison(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorStrcat.
    def visitOperatorStrcat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorAddSub.
    def visitOperatorAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorMulDivMod.
    def visitOperatorMulDivMod(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorBitwise.
    def visitOperatorBitwise(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorUnary.
    def visitOperatorUnary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#operatorPower.
    def visitOperatorPower(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#number.
    def visitNumber(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LuaParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


