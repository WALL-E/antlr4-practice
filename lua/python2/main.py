#!/usr/bin/env python

import sys

from antlr4 import *
from LuaLexer import LuaLexer
from LuaListener import LuaListener
from LuaParser import LuaParser


class Graph():
    def __init__(self):
        self.nodes = set()
        self.edges = list()

    def edge(self, src, dst):
        edge = {"src": src, "dst": dst}
        self.edges.append(edge)

    def toDot(self):
        buf = []
        buf.append("digraph G {\n")
        buf.append("  ranksep=.75;\n")
        buf.append("  edge [arrowsize=.5]\n")
        buf.append("  node [shape=circle, fontname=\"ArialNarrow\",\n")
        buf.append("        fontsize=18, fixedsize=false, height=2.5];\n")
        buf.append("  ")

        for node in self.nodes:
            buf.append("\"%s\"" %(node))
            buf.append(";")
        buf.append("\n")

        for edge in self.edges:
            if edge["src"] is None:
                continue
            buf.append("  ");
            buf.append("\"%s\""%(edge["src"]));
            buf.append(" -> ");
            buf.append("\"%s\""%(edge["dst"]));
            buf.append("\n");

        buf.append("}\n");

        return "".join(buf)


class LuaPrintListener(LuaListener):
    def __init__(self):
        self.graph = Graph()
        self.currentFuntionName = None

    def exitFunctioncall(self, ctx):
        funcName = ctx.varOrExp().getText()
        self.graph.edge(self.currentFuntionName, funcName);

    def enterStat13(self, ctx):
        self.currentFuntionName = ctx.funcname().getText()
        self.graph.nodes.add(self.currentFuntionName)

def main():
    lexer = LuaLexer(FileStream("./t.lua"))
    stream = CommonTokenStream(lexer)
    parser = LuaParser(stream)
    tree = parser.chunk()

    listener = LuaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(listener.graph.toDot())

if __name__ == '__main__':
    main()

