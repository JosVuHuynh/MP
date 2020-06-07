import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function_1(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin foo();end"""
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """procedure main (); begin
            putIntLn();
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_undeclared_function_2(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[
            CallStmt(Id("foo"),[])])])
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,402))

    
    def test_diff_numofparam_mismatch(self):
        """More complex program"""
        input = """procedure main (a:real); begin
            putIntLn(a);
        end"""
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_undecle1_indetifier(self):
        """More complex program"""
        input = """procedure main (a:real); begin
            a:=c;
        end"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_undecle2_function(self):
        """More complex program"""
        input = """procedure main (a:real); begin
            a:=main1();
        end"""
        expect = "Undeclared Function: main1"
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_undecle3_procedure(self):
        """More complex program"""
        input = """procedure main (a:real); begin
            main1();
        end"""
        expect = "Undeclared Procedure: main1"
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_undecle4_identifier(self):
        """More complex program"""
        input = """procedure main (a:real); begin
            with c: real ; do c:=b;
        end"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_redeclared1_procedure(self):
        input = """var a: integer;
                    procedure main (); begin
                    end
                    procedure a (); begin
                    end
                """
        expect = "Redeclared Procedure: a"
        self.assertTrue(TestChecker.test(input,expect,408))
    def test_redeclared2_Variable1(self):
        input = """var a: integer;
                   procedure main (); begin
                   end
                   var a: integer;
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_redeclared3_variable2(self):
        input = """var a: integer;
                    var a:integer;
                    procedure main (); begin
                    end
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))
    def test_redeclared4_function(self):
        input = """var a: integer;
                    var b:integer;
                    procedure main (); begin
                    end
                    function a (): integer; begin
                    end
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,411))
    def test_redeclared5_function(self):
        """More complex program"""
        input = """
        var x:real;
        
        procedure main (a:real); begin
            with c: real ; do c:=a;
          
        end
        function Mai1n (a:real): real; begin
            with c: real ; do with r:real ; r:real; do c:=1;
            return Mai1n(1);
            
        end
        """
        expect = "Redeclared Variable: r"
        self.assertTrue(TestChecker.test(input,expect,412))
    def test_reundecle6_Parameter(self):
        """More complex program"""
        input = """
        var x:real;
        
        procedure main (a:real; c:real; a:string); begin
            with c: real ; do c:=a;
          
        end
        function Mai1n (a:real): real; begin
            with c: real ; do with r:real ; r:real; do c:=1;
            return Mai1n(1);
            
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,413))
    def test_reundecle7_variable(self):
        """More complex program"""
        input = """
        var x:real;y:real;z:real;t:real;x:real;
        procedure main (a:real; c:real; a:string); begin
            with c: real ; do c:=a;
        end
       
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,414))
    def test_reundecle8_procedure(self):
        """More complex program"""
        input = """
        procedure main (a:real; c:real; z:string); begin
            with c: real ; do c:=a;
        end
        procedure main (a:real; c:real; a:string); begin
            with c: real ; do c:=a;
        end
        var x:real;y:real;z:real;t:real;x:real;
        """
        expect = "Redeclared Procedure: main"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test_typemismatchStmt_1_callstmt(self):
        input = Program([
                FuncDecl(Id("main"),[],[],[
                    CallStmt(Id("putIntLn"),[])])])

        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test_typemismatchStmt_2_callstmt(self):
        input = """procedure main();
                    begin
                        putIntLn();
                    end
                """

        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test_typemismatchStmt_3_callstmt(self):
        """More complex program"""
        input = Program([VarDecl(Id("a"),StringType()),FuncDecl(Id("main"),[],[],[With([VarDecl(Id("a"),StringType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),IntType())],[CallStmt(Id("putIntLn"),[])])],VoidType())])
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_typemismatchStmt_4_callstmt(self):
        """More complex program"""
        input = """procedure foo(a:real);
                    Begin
                        foo(2+2+(3*4));
                        foo();
                    end"""
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_typemismatchStmt_5_callstmt(self):
        """More complex program"""
        input = """
                function foo(a:integer):integer;
                    Begin
                        return 1;
                    end
                procedure fool(a:integer);
                begin end
                procedure main();
                    Begin
                        fool(2+2+foo(2));
                        fool(2,3);
                    end"""
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(fool),[IntLiteral(2),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared5_function(self):
        """More complex program"""
        input = """
                function foo(a:integer):integer;
                    Begin
                        return 1;
                    end
                procedure fool(a:integer);
                begin end
                procedure main();
                    Begin
                        fool(2+2+fool(2));
                        fool(2,3);
                    end"""
                        
        expect = "Undeclared Function: fool"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_typemismatchStmt_6_callexpr(self):
        """More complex program"""
        input = """
        var x:boolean;var c:real;
         function foo (): real; begin
            return 1;
        end
        procedure main (); begin
            if foo() then main();
        end
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(foo),[]),[CallStmt(Id(main),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_typemismatchStmt_7_If(self):
        """More complex program"""
        input = """
                var a,b : integer;
                procedure main();
                    Begin
                    if(a+b) then
                        a:=b :=2;
                    else
                        fool();
                    end"""
                        
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),[AssignStmt(Id(b),IntLiteral(2)),AssignStmt(Id(a),Id(b))],[CallStmt(Id(fool),[])])"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_typemismatchStmt_8_assign(self):
        """More complex program"""
        input = """
                var a,b : boolean;
                procedure main();
                    Begin
                    if(a) then
                        a:=b :=2;
                    a();
                    end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_typemismatchExp_1_BinaryOp(self):
        input = """procedure main();
                    begin
                    end
                    procedure foo(a:real);
                    begin
                        foo("2"+2);
                    end
                """

        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(2),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_typemismatchStmt_9_If(self):
        """More complex program"""
        input = """
        var x:boolean;var c:real;
         function foo (): real; begin
            return 1;
        end
        procedure main (); begin
            if foo() then main();
        end
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(foo),[]),[CallStmt(Id(main),[])],[])"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_typemismatchExp_2_BinaryOp(self):
        """More complex program"""
        input = """
        var x:boolean;var c:real;
         function foo (): real; begin
            return 1;
        end
        procedure main (); begin
            if foo()=True then main();
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,CallExpr(Id(foo),[]),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_typemismatchStmt_10_For(self):
        """More complex program"""
        input = """
        var x:boolean;var c:real;
        
        procedure main (); var c: real; begin
           for c:=1 to 3 do main();
        end
        """
        expect = "Type Mismatch In Statement: For(Id(c)IntLiteral(1),IntLiteral(3),True,[CallStmt(Id(main),[])])"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_typemismatchExp_3_Arracell(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                    abcd[1]:=2.4;
                    abcd[2]:=a;
                    abcd[a]:=1;     
                    a[1]:=1;  
                end"""
                        
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_typemismatchStmt_11_return(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of integer;
                Begin
                    abcd[abcd[a]]:=a;
                    return abcd;
                end"""
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(abcd)))"
        self.assertTrue(TestChecker.test(input,expect,430))
    
    def test_typemismatchStmt_12_return(self):
        """More complex program"""
        input = """
                function foo():array [1 .. 100] of Boolean;
                var abc :array [1 .. 100] of Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of integer;
                Begin
                    foo()[1]:=true;
                    return abcd;
                end"""
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(abcd)))"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_typemismatchExp_4_ArrayCell(self):
        """More complex program"""
        input = """
                function foo(): Boolean;
                var abc : Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of integer;
                Begin
                    foo()[1]:=true;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    
    def test_typemismatchStmt_11_for(self):
        """More complex program"""
        input = """
        var x:boolean;var c:integer;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (c:integer); begin
           for c:=main1() +1.2 to 31 do main(c);
        end
        """
        expect = "Type Mismatch In Statement: For(Id(c)BinaryOp(+,CallExpr(Id(main1),[]),FloatLiteral(1.2)),IntLiteral(31),True,[CallStmt(Id(main),[Id(c)])])"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_typemismatchStmt_14_for(self):
        """More complex program"""
        input = """
        var x:boolean;var c:integer;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (x:integer); begin
           for x:=c to 1.3 do c:=main1();
        end
        """
        expect = "Type Mismatch In Statement: For(Id(x)Id(c),FloatLiteral(1.3),True,[AssignStmt(Id(c),CallExpr(Id(main1),[]))])"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_typemismatchStmt_15_while(self):
        """More complex program"""
        input = """
        var x:boolean;var c:integer;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (); begin
           while 1 do main();
        end
        """
        expect = "Type Mismatch In Statement: While(IntLiteral(1),[CallStmt(Id(main),[])])"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_typemismatchExp_5_BinaryOp(self):
        """More complex program"""
        input = """
        var x:boolean;var c:integer;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (); begin
           while x+1 do main();
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_typemismatchStmt_16_while(self):
        """More complex program"""
        input = """
        var x:boolean;var c:integer;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (); begin
           while main1() do main();
        end
        """
        expect = "Type Mismatch In Statement: While(CallExpr(Id(main1),[]),[CallStmt(Id(main),[])])"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_typemismatchStmt_17_assign(self):
        """More complex program"""
        input = """
        var x:boolean;var c:string;
        function main1 (): integer ; begin
           return 1;
        end
        procedure main (); begin
           c:="x";
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),StringLiteral(x))"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_typemismatchExp_6_BinaryOp (self):
        input = """
                var aBc: array[1 .. 10] of real;
                var a:boolean;
                procedure main();
                begin
                    if aBc and a then a := False;
                end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(aBc),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_typemismatchExp_7_BinaryOp (self):
        input = """
                var a:boolean;
                procedure main();
                begin
                    if a and -1 then a := False;
                end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and,Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_typemismatchExp_8_BinaryOp (self):
        input = """
                var a:boolean;
                procedure main();
                begin
                    if a > -1 then a := False;
                end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test_typemismatchExp_9_BinaryOp (self):
        input = """
                var a:integer;
                var c:real;
                var d:boolean;
                procedure main();
                begin
                    if a > d then a := 1;
                end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(a),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test_typemismatchStmt_18_assign(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                Begin
                    a := 1+2;
                    a := 1 + 1.2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_typemismatchExp_10_BinaryOp(self):
        """More complex program"""
        input = """
                procedure main();
                var a:REAl;
                Begin
                    a := 1+2;
                    a := True + 1.2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_typemismatchStmt_19_assign(self):
        """More complex program"""
        input = """
                function foo():String;
                begin
                    return "abc"; 
                end
                procedure main();
                var a:REAl;
                    b:boolean;
                Begin
                    a := 1.1+2.3;
                    b := true and false;
                    b := (1<2) and true;
                    a := foo();
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_typemismatchStmt_20_assign(self):
        """More complex program"""
        input = """
                procedure main();
                var a:REAl;
                    b:boolean;
                    c:integer;
                Begin
                    c :=  3 mod 2 div 4;
                    b := (1<2.1) and (1+1 = 2) and b;
                    a := c + 1.2;
                    c := 2/2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(/,IntLiteral(2),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_typemismatchExp_11_Callexpr(self):
        """More complex program"""
        input = """
                function foo(a : integer;b,c:real) : boolean;
                var abc : Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a,b:boolean;
                Begin
                        a := b:= Foo(1,2.2);       
                end"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[IntLiteral(1),FloatLiteral(2.2)])"
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_typemismatchExp_12_Callexpr(self):
        """More complex program"""
        input = """
                function foo(a : integer;b,c:real) : boolean;
                var abc : Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a,b:boolean;
                Begin
                        g := 123;
                        a :=Foo(1,2.2,2,2);       
                end
                var g : integer;"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[IntLiteral(1),FloatLiteral(2.2),IntLiteral(2),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_typemismatchExp_13_Callexpr(self):
        """More complex program"""
        input = """
        var x: array [1 .. 2] of integer;var c:real;var d:integer;
        function main1():   integer;
        begin return 1; end
        procedure main (e:integer); begin
           c:=main(c);
         
        end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(main),[Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_typemismatchExp_14_Callexpr(self):
        """More complex program"""
        input = """
        var x: array [1 .. 2] of integer;var c:real;var d:integer;
        function main1():   integer;
        begin return 1; end
        procedure main (e:integer); begin
           c:=1+"2";
         
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),StringLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_typemismatchExp_15_Arraycell(self):
        """More complex program"""
        input = """
        var x: array [1 .. 2] of integer;var c:real;var d:integer;
        function main1():   integer;
        begin return 1; end
        procedure main (e:integer); begin
           c[898]:=1+1;
         
        end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),IntLiteral(898))"
        self.assertTrue(TestChecker.test(input,expect,451))
    def test_break_not_in_loop_1(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                var a: array [3 .. 5] of integer;
                begin
                    break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_break_not_in_loop_2(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                begin
                    if True then break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_break_not_in_loop_3(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                var a:integer;
                begin
                    if True then a := 1; else break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,454))
    def test_break_not_in_loop_4(self):
        input = """
                procedure main ();
                begin
                end
                function foo():integer;
                begin
                    break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))
    def test_break_not_in_loop_5(self):
        input = """
                procedure main ();
                begin
                end
                function foo():integer;
                begin
                    with a:integer; do a:=1; break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,456))
    def test_break_not_in_loop_6(self):
        input = """
                procedure main ();
                begin
                end
                function foo():integer;
                var a:integer;
                begin
                    for a:=1 to 5 do begin
                        if a > 1 then a := 3; else break;
                    end
                    break;
                end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,457))
    def test_continue_not_in_loop_1(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                var a: array [3 .. 5] of integer;
                begin
                    continue;
                end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,458))
    def test_continue_not_in_loop_2(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                begin
                    if True then continue;
                end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,459))
    def test_continue_not_in_loop_3(self):
        input = """
                procedure main ();
                begin
                end
                procedure foo();
                var a:integer;
                begin
                    if True then a := 1; else continue;
                end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_continue_not_in_loop_4(self):
        input = """
                procedure main ();
                begin
                end
                function foo():integer;
                begin
                    continue;
                end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_Noentrypoint_1(self):
        """More complex program"""
        input = """
        var x: array [1 .. 2] of integer;var c:real;var d:integer;
        function main1():   integer;
        begin return 1; end
        function main (e:integer): real; begin
           return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,462))
    def test_Noentrypoint_2(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                    a:=1;
                    break;
                    abcd[1]:=1;       
                end"""
                        
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_Noentrypoint_3(self):
        """More complex program"""
        input = """
        var x: array [1 .. 2] of integer;var c:real;var d:integer;
        function main1():   integer;
        begin return 1; end
        function main (e:integer): real; begin
           return 1;
        end
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,464))
    def test_undeclare(self):
        """More complex program"""
        input = """
        procedure Main32( c: real);    //1
        var Main32: real;       //2               
        begin 
                if true then Main32(1);   
        end
        procedure Main( c: real);    //1
              
        begin   
        end
        """
        expect = "Undeclared Procedure: Main32"
        self.assertTrue(TestChecker.test(input,expect,465))
    def test_funtionNotReturn_1(self):
        """More complex program"""
        input = """
        function Main32( c: real):real;    //1
        var Main32: real;       //2               
        begin 
                if true then Main32:=1;   
        end
        procedure Main( c: real);    //1    
        begin   
        end
        """
        expect = "Function Main32Not Return "
        self.assertTrue(TestChecker.test(input,expect,466))
    def test_funtionNotReturn_2(self):
        """More complex program"""
        input = """
                var abc : array[1 .. 100] of integer;
                function foomeyoko(a : integer;b:array[1 .. 100] of integer) : integer;
                begin
                    if a = 1 then return -234;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                         a := Foo(abc[1],abc);
                         a :=  Foo(a,abcd);       
                end"""
                        
        expect = "Function foomeyokoNot Return "
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_funtionNotReturn_3(self):
        """More complex program"""
        input = """
                var abc : array[1 .. 100] of integer;
                function foomeyoko(a : integer;b:array[1 .. 100] of integer) : integer;
                begin
                    if a = 1 then return -234;
                    else a:=1;
                    return 1;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                         a := Foo(abc[1],abc);
                         a :=  Foo(a,abcd);       
                end"""
                        
        expect = "Function foomeyokoNot Return "
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_noentrypoint_4(self):
        input = """var a: integer;
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,469))
    def test_noentrypoint_5(self):
        input = """var a: integer;
                    var b:integer;
                    procedure min (); begin
                    end
                    function main (): integer; begin
                    return 1;
                    end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_noentrypoint_6(self):
        """More complex program"""
        input = """
                procedure notnotMain();
                begin
                    g:= notmain();
                    return ;
                end
                function notmain():integer;
                begin
                    while(Not True) do return 1;
                    g:=1;
                    return g;
                end
                procedure _main();
                Begin
                    notnotmain();
                end
                var g:integer;
                """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_470(self):
        """More complex program"""
        input = """
        var main : integer;
                procedure notnotMain();
                begin
                    g:= notmain();
                    return ;
                end
                function notmain():integer;
                begin
                    while(Not True) do return 1;
                    g:=1;
                    return g;
                end
                procedure _main();
                Begin
                    notnotmain();
                end
                var g:integer;
                """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_471(self):
        """More complex program"""
        input = """
                procedure notnotMain();
                begin
                    g:= main();
                    return ;
                end
                function main():integer;
                begin
                    while(Not True) do return 1;
                    g:=1;
                    return g;
                end
                procedure _main();
                Begin
                    notnotmain();
                end
                var g:integer;
                """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_noentrypoint_7(self):
        """More complex program"""
        input = """
                procedure notnotMain();
                begin
                    g:= notmain();
                    return ;
                end
                function notmain():integer;
                begin
                    while(Not True) do return 1;
                    g:=1;
                    return g;
                end
                procedure main(param : integer);
                Begin
                    notnotmain();
                end
                var g:integer;
                """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,474))
    def test_noentrypoint_8(self):
        """More complex program"""
        input = """
                function foo():integer;
                begin
                    return 1;
                end
                procedure main(q:integer);
                var a,i,n:integer;
                Begin
                    return;
                end       
            """
                        
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,475))
    
    def test_typemismatchStmt_21_return(self):
        """More complex program"""
        input = """
                function foo():integer;
                begin
                    return foo2();
                end
                function foo2():integer;
                begin
                    return foo();
                end
                procedure main();
                var a,i,n:integer;
                Begin
                    return a;
                end       
            """
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,476))
    def test_typemismatchStmt_22_return (self):
        input = """
                procedure main ();
                begin
                end
                function foo(): array [1 .. 5] of integer;
                var a: array [1 .. 2] of integer;
                begin
                    return a;
                end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,477))
    def test_typemismatchStmt_23_return (self):
        input = """
                procedure main ();
                begin
                end
                function foo(): array [1 .. 5] of integer;
                var a: array [3 .. 5] of integer;
                begin
                    return a;
                end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_typemismatchStmt_24_return(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of integer;
                Begin
                    abcd[abcd[a]]:=a;
                    return abcd;
                end"""
                        
        expect = "Type Mismatch In Statement: Return(Some(Id(abcd)))"
        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_typemismatchStmt_25_return(self):
           
        input = """
                procedure main();
                var a,i:integer;
                abcd : array[1 .. 100] of real;
                Begin
                    
                    while(a>0)do
                    begin
                       
                        if i = abcd[1] then 
                        continue;
                        else break;
                    end
                    return "a";
                end
                """
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(a)))"
        self.assertTrue(TestChecker.test(input,expect,480))
    def test_typemismatchStmt_26_assign(self):
           
        input = """
                function foo(): array [1 .. 2] of real;
               var a,x:REAl;
                    b:array [1 .. 2] of real;
                begin
                    return b;
                end
                procedure main();
                var a,x:REAl;
                    b:array [1 .. 2] of real;
                    c:integer;

                Begin
                    a := b[10] := foo ()[3] := x := 1 ;
                   
                    c := 2/2;
                    return ;
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(/,IntLiteral(2),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_typemismatchStmt_27_assign(self):
           
        input = """
                function foo(): array [1 .. 2] of real;
               var a,x:REAl;
                    b:array [1 .. 2] of real;
                begin
                    return b;
                end
                procedure main();
                var a,x:REAl;
                    b:array [1 .. 2] of real;
                    c:integer;

                Begin
                    a := b[10] := foo ()[3] := x := 1 ;
                   
                    c := 2/2;
                    return ;
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(/,IntLiteral(2),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,482))
    def test_typemismatchexpr(self):
        """More complex program"""
        input = """
                function foo(): Boolean;
                var abc : Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of integer;
                Begin
                    foo()[1]:=true;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_typemismatchStmt_28_assign(self):
        """More complex program"""
        input = """
                procedure main();
                var a:integer;
                Begin
                    a := 1+2;
                    a := 1 + 1.2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_typemismatchExp_16_BinaryOp(self):
        """More complex program"""
        input = """
                procedure main();
                var a:REAl;
                Begin
                    a := 1+2;
                    a := True + 1.2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(True),FloatLiteral(1.2))"
        self.assertTrue(TestChecker.test(input,expect,485))
    
    def test_typemismatchStmt_29_assign(self):
        """More complex program"""
        input = """
                function foo():String;
                begin
                    return "abc"; 
                end
                procedure main();
                var a:REAl;
                    b:boolean;
                Begin
                    a := 1.1+2.3;
                    b := true and false;
                    b := (1<2) and true;
                    a := foo();
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,486))
    
    def test_typemismatchStmt_30_assign(self):
        """More complex program"""
        input = """
                procedure main();
                var a:REAl;
                    b:boolean;
                    c:integer;
                Begin
                    c :=  3 mod 2 div 4;
                    b := (1<2.1) and (1+1 = 2) and b;
                    a := c + 1.2;
                    c := 2/2;
                    return ;
                end"""
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(/,IntLiteral(2),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,487))
    def test_typemismatchExp_17_callexpr(self):
        """More complex program"""
        input = """
                function foo(a : integer;b,c:real) : boolean;
                var abc : Boolean;
                begin
                    return abc;
                end
                procedure main();
                var a,b:boolean;
                Begin
                        g := 123;
                        a :=Foo(1,2.2,2,2);       
                end
                var g : integer;"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[IntLiteral(1),FloatLiteral(2.2),IntLiteral(2),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_typemismatchExp_18_callexpr(self):
        """More complex program"""
        input = """
                function foo(a : String;b,c:real;d:boolean) : integer;
                var abc : integer;
                begin
                    return abc + 100 ;
                end
                procedure main();
                var a:integer;
                    b:boolean;
                Begin
                        a := Foo("ok con de",2.2,2,not True);
                        b := Foo("ok con de",a,b,True);
                               
                end"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[StringLiteral(ok con de),Id(a),Id(b),BooleanLiteral(True)])"
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_typemismatchExp_19_CallExpr(self):
        """More complex program"""
        input = """
                var abc : array[1 .. 100] of real;
                function foo(a : integer;b:array[1 .. 100] of real): real;
                begin
                    return b[2];
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 1000] of real;
                Begin
                        abcd[1] := Foo(a,abc);
                        abcd[2] := Foo(a,abcd);       
                end"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[Id(a),Id(abcd)])"
        self.assertTrue(TestChecker.test(input,expect,490))
    def test_typemismatchExp_20_Callexpr(self):
        """More complex program"""
        input = """
                var abc : array[1 .. 100] of integer;
                function foo(a : integer;b:array[1 .. 100] of integer) : integer;
                begin
                    return -234;
                end
                procedure main();
                var a:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                         a := Foo(abc[1],abc);
                         a :=  Foo(a,abcd);       
                end"""
                        
        expect = "Type Mismatch In Expression: CallExpr(Id(Foo),[Id(a),Id(abcd)])"
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_typemismatchStmt_28_call(self):
        """More complex program"""
        input = """
          
            procedure mai1n(b:real;c:String);
                var a:integer;
                Begin end   
            procedure main(a:real);
                var b:integer;
                Begin  mai1n ("a","xx"); end                    
            """
                        
        expect = "Type Mismatch In Statement: CallStmt(Id(mai1n),[StringLiteral(a),StringLiteral(xx)])"
        self.assertTrue(TestChecker.test(input,expect,492))
    def test_typemismatchStmt_32_assign(self):
        input = """
                procedure main();
                var a,b : integer;
                    c : array[1 .. 100] of integer;
                    d : real;
                    Begin
                        d:= 3.14;
                        d:=314;
                        d:=a;
                        c[1] := 2;
                        d := True;
                end"""

        expect = "Type Mismatch In Statement: AssignStmt(Id(d),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,493))
    def test_typemismatchStmt_33_call(self):
        input = """
                procedure notmain(a:string);
                begin
                    while (not true) do putIntLn(a);
                end
                procedure main();
                begin
                end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,494))
    def test_typemismatchStmt_34_return (self):
        input = """
                function notmain(a:string): integer;
                begin
                    return a;
                end
                procedure main();
                begin
                end
        """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_typemismatchStmt_35_return (self):
        input = """
                procedure main ();
                begin

                end
                function s(a:integer; b:real):integer;
                var c:integer;
                    d:real;
                begin
                    return;
                end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_typemismatchStmt_36_assign(self):
        """More complex program"""
        input = """
                procedure main();
                var a,i,n:integer;
                Begin
                    while true do
                    Break ;
                    a:=1.1;
                end       
            """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_typemismatchStmt_37_return(self):
        """More complex program"""
        input = """
                procedure main();
                var a,i:integer;
                 abcd : array[1 .. 100] of real;
                Begin
                    for i := 1 to 100 do
                    begin
                        a:=1;
                        abcd[1]:=1;
                        break;
                    end
                    while(a>0)do
                    begin
                        a:=i -i +i;
                        abcd[1]:=1;
                        if i = abcd[1] then 
                        continue;
                        else break;
                    end
                    return "a";
                end"""
                        
        expect = "Type Mismatch In Statement: Return(Some(StringLiteral(a)))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_typemismatchStmt_return(self):
        """More complex program"""
        input = """  function foo(): array [1 .. 2] of real;
               var a,x:REAl;
                    b:array [1 .. 2] of real;
                begin
                    return b;
                end
                procedure main();
                var a,x:REAl;
                    b:array [1 .. 2] of real;
                    c:integer;

                Begin
                    a := b[10] := foo ()[3] := x := 1 ;
                   
                    c := 2/2;
                    return ;
                end
                """
                        
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),BinaryOp(/,IntLiteral(2),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,499))

