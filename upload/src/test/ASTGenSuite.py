import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test_vardecl_integer(self):
	    input = """var a:integer;"""
	    expect = str(Program([VarDecl(Id("a"),IntType())]))
	    self.assertTrue(TestAST.test(input,expect,300))

	def test_vardecla_many_integer(self):
	    input = """var a,b,c:integer;"""
	    expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())]))
	    self.assertTrue(TestAST.test(input,expect,301))

	def test_vardecl_real(self):
	    input = """var a,b:real;"""
	    expect = str(Program([VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())]))
	    self.assertTrue(TestAST.test(input,expect,302))

	def test_vardecl_mutil_type(self):
	    input = """var a:integer;
	                   b:real;
	                   c:boolean;"""
	    expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),VarDecl(Id("c"),BoolType())]))
	    self.assertTrue(TestAST.test(input,expect,303))

	def test_vardecl_array(self):
	    input = """var a:array[1 .. 2] of real;
	                   s:string;
	                   """
	    expect = str(Program([VarDecl(Id("a"),ArrayType(1,2,FloatType())),VarDecl(Id("s"),StringType())]))
	    self.assertTrue(TestAST.test(input,expect,304))

  
	def test_vardecl_arr_and_int(self):
	    input = """var a:integer;
	                   a,b:array[1 .. 5] of integer;"""
	    expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("a"),ArrayType(1,5,IntType())),VarDecl(Id("b"),ArrayType(1,5,IntType()))]))
	    self.assertTrue(TestAST.test(input,expect,305))

	def test_vardecl_string_of_array(self):
	    input = """var a:integer;
	                   c,d:array[-1 .. 6] of string;
	    """
	    expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("c"),ArrayType(-1,6,StringType())),VarDecl(Id("d"),ArrayType(-1,6,StringType()))]))
	    self.assertTrue(TestAST.test(input,expect,306))

	def test_var(self):

		"""Simple var """
		input = """var a : integer; """
		expect = str(Program([VarDecl(Id("a"),IntType())]))
		self.assertTrue(TestAST.test(input,expect,307))

	def test_variable_mutil(self):
		"""full var test """
		input = """var a : integer; 
		            b,c:real;
		            c:array[1 .. 100] of boolean;
		            d:string;"""
		expect = str(Program([VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType()),
		VarDecl(Id("c"),FloatType()),VarDecl(Id("c"),ArrayType(1,100,BoolType())),VarDecl(Id("d"),StringType())]))
		self.assertTrue(TestAST.test(input,expect,308))

	

	def test_function_declare_1(self):
		input = """function foo(): integer;
		begin
		end	"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
		self.assertTrue(TestAST.test(input,expect,309))

	def test_function_declare_2(self):
		"""function foo(): real;
		begin
		end"""
		input = """function foo(): real;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[],FloatType())]))
		self.assertTrue(TestAST.test(input,expect,310))

		
		
	def test_function_declare_3(self):
		"""function foo(): string;
		begin
		end"""
		input = """function foo(): string;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[],StringType())]))
		self.assertTrue(TestAST.test(input,expect,311))

	def test_function_declare_4(self):
		"""function foo(): boolean;
		begin
		end"""
		input = """function foo(): boolean;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[],BoolType())]))
		self.assertTrue(TestAST.test(input,expect,312))

	def test_function_declare_5(self):
		"""function foo(): array [1 .. 5] of integer;
		begin
		end"""
		input = """function foo(): array [1 .. 5] of integer;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[],ArrayType(1,5,IntType()))]))
		self.assertTrue(TestAST.test(input,expect,313))

	def test_function_declare_6(self):
		"""function foo(a: integer): array [1 .. 5] of integer;
		begin
		end"""
		input = """function foo(a: integer): array [1 .. 5] of integer;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType())],[],[],ArrayType(1,5,IntType()))]))
		self.assertTrue(TestAST.test(input,expect,314))

	def test_function_declare_7(self):
		"""function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end"""
		input = """function foo(a,b: integer): array [1 .. 5] of integer;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[],[],ArrayType(1,5,IntType()))]))
		self.assertTrue(TestAST.test(input,expect,315))
		
	def test_function_declare_8(self):
		"""function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end"""
		input = """function foo(a,b: integer ; c: real): array [1 .. 5] of integer;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),FloatType())],[],[],ArrayType(1,5,IntType()))]))
		self.assertTrue(TestAST.test(input,expect,316))

	def test_function_declare_9(self):
		"""function foo(): integer;
		var b: integer;
		begin
		end"""
		input = """function foo(): integer;
		var b: integer;
		begin
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[VarDecl(Id("b"),IntType())],[],IntType())]))
		self.assertTrue(TestAST.test(input,expect,317))

	def test_function_declare_8(self):
		"""function foo(): integer;
		begin
			a := 3;
		end"""
		input = """function foo(): integer;
		begin
			a := 3;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),IntLiteral(3))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,318))

	      
	def test_assign1(self):
		input = """procedure main();
		           var a : integer;
		           Begin
		               a:=exp;
		           end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[Assign(Id("a"),Id("exp"))],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,319)) 

	def test_assignment_2(self):
		input = """function foo(): integer;
		begin
			a := b := 4;
		end	"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("b"),IntLiteral(4)),Assign(Id("a"),Id("b"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,320))

	def test_assignment_3(self):
	
		input = """function foo(): integer;
		begin
			a := b := c := d := 4;
		end"""
		
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("d"),IntLiteral(4)),Assign(Id("c"),Id("d")),Assign(Id("b"),Id("c")),Assign(Id("a"),Id("b"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,321))


	def test_assignment_4(self):
		"""function foo(): integer;
		begin
			a[2] := 6;
		end"""
		input = """function foo(): integer;
		begin
			a[2] := 6;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(6))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,322))

	def test_assignment_complex(self):
		"""complex assign """
		input = """function sim(a:array[1 .. 2] of string;b:boolean) : integer; 
		           var bien1,bien2 : integer;
		           begin
		                bien1:=bien2:=len(a[1])+len(a[2]);  
		           end"""
		expect = str(Program([FuncDecl(Id("sim"),[VarDecl(Id("a"),ArrayType(1,2,StringType())),VarDecl(Id("b"),BoolType())],[VarDecl(Id("bien1"),IntType()),VarDecl(Id("bien2"),IntType())],[Assign(Id("bien2"),BinaryOp("+",CallExpr(Id("len"),[ArrayCell(Id("a"),IntLiteral(1))]),CallExpr(Id("len"),[ArrayCell(Id("a"),IntLiteral(2))]))),Assign(Id("bien1"),Id("bien2"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,323))

	def test_stmt_if1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if (a=b) then foo(2);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[IntLiteral(2)])],[])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,324))

	def test_stmt_if2(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if (a=b) then foo(2);
		                else a:=b;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[IntLiteral(2)])],[Assign(Id("a"),Id("b"))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,325))

	def test_stmt_if3(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if (a=b) then begin
		                    foo(a);
		                    foo(2);
		                end
		                else a:=b;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[Id("a")]),CallStmt(Id("foo"),[IntLiteral(2)])],[Assign(Id("a"),Id("b"))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,326))

	def test_stmt_if4(self):    
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if (a=b) then foo(2);
		                else begin 
		                    a:=b;
		                    c:=d:=1;
		                end
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[IntLiteral(2)])],[Assign(Id("a"),Id("b")),Assign(Id("d"),IntLiteral(1)),Assign(Id("c"),Id("d"))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,327))

	def test_stmt_if5(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if (a=b) then begin
		                    foo(a);
		                    foo(2);
		                end
		                else begin 
		                    a:=b;
		                    c:=d:=1;
		                end
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BinaryOp("=",Id("a"),Id("b")),[CallStmt(Id("foo"),[Id("a")]),CallStmt(Id("foo"),[IntLiteral(2)])],[Assign(Id("a"),Id("b")),Assign(Id("d"),IntLiteral(1)),Assign(Id("c"),Id("d"))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,328))

	def test_stmt_if6(self):
		input = """procedure main();
			var a : integer;
			Begin
			if true then
			if false then a:=false;
			else a:=true;
			end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BooleanLiteral(True),[If(BooleanLiteral(False),[Assign(Id("a"),BooleanLiteral(False))],[Assign(Id("a"),BooleanLiteral(True))])],[])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,329))

	def test_stmt_if7(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            var a : integer;
		            Begin
		                if true then a:=true;
		                else
		                if false then a:=false;
		                else
		                if true and false then a:=true AND false;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType())],[If(BooleanLiteral(True),[Assign(Id("a"),BooleanLiteral(True))],[If(BooleanLiteral(False),[Assign(Id("a"),BooleanLiteral(False))],[If(BinaryOp("and",BooleanLiteral(True),BooleanLiteral(False)),[Assign(Id("a"),BinaryOp("and",BooleanLiteral(True),BooleanLiteral(False)))],[])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,330))
	def test_statement_while1(self):
		input = """function foo(): integer;
		begin
			while a < 5
			do
				a := a + 1 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<",Id("a"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,331))

	def test_statement_while2(self):
		"""test_statement"""
		input = """function foo(): integer;
		begin
			while a <= b
			do
				a := a*b - 6 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,332))

	def test_statement_while3(self):
		input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,333))

	def test_statement_while4(self):
		input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a*b - 6 ;
			end	
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),IntLiteral(6)))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,334))

	def test_statement_while5(self):
		input = """function foo(): integer;
		begin
			while a <= b
			do
			begin
				a := a + 1 ;
				b := b + 1 ;
			end	
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[While(BinaryOp("<=",Id("a"),Id("b")),[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,335))
	def test_stmt_for1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            for i := 1 to n do a[i]:=1.1;
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(1),Id("n"),True,[Assign(ArrayCell(Id("a"),Id("i")),FloatLiteral(1.1))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,336))

	def test_stmt_for2(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            for i := 1 downto n do begin
		                foo(i,i);
		                if(i<n)then i:=n;
		                else i:=i+i;
		            end
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(1),Id("n"),False,[CallStmt(Id("foo"),[Id("i"),Id("i")]),If(BinaryOp("<",Id("i"),Id("n")),[Assign(Id("i"),Id("n"))],[Assign(Id("i"),BinaryOp("+",Id("i"),Id("i")))])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,337))
	def test_stmt_for3(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            if n>0 then
		            for i := 1 to n do
		                foo(i,i);
		            else for i := 10 downto n do
		                foo(i,i);
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[If(BinaryOp(">",Id("n"),IntLiteral(0)),[For(Id("i"),IntLiteral(1),Id("n"),True,[CallStmt(Id("foo"),[Id("i"),Id("i")])])],[For(Id("i"),IntLiteral(10),Id("n"),False,[CallStmt(Id("foo"),[Id("i"),Id("i")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,338))
	def test_stmt_for4(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            while n>0 do
		            for i := 1 to n do
		                foo(i,i);
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp(">",Id("n"),IntLiteral(0)),[For(Id("i"),IntLiteral(1),Id("n"),True,[CallStmt(Id("foo"),[Id("i"),Id("i")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,339))
	def test_stmt_for5(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            for i := 1 to n do
		                while(a=a)do
		                foo(i,i);
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(1),Id("n"),True,[While(BinaryOp("=",Id("a"),Id("a")),[CallStmt(Id("foo"),[Id("i"),Id("i")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,340))
	def test_stmt_for6(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		        Begin
		            for i := -1 to n+1 do
		                
		                foo(i,i);
		        end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),UnaryOp("-",IntLiteral(1)),BinaryOp("+",Id("n"),IntLiteral(1)),True,[CallStmt(Id("foo"),[Id("i"),Id("i")])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,341))
	def test_stmt_break1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                break;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[Break()],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,342))
	def test_stmt_break2(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		             
		                    if (true) then
		                    brEak;
		                
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[If(BooleanLiteral(True),[Break()],[])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,343))
	def test_stmt_break3(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                for i := 1 to n do
		                    brEak;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(1),Id("n"),True,[Break()])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,344))
	def test_stmt_break4(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                while n<100 do
		                begin
		                    brEak;
		                    n:=n+1;
		                    end
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("<",Id("n"),IntLiteral(100)),[Break(),Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1)))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,345))
	def test_return1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                return;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[Return()],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,346))
	def test_return2(self):
		"""Simple program: int main() {} """
		input = """function foo():integer;
		            Begin
		                return foo((a[1])[1]);
		            end"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(CallExpr(Id("foo"),[ArrayCell(ArrayCell(Id("a"),IntLiteral(1)),IntLiteral(1))]))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,347))
	def test_return3(self):
		"""Simple program: int main() {} """
		input = """function foo():boolean;
		            Begin
		                return (A>b) and c;
		            end"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(BinaryOp("and",BinaryOp(">",Id("A"),Id("b")),Id("c")))],BoolType())]))
		self.assertTrue(TestAST.test(input,expect,348))
	def test_return4(self):
		"""Simple program: int main() {} """
		input = """function foo():boolean;
		            Begin
		                if a then
		                return (A>b) and c;
		                else return b;
		            end"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[If(Id("a"),[Return(BinaryOp("and",BinaryOp(">",Id("A"),Id("b")),Id("c")))],[Return(Id("b"))])],BoolType())]))
		self.assertTrue(TestAST.test(input,expect,349))    
	def test_stmt_continue1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                continue;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[Continue()],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,350))
	def test_stmt_continue2(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		             
		                    if (true) then
		                    ConTiNuE;
		                
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[If(BooleanLiteral(True),[Continue()],[])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,351))
	def test_stmt_continue3(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                for i := 1 to n do
		                    conTINue;
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(1),Id("n"),True,[Continue()])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,352))
	def test_stmt_continue4(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                while n<100 do
		                begin
		                    ConTinUE;
		                    n:=n+1;
		                    end
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("<",Id("n"),IntLiteral(100)),[Continue(),Assign(Id("n"),BinaryOp("+",Id("n"),IntLiteral(1)))])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,353))
	def test_stmt_continue5(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                for i := -n to -m do begin
		                    if (true) then
		                    brEak;
		                    else ConTiNue;
		                EnD
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),UnaryOp("-",Id("n")),UnaryOp("-",Id("m")),True,[If(BooleanLiteral(True),[Break()],[Continue()])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,354))
	def test_stmt_with1(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                with a:string; do
		                print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType())],[CallStmt(Id("print"),[Id("a")])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,355))
	def test_stmt_with2(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                with a:string;a,b:integer; do
		                begin
		                    a:=b+1;
		                    print(a);
		                    print(A+b);
		                end
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1))),CallStmt(Id("print"),[Id("a")]),CallStmt(Id("print"),[BinaryOp("+",Id("A"),Id("b"))])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,356))
	def test_stmt_with3(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                with a:string;a,b:integer; do
		                if 1 then print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[If(IntLiteral(1),[CallStmt(Id("print"),[Id("a")])],[])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,357))
	def test_stmt_with4(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		            if 1 then 
		                with a:string;a,b:integer; do print(a);
		            else with a:string;a,b:integer; do print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[If(IntLiteral(1),[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallStmt(Id("print"),[Id("a")])])],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallStmt(Id("print"),[Id("a")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,358))
	def test_stmt_with5(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		            for i:= 2 to 3 do
		                with a:string;a,b:integer; do print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id("i"),IntLiteral(2),IntLiteral(3),True,[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallStmt(Id("print"),[Id("a")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,359))
	def test_stmt_with6(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                with a:string;a,b:integer; do for i:= 2 to 3 do print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[For(Id("i"),IntLiteral(2),IntLiteral(3),True,[CallStmt(Id("print"),[Id("a")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,361))
	def test_stmt_with7(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                with a:string;a,b:integer; do 
		                while (n<2) and (n>3) do print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[While(BinaryOp("and",BinaryOp("<",Id("n"),IntLiteral(2)),BinaryOp(">",Id("n"),IntLiteral(3))),[CallStmt(Id("print"),[Id("a")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,362))
	def test_stmt_with8(self):
		"""Simple program: int main() {} """
		input = """procedure main();
		            Begin
		                while (n<2) and (n>3) do
		                with a:string;a,b:integer; do 
		                print(a);
		            end"""
		expect = str(Program([FuncDecl(Id("main"),[],[],[While(BinaryOp("and",BinaryOp("<",Id("n"),IntLiteral(2)),BinaryOp(">",Id("n"),IntLiteral(3))),[With([VarDecl(Id("a"),StringType()),VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallStmt(Id("print"),[Id("a")])])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,363))
	def test_expression_1(self):
		"""function foo(): integer;
		begin
			a := b and then c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b and then c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("and then",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,364))

	def test_expression_2(self):
		"""function foo(): integer;
		begin
			a := b or else c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b or else c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("or else",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,365))

	def test_expression_3(self):
		"""function foo(): integer;
		begin
			a := b + c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b + c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,366))

	def test_expression_4(self):
		"""function foo(): integer;
		begin
			a := b - c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b - c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("-",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,367))

	def test_expression_5(self):
		"""function foo(): integer;
		begin
			a := b * c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b * c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("*",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,368))

	def test_expression_6(self):
		"""function foo(): integer;
		begin
			a := b / c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b / c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("/",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,369))

	def test_expression_7(self):
		"""function foo(): integer;
		begin
			a := b <> c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b <> c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("<>",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,370))

	def test_expression_8(self):
		"""function foo(): integer;
		begin
			a := b and c ;
		end"""
		input = """function foo(): integer;
		begin
			a := b and c ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("and",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,371))

	def test_expression_9(self):
		"""function foo(): integer;
		begin
			a := -b;
		end"""
		input = """function foo(): integer;
		begin
			a := -b;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),UnaryOp("-",Id("b")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,322))

	def test_expression_10(self):
		"""function foo(): integer;
		begin
			a := not b;
		end"""
		input = """function foo(): integer;
		begin
			a := not b;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),UnaryOp("not",Id("b")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,373))

	def test_expression_11(self):
		"""function foo(): integer;
		begin
			a := (b + c);
		end"""
		input = """function foo(): integer;
		begin
			a := (b + c);
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("+",Id("b"),Id("c")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,374))

	def test_expression_12(self):
		"""function foo(): integer;
		begin
			a := b + c*d - e ;
		end"""
		input = """function foo(): integer;
		begin
			a := b + c*d - e ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),BinaryOp("*",Id("c"),Id("d"))),Id("e")))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,375))

	def test_expression_13(self):
		"""function foo(): integer;
		begin
			a[3] := 3 ;
		end"""
		input = """function foo(): integer;
		begin
			a[3] := 3 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),IntLiteral(3)),IntLiteral(3))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,376))

	def test_expression_14(self):
		"""function foo(): integer;
		begin
			a := b[5] := c + 6 ;
		end"""
		input = """function foo(): integer;
		begin
			a := b[5] := c + 6 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),Assign(ArrayCell(Id("b"),IntLiteral(5)),BinaryOp("+",Id("c"),IntLiteral(6))))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,377))

	def test_expression_15(self):
		"""function foo(): integer;
		begin
			a := true ;
		end"""
		input = """function foo(): integer;
		begin
			a := true ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BooleanLiteral(True))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,378))

	def test_expression_16(self):
		"""function foo(): integer;
		begin
			a := false ;
		end"""
		input = """function foo(): integer;
		begin
			a := false ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BooleanLiteral(False))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,379))

	def test_expression_17(self):
		"""function foo(): integer;
		begin
			a := true or false or true and false ;
		end"""
		input = """function foo(): integer;
		begin
			a := true or false or true and false ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),BinaryOp("or",BinaryOp("or",BooleanLiteral(True),BooleanLiteral(False)),BinaryOp("and",BooleanLiteral(True),BooleanLiteral(False))))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,380))

	def test_expression_18(self):
		"""function foo(): integer;
		begin
			a := "xin chao cac ban" ;
		end"""
		input = """function foo(): integer;
		begin
			a := "xin chao cac ban" ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),StringLiteral("xin chao cac ban"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,381))

	def test_expression_19(self):
		"""function foo(): integer;
		begin
			a := "day la mon nguyen ly ngon ngu lap trinh" ;
		end"""
		input = """function foo(): integer;
		begin
			a := "day la mon nguyen ly ngon ngu lap trinh" ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),StringLiteral("day la mon nguyen ly ngon ngu lap trinh"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,382))

	def test_expression_20(self):
		"""function foo(): integer;
		begin
			a := 2.5 ;
		end"""
		input = """function foo(): integer;
		begin
			a := 2.5 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),FloatLiteral(2.5))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,383))

	def test_expression_21(self):
		"""function foo(): integer;
		begin
			a := 2.1e-2 ;
		end"""
		input = """function foo(): integer;
		begin
			a := 2.1e-2 ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),FloatLiteral(2.1e-2))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,384))

	def test_expression_22(self):
		"""function foo(): integer;
		begin
			a[2] := b[3] := c[4] := d[5] ;
		end"""
		input = """function foo(): integer;
		begin
			a[2] := b[3] := c[4] := d[5] ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("c"),IntLiteral(4)),ArrayCell(Id("d"),IntLiteral(5))),Assign(ArrayCell(Id("b"),IntLiteral(3)),ArrayCell(Id("c"),IntLiteral(4))),Assign(ArrayCell(Id("a"),IntLiteral(2)),ArrayCell(Id("b"),IntLiteral(3)))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,385))

	def test_expression_23(self):
		"""function foo(): integer;
		begin
			a := b[c[d[6]]] ;
		end"""
		input = """function foo(): integer;
		begin
			a := b[c[d[6]]] ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),ArrayCell(Id("b"),ArrayCell(Id("c"),ArrayCell(Id("d"),IntLiteral(6)))))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,386))

	def test_expression_24(self):
		"""function foo(): integer;
		begin
			a[b[3]] := c[d[2]] ;
		end"""
		input = """function foo(): integer;
		begin
			a[b[3]] := c[d[2]] ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(3))),ArrayCell(Id("c"),ArrayCell(Id("d"),IntLiteral(2))))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,387))

	def test_expression_25(self):
		"""function foo(): integer;
		begin
			a := foo(3) ;
		end"""
		input = """function foo(): integer;
		begin
			a := foo(3) ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3)]))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,388))

	def test_expression_26(self):
		"""function foo(): integer;
		begin
			a := foo(3,4,5,6,7) ;
		end"""
		input = """function foo(): integer;
		begin
			a := foo(3,4,5,6,7) ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[IntLiteral(3),IntLiteral(4),IntLiteral(5),IntLiteral(6),IntLiteral(7)]))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,389))

	def test_expression_27(self):
		"""function foo(): integer;
		begin
			a := foo(b,c,d) ;
		end"""
		input = """function foo(): integer;
		begin
			a := foo(b,c,d) ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[Id("b"),Id("c"),Id("d")]))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,390))

	def test_expression_28(self):
		"""function foo(): integer;
		begin
			a := foo(1 + 2,3 * b,c[d[2 + 4]]) ;
		end"""
		input = """function foo(): integer;
		begin
			a := foo(1 + 2,3 * b,c[d[2 + 4]]) ;
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[],[],[Assign(Id("a"),CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(1),IntLiteral(2)),BinaryOp("*",IntLiteral(3),Id("b")),ArrayCell(Id("c"),ArrayCell(Id("d"),BinaryOp("+",IntLiteral(2),IntLiteral(4))))]))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,391))
	def test_complex_program1(self):
		"""hello world"""
		input = """
		var st : string;
		procedure main();
		begin
		    st := "hello world";
		    print(st);
		end"""
		expect = str(Program([VarDecl(Id("st"),StringType()),FuncDecl(Id("main"),[],[],[Assign(Id("st"),StringLiteral("hello world")),CallStmt(Id("print"),[Id("st")])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,392))
	def test_complex_program2(self):
		"""nhap chuoi"""
		input = """
		var st : string;
		procedure main();
		begin
		    println("nhap str:");
		    readln(st);
		    print(st);
		end"""
		expect = str(Program([VarDecl(Id("st"),StringType()),FuncDecl(Id("main"),[],[],[CallStmt(Id("println"),[StringLiteral("nhap str:")]),CallStmt(Id("readln"),[Id("st")]),CallStmt(Id("print"),[Id("st")])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,393))
	def test_complex_program3(self):
		"""ham giai thua"""
		input = """
		function gt(i : integer): integer;
		begin
		    if i <= 1 then return 1;
		    else
		    retuRn i*gt(i-1);
		end"""
		expect = str(Program([FuncDecl(Id("gt"),[VarDecl(Id("i"),IntType())],[],[If(BinaryOp("<=",Id("i"),IntLiteral(1)),[Return(IntLiteral(1))],[Return(BinaryOp("*",Id("i"),CallExpr(Id("gt"),[BinaryOp("-",Id("i"),IntLiteral(1))])))])],IntType())]))
		self.assertTrue(TestAST.test(input,expect,394))
	def test_complex_program4(self):
		"""ham tim max"""
		input = """
		function max(M : array[1 .. 100] of integer; n:integer): integer;
		var ret :integer;
		begin
		    for i :=1 to n do
		        if max < M[i] then max := M[i];//loi thieu :
		    return max;
		end"""
		expect = str(Program([FuncDecl(Id("max"),[VarDecl(Id("M"),ArrayType(1,100,IntType())),VarDecl(Id("n"),IntType())],[VarDecl(Id("ret"),IntType())],[For(Id("i"),IntLiteral(1),Id("n"),True,[If(BinaryOp("<",Id("max"),ArrayCell(Id("M"),Id("i"))),[Assign(Id("max"),ArrayCell(Id("M"),Id("i")))],[])]),Return(Id("max"))],IntType())]))
		self.assertTrue(TestAST.test(input,expect,395))
	def test_complex_program5(self):
		"""in so le"""
		input = """
		procedure main();
		var i,n :integer;
		begin
		    readln(n);
		    for i:=1 to n do if i mod 2 = 0 then print(i," ");
		end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],[CallStmt(Id("readln"),[Id("n")]),For(Id("i"),IntLiteral(1),Id("n"),True,[If(BinaryOp("=",BinaryOp("mod",Id("i"),IntLiteral(2)),IntLiteral(0)),[CallStmt(Id("print"),[Id("i"),StringLiteral(" ")])],[])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,396))
	def test_complex_program6(self):
		"""in so le >0"""
		input = """
		procedure main();
		var i,n :integer;
		begin
		    readln(n);
		    for i:=1 to n do 
		    if  (i > 0 )and ((i mod 2)  > 0) then print(i," ");
		end"""
		expect = str(Program([FuncDecl(Id("main"),[],[VarDecl(Id("i"),IntType()),VarDecl(Id("n"),IntType())],[CallStmt(Id("readln"),[Id("n")]),For(Id("i"),IntLiteral(1),Id("n"),True,[If(BinaryOp("and",BinaryOp(">",Id("i"),IntLiteral(0)),BinaryOp(">",BinaryOp("mod",Id("i"),IntLiteral(2)),IntLiteral(0))),[CallStmt(Id("print"),[Id("i"),StringLiteral(" ")])],[])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,397))
	def test_complex_program7(self):
		"""chu vi hcn"""
		input = """function cv(a,b : real):real;
		begin
		    return a+a+b+b;
		end
		procedure main();
		var a,b :integer;
		begin
		    readln(a,b);
		    print(cv(a,b));
		end"""
		expect = str(Program([FuncDecl(Id("cv"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],[],[Return(BinaryOp("+",BinaryOp("+",BinaryOp("+",Id("a"),Id("a")),Id("b")),Id("b")))],FloatType()),FuncDecl(Id("main"),[],[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],[CallStmt(Id("readln"),[Id("a"),Id("b")]),CallStmt(Id("print"),[CallExpr(Id("cv"),[Id("a"),Id("b")])])],VoidType())]))
		self.assertTrue(TestAST.test(input,expect,398))
	def test_complex_8(self):

		input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[If(BinaryOp("<",Id("y"),IntLiteral(10)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(2)))])])])])]))
		self.assertTrue(TestAST.test(input,expect,399))

	def test_complex_9(self):

		input = """procedure foo(a,b: integer; c: array [1 .. 5] of string);
		var x,y: real ;
		z: array [10 .. 20] of integer ;
		begin
			if x < 5 then
				a := b + 1 ;
			else
				if y < 10 then
					if z < 20 then
						b := b - 2 ; 
					else
						c := c + 5 ;						
		end
		"""
		expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),ArrayType(1,5,StringType()))],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("z"),ArrayType(10,20,IntType()))],[If(BinaryOp("<",Id("x"),IntLiteral(5)),[Assign(Id("a"),BinaryOp("+",Id("b"),IntLiteral(1)))],[If(BinaryOp("<",Id("y"),IntLiteral(10)),[If(BinaryOp("<",Id("z"),IntLiteral(20)),[Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(2)))],[Assign(Id("c"),BinaryOp("+",Id("c"),IntLiteral(5)))])])])])]))
		self.assertTrue(TestAST.test(input,expect,400))

