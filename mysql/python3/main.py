#!/usr/bin/env python3

import sys

from antlr4 import *
from MySqlLexer import MySqlLexer
from MySqlParser import MySqlParser
from MySqlParserListener import MySqlParserListener


class PrintListener(MySqlParserListener):
    def exitSelectElements(self, ctx):
        print("exit SelectElements")

    def exitTableSources(self, ctx):
        print("exit TableSources")

def main():

    lexer = MySqlLexer(FileStream("sqls.txt"))
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    root = parser.root()

    printer = PrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()

