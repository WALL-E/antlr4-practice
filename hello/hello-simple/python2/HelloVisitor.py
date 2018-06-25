# Generated from Hello.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by HelloParser.

class HelloVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloParser#hi.
    def visitHi(self, ctx):
        return self.visitChildren(ctx)


