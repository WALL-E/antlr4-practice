// Generated from CYMBOL.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CYMBOLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CYMBOLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#root}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRoot(CYMBOLParser.RootContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#chunk}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitChunk(CYMBOLParser.ChunkContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#varDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDecl(CYMBOLParser.VarDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#varType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarType(CYMBOLParser.VarTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#functionDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDecl(CYMBOLParser.FunctionDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#formalParameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormalParameters(CYMBOLParser.FormalParametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#formalParameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFormalParameter(CYMBOLParser.FormalParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(CYMBOLParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStat(CYMBOLParser.StatContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#exprList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprList(CYMBOLParser.ExprListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(CYMBOLParser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link CYMBOLParser#functioncall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctioncall(CYMBOLParser.FunctioncallContext ctx);
}