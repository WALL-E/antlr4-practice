
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

    public void exitString(JSONParser.TextContext ctx) {
        setXML(ctx, stripQuotes(ctx.getText()));
    }

    public void exitArrayValue(JSONParser.EmptyContext ctx) {
         setXML(ctx, getXML(ctx.array()));
    }
    
    public void exitObjectValue(JSONParser.EmptyContext ctx) {
         setXML(ctx, getXML(ctx.object()));
    }

    public void exitPair(JSONParser.HdrContext ctx) {
        String tag = stripQuotes(ctx.STRING().getText());
        JSONParser.ValueContext vctx = ctx.value();
        String x = String.format("<%s>%s<%s>", tag, getXML(vctx), tag);
        
        setXML(ctx, x);
    }

    public void enterRow(JSONParser.RowContext ctx) {
        currentRowFieldValues = new ArrayList<String>();
    }

    public void exitRow(CSVParser.RowContext ctx) {
        if ( ctx.getParent().getRuleIndex() == CSVParser.RULE_hdr ) return;
        
        Map<String, String> m = new LinkedHashMap<String, String>();
        int i = 0;
        for (String v : currentRowFieldValues) {
            m.put(header.get(i), v);
            i++;
        }
        rows.add(m);
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
        
        System.out.println(loader.xml);
    }
}
