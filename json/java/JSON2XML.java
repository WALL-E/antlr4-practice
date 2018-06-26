
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

import java.util.*;


class Loader extends JSONBaseListener {
    ParseTreeProperty<String> xml = new ParseTreeProperty<String>();
    
    String getXML(ParseTree ctx) {return xml.get(ctx);}
    void setXML(ParseTree ctx, String s) {xml.put(ctx, s)}
    

    public void exitAtom(JSONParser.AtomContext ctx) {
        setXML(ctx, ctx.getText());
    }

    public void exitString(JSONParser.StringContext ctx) {
        setXML(ctx, stripQuotes(ctx.getText()));
    }

    public void exitArrayValue(JSONParser.ArrayValueContext ctx) {
         setXML(ctx, getXML(ctx.array()));
    }
    
    public void exitObjectValue(JSONParser.ObjectValueContext ctx) {
         setXML(ctx, getXML(ctx.object()));
    }

    public void exitPair(JSONParser.PairContext ctx) {
        String tag = stripQuotes(ctx.STRING().getText());
        JSONParser.ValueContext vctx = ctx.value();
        String x = String.format("<%s>%s<%s>", tag, getXML(vctx), tag);
        
        setXML(ctx, x);
    }
    
    public void exitAnObject(JSONParser.AnObjectContext ctx) {
        StringBuilder buf = new StringBuilder();
        buf.append("\n");
        for (JSONParser.PairContext pctx : ctx.pair()) {
            buf.append(getXML(pctx));
        }
        setXML(ctx, buf.toString());
    }
    
    public void exitAnObject(JSONParser.AnObjectContext ctx) {
        StringBuilder buf = new StringBuilder();
        buf.append("\n");
        for (JSONParser.ValueContext vctx : ctx.value()) {
            buf.append("<element>");
            buf.append(getXML(vctx));
            buf.append("</element>");
            buf.append("\n");
        }
        setXML(ctx, buf.toString());
    }

    public void exitJson(JSONParser.JsonContext ctx) {
         setXML(ctx, getXML(ctx.getChild(0)));
    }
}


public class JSON2XML {
    public static void main( String[] args) throws Exception
    {
        String inputFile = null;

        if ( args.length > 0 ) inputFile = args[0];
        InputStream is = System.in;
        if (inputFile != null) is = new FileInputStream(inputFile);
        ANTLRInputStream input = new ANTLRInputStream(is);

        JSONLexer lexer = new JSONLexer(input);
        JSONParser parser = new JSONParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.csvFile();

        ParseTreeWalker walker = new ParseTreeWalker();
        Loader loader = new Loader();
        walker.walk(loader, tree);
        
        System.out.println("translate ok");
    }
}
