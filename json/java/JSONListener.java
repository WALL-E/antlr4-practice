// Generated from JSON.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link JSONParser}.
 */
public interface JSONListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link JSONParser#json}.
	 * @param ctx the parse tree
	 */
	void enterJson(JSONParser.JsonContext ctx);
	/**
	 * Exit a parse tree produced by {@link JSONParser#json}.
	 * @param ctx the parse tree
	 */
	void exitJson(JSONParser.JsonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AnObj}
	 * labeled alternative in {@link JSONParser#obj}.
	 * @param ctx the parse tree
	 */
	void enterAnObj(JSONParser.AnObjContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AnObj}
	 * labeled alternative in {@link JSONParser#obj}.
	 * @param ctx the parse tree
	 */
	void exitAnObj(JSONParser.AnObjContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EmptyObj}
	 * labeled alternative in {@link JSONParser#obj}.
	 * @param ctx the parse tree
	 */
	void enterEmptyObj(JSONParser.EmptyObjContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EmptyObj}
	 * labeled alternative in {@link JSONParser#obj}.
	 * @param ctx the parse tree
	 */
	void exitEmptyObj(JSONParser.EmptyObjContext ctx);
	/**
	 * Enter a parse tree produced by the {@code PairGroup}
	 * labeled alternative in {@link JSONParser#pair}.
	 * @param ctx the parse tree
	 */
	void enterPairGroup(JSONParser.PairGroupContext ctx);
	/**
	 * Exit a parse tree produced by the {@code PairGroup}
	 * labeled alternative in {@link JSONParser#pair}.
	 * @param ctx the parse tree
	 */
	void exitPairGroup(JSONParser.PairGroupContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArrayOfValues}
	 * labeled alternative in {@link JSONParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArrayOfValues(JSONParser.ArrayOfValuesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArrayOfValues}
	 * labeled alternative in {@link JSONParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArrayOfValues(JSONParser.ArrayOfValuesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code EmptyArray}
	 * labeled alternative in {@link JSONParser#array}.
	 * @param ctx the parse tree
	 */
	void enterEmptyArray(JSONParser.EmptyArrayContext ctx);
	/**
	 * Exit a parse tree produced by the {@code EmptyArray}
	 * labeled alternative in {@link JSONParser#array}.
	 * @param ctx the parse tree
	 */
	void exitEmptyArray(JSONParser.EmptyArrayContext ctx);
	/**
	 * Enter a parse tree produced by the {@code String}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void enterString(JSONParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code String}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void exitString(JSONParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void enterAtom(JSONParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Atom}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void exitAtom(JSONParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ObjValue}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void enterObjValue(JSONParser.ObjValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ObjValue}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void exitObjValue(JSONParser.ObjValueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ArrayValue}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void enterArrayValue(JSONParser.ArrayValueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ArrayValue}
	 * labeled alternative in {@link JSONParser#value}.
	 * @param ctx the parse tree
	 */
	void exitArrayValue(JSONParser.ArrayValueContext ctx);
}