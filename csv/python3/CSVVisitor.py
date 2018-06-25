# Generated from CSV.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSVParser import CSVParser
else:
    from CSVParser import CSVParser

# This class defines a complete generic visitor for a parse tree produced by CSVParser.

class CSVVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVParser#csvFile.
    def visitCsvFile(self, ctx:CSVParser.CsvFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#hdr.
    def visitHdr(self, ctx:CSVParser.HdrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#row.
    def visitRow(self, ctx:CSVParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#text.
    def visitText(self, ctx:CSVParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#string.
    def visitString(self, ctx:CSVParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVParser#empty.
    def visitEmpty(self, ctx:CSVParser.EmptyContext):
        return self.visitChildren(ctx)



del CSVParser