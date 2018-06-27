
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.antlr.v4.runtime.misc.*;
import java.io.FileInputStream;
import java.io.InputStream;

import java.util.*;


class Graph {
    Set<String> nodes = new OrderedHashSet<String>();
    MultiMap<String, String> edges = new MultiMap<String, String>();

    public void edge(String src, String dst) {
        edges.map(src, dst);
    }

    public String toDot() {
        StringBuilder buf = new StringBuilder();
        buf.append("digraph G {\n");
        buf.append("  ranksep=.25;\n");
        buf.append("  edge [arrowsize=.5]\n");
        buf.append("  node [shape=circle, fontname=\"ArialNarrow\", \n");
        buf.append("        fontsize=12, fixedsize=true, height=.45];\n");
        buf.append("  ");

        for (String node : nodes) {
            buf.append(node);
            buf.append(";");
        }
        buf.append("\n");

        for (String src : edges.keySet()) {
            for (String dst : edges.get(src)) {
                buf.append("  ");
                buf.append(src);
                buf.append(" -> ");
                buf.append(dst);
                buf.append("\n");
            }
        }
        
        buf.append("}\n");

        return buf.toString();
    }
}

class Loader extends LuaBaseListener {
    Graph graph = new Graph();
    String currentFuntionName = null;
 
    public void exitFunctioncall(LuaParser.FunctioncallContext ctx) {
        String funcName = ctx.getChild(0).getText();
        graph.edge(currentFuntionName, funcName);

        // System.out.println(ctx.getChild(0).getText());
    }

    public void enterStat13(LuaParser.Stat13Context ctx) {
        currentFuntionName = ctx.getChild(1).getText();
        graph.nodes.add(currentFuntionName);

        //System.out.println(ctx.getChild(1).getText());
    }
}


public class LoadLua {
    public static void main( String[] args) throws Exception
    {
        String inputFile = null;

        if ( args.length > 0 ) inputFile = args[0];
        InputStream is = System.in;
        if (inputFile != null) is = new FileInputStream(inputFile);
        ANTLRInputStream input = new ANTLRInputStream(is);

        LuaLexer lexer = new LuaLexer(input);
        LuaParser parser = new LuaParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.chunk();

        ParseTreeWalker walker = new ParseTreeWalker();
        Loader loader = new Loader();
        walker.walk(loader, tree);

        // System.out.println(loader.graph.toString());
        System.out.println(loader.graph.toDot());
    }
}
