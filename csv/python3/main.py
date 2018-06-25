#!/usr/bin/env python3

import sys

from antlr4 import *
from CSVLexer import CSVLexer
from CSVListener import CSVListener
from CSVParser import CSVParser
import sys

class CSVPrintListener(CSVListener):
    def __init__(self):
        self.EMPTY = ""
        self.header = []
        self.rows = []
        self.currentRowFieldValues = []

    def enterString(self, ctx):
        # print("String: %s" % ctx.STRING().getText())
        pass

    def enterText(self, ctx):
        # print("Text: %s" % ctx.TEXT().getText())
        pass

    def exitString(self, ctx):
        self.currentRowFieldValues.append(ctx.STRING().getText());

    def exitText(self, ctx):
        self.currentRowFieldValues.append(ctx.TEXT().getText())

    def exitEmpty(self, ctx):
        self.currentRowFieldValues.append(self.EMPTY)

    def exitHdr(self, ctx):
        self.header = self.currentRowFieldValues.copy()

    def enterRow(self, ctx):
        self.currentRowFieldValues = []

    def exitRow(self, ctx):
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_hdr:
            return;

        m = {}
        for i in range(len(self.currentRowFieldValues)):
            m[self.header[i]] = self.currentRowFieldValues[i]
        self.rows.append(m)


def main():
    lexer = CSVLexer(FileStream("./t.csv"))
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    printer = CSVPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    print(printer.rows)

if __name__ == '__main__':
    main()

