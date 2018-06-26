
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.*;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;


class Loader extends MySqlParserBaseListener {
    public void exitSelectElements(MySqlParser.SelectElementsContext ctx) {
        System.out.println("exit SelectElements");
    }

    public void exitTableSources(MySqlParser.TableSourcesContext ctx) {
        System.out.println("exit TableSources");
    }
}

public class MySql {
  public static void main( String[] args) throws Exception
  {
    String inputFile = null;

    if ( args.length > 0 ) inputFile = args[0];
    InputStream is = System.in;
    if (inputFile != null) is = new FileInputStream(inputFile);
    ANTLRInputStream input = new ANTLRInputStream(is);


    MySqlLexer lexer = new MySqlLexer(input);
    MySqlParser parser = new MySqlParser(new CommonTokenStream(lexer));
    ParseTree root = parser.root();

    ParseTreeWalker walker = new ParseTreeWalker();
    Loader loader = new Loader();
    walker.walk(loader, root);

    // System.out.println(root.toStringTree(parser));
  }
}

