
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.FileInputStream;
import java.io.InputStream;

import java.util.*;


class Loader extends CSVBaseListener {
    public static final String EMPTY = "";

    List<Map<String,String>> rows = new ArrayList<Map<String,String>>();

    List<String> header;

    List<String> currentRowFieldValues;

 
    public void exitString(CSVParser.StringContext ctx) {
        currentRowFieldValues.add(ctx.STRING().getText());
    }

    public void exitText(CSVParser.TextContext ctx) {
        currentRowFieldValues.add(ctx.TEXT().getText());
    }

    public void exitEmpty(CSVParser.EmptyContext ctx) {
        currentRowFieldValues.add(EMPTY);
    }

    public void exitHdr(CSVParser.HdrContext ctx) {
        header = new ArrayList<String>();
        header.addAll(currentRowFieldValues);
    }

    public void enterRow(CSVParser.RowContext ctx) {
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


public class LoadCSV {
    public static void main( String[] args) throws Exception
    {
        String inputFile = null;

        if ( args.length > 0 ) inputFile = args[0];
        InputStream is = System.in;
        if (inputFile != null) is = new FileInputStream(inputFile);
        ANTLRInputStream input = new ANTLRInputStream(is);

        CSVLexer lexer = new CSVLexer(input);
        CSVParser parser = new CSVParser(new CommonTokenStream(lexer));
        ParseTree tree = parser.csvFile();

        ParseTreeWalker walker = new ParseTreeWalker();
        Loader loader = new Loader();
        walker.walk(loader, tree);
        
        System.out.println(loader.rows);
    }
}
