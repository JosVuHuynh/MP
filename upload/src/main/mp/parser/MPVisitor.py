# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardel.
    def visitVardel(self, ctx:MPParser.VardelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_decla.
    def visitVar_decla(self, ctx:MPParser.Var_declaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_type.
    def visitReturn_type(self, ctx:MPParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_type.
    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#subscript.
    def visitSubscript(self, ctx:MPParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdel.
    def visitFuncdel(self, ctx:MPParser.FuncdelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_statement.
    def visitCompound_statement(self, ctx:MPParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MPParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_statement.
    def visitIf_statement(self, ctx:MPParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_statement.
    def visitFor_statement(self, ctx:MPParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_statement.
    def visitWhile_statement(self, ctx:MPParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_statement.
    def visitBreak_statement(self, ctx:MPParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_statement.
    def visitContinue_statement(self, ctx:MPParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_statement.
    def visitReturn_statement(self, ctx:MPParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_statement.
    def visitCall_statement(self, ctx:MPParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_statement.
    def visitWith_statement(self, ctx:MPParser.With_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedel.
    def visitProcedel(self, ctx:MPParser.ProcedelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr1.
    def visitExpr1(self, ctx:MPParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr2.
    def visitExpr2(self, ctx:MPParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr3.
    def visitExpr3(self, ctx:MPParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr4.
    def visitExpr4(self, ctx:MPParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr5.
    def visitExpr5(self, ctx:MPParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr6.
    def visitExpr6(self, ctx:MPParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index_exp.
    def visitIndex_exp(self, ctx:MPParser.Index_expContext):
        return self.visitChildren(ctx)



del MPParser