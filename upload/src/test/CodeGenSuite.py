import unittest
from TestUtils import TestCodeGen
from AST import *
from CodeGenError import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
        input = Program([VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),FloatType()),
          FuncDecl(Id("main"),[],[],[
              CallStmt(Id("putInt"),[IntLiteral(5)]),
                CallStmt(Id("putInt"),[IntLiteral(6)]),

                ]

                )])
        expect = "56"
        self.assertTrue(TestCodeGen.test(input,expect,501))
  
    def test_putString(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putString"),[StringLiteral("abc")])
                ]
                )])

        expect = "abc"
        self.assertTrue(TestCodeGen.test(input,expect,502))   

    def test_float_ast_(self):
        input = Program([
            FuncDecl(Id("main"),[],[],[
                CallStmt(Id("putFloat"),[FloatLiteral(5.0)])])])
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_exp(self):
        input = Program([
          FuncDecl(Id("main"),[],[],[
              CallStmt(Id("putFloat"),[BinaryOp("+", FloatLiteral(4.0), FloatLiteral(6.0))])])])
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_assign_ast(self):
        input = Program([VarDecl(Id("a"),IntType()),FuncDecl(Id("main"),[],[],[Assign(Id("a"),IntLiteral(5)),CallStmt(Id("putInt"),[Id("a")])],VoidType())])
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    
    def test_var_putBool_7(self):
        input = """
            var a:boolean;
            procedure main();
            begin
                a := FaLsE;
                putBool(a);
            end
        """
        expect="false"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_bin_add(self):
        input = """procedure main(); begin
            putInt(1 + 3);
        end"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_bin_mul(self):
        input = """procedure main(); begin
            putInt(1 * 3);
        end"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_bin_sub(self):
        input = """procedure main(); begin
            putInt(1 - 3);
        end"""
        expect = "-2"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    
    def test_bin_div(self):
        input = """procedure main(); begin
            putFloat(1/2);
        end"""
        expect = "0.5"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_bin_addF(self):
        input = """procedure main(); begin
            putFloat(1+2.1);
        end"""
        expect = "3.1"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_bin_subF(self):
        input = """procedure main(); begin
            putFloat(1.0-4.1);
        end"""
        expect = "-3.1"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    
    def test_bin_mulF(self):
        input = """procedure main(); begin
            putFloat(1.1 * 4);
        end"""
        expect = "4.4"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_binaryop_mul_2(self):
        input=Program([
          FuncDecl(Id("main"),[],[],[
            CallStmt(Id("putInt"),[BinaryOp("*",IntLiteral(6),IntLiteral(3))])])])
        expect="18"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_binaryop_mul_3(self):
        input=Program([
          FuncDecl(Id("main"),[],[],[
            CallStmt(Id("putFloat"),[BinaryOp("*",FloatLiteral(6.1),FloatLiteral(2.3))])])])
        expect="14.03"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_binaryop_div_1(self):
        input=Program([
          FuncDecl(Id("main"),[],[],[
            CallStmt(Id("putFloat"),[BinaryOp("/",IntLiteral(6),IntLiteral(3))])])])
        expect="2.0"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test_binaryop_div_2(self):
        input=Program([
          FuncDecl(Id("main"),[],[],[
            CallStmt(Id("putFloat"),[BinaryOp("/",FloatLiteral(6.0),IntLiteral(3))])])])
        expect="2.0"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_binaryop_div_3(self):
        input=Program([
          FuncDecl(Id("main"),[],[],[
            CallStmt(Id("putFloat"),[BinaryOp("/",IntLiteral(6),FloatLiteral(3.0))])])])
        expect="2.0"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_putBool_mutil1(self):
        input = """procedure main(); begin
            putBool(1 > 2);
            putBool(1 < 2);
            putBool(1 >= 1);
            putBool(1 <= 2);
            putBool(1 <> 2);
            putBool(1 = 2);
        end"""
        expect = """falsetruetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input,expect,519))
    
    def test_putBool_float(self):
        input = """procedure main(); begin
            putBool(1.0 > 2.0);
            
        end"""
        expect = """false"""
        self.assertTrue(TestCodeGen.test(input,expect,520))
    
    def test_putBool_mutil3(self):
        input = """procedure main(); begin
            putBool((1.0 > 2.0 ) and (2.0 > 1.0));
            putBool((1.0 >= 1.0 ) and (2 > 1));
            putBool(false and tRue);
        end"""
        expect = """falsetruefalse"""
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_putBool_mutil4(self):
        input = """procedure main(); begin
            putBool((1.0 > 2.0 ) or (2.0 > 1.0));
            putBool((1.0 >= 1.0 ) or (2 > 1));
            putBool(false or (tRue and false));
        end"""
        expect = """truetruefalse"""
        self.assertTrue(TestCodeGen.test(input,expect,522))
    
    def test_putInt_case_Insensitive1(self):
        input = """
        procedure notMain();
        begin
            putInt(12);
        end
        procedure main(); begin
            putINT(1);
            notMaiN();
        end"""
        expect = """112"""
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    def test_putInt_case_Insensitive2(self):
        input = """
        function notMain() : integer;
        begin
            putInt(12);
            return 1;
        end
        procedure main(); begin
            putINT(notMain());
            
        end"""
        expect = """121"""
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_var_decl_gen(self):
        input="""
        var
          a: integer;
        procedure main();
                         begin
                         a:=1;
                         putInt(a);
                         end
        """
        expect="1"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_local_var_decl_gen(self):
        input="""
        var
          a: integer;
        procedure main();
                         begin
                         foo(2);
                         end
        procedure foo (x:integer); begin  x:=3; putInt(x); end
        """
        expect="3"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_local_var_decl_gen_2(self):
        input="""
        var
          a: integer;
        procedure main();
                         begin
                         foo(2);
                         end
        procedure foo (x:integer);
        var
         b:integer; 
         begin  b:=10; putInt(b); end
        """
        expect="10"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    
    
   

    def test_ass_stmt(self):
      input="""
      var
        x: real;
         procedure main();
                          begin
                             x:= 3 +5;
                             putFloat(x);
                          end
        """
        
      expect="8.0"
      self.assertTrue(TestCodeGen.test(input,expect,528))

   

    def test_float_var_decl_gen(self):
        input="""
        var
        x: real;
         procedure main();
                          begin
                          x := 2;
                          putFloat(x);
                          end
        """
        
        expect="2.0"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_bop_DIV(self):
        input="""
        procedure main();
                         begin
                         putInt(3 div 2);
                         end
        """
        expect="1"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_bop_DIV_2(self):
        input="""
        procedure main();
                         begin
                         putInt(3 div 5);
                         end
        """
        expect="0"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    def test_withstmt1(self):
        input = """
        
        procedure main();
        begin
            with a:integer ; do
            a:=1;
            putInt(1);
        end
        
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect,532))
    
    def test_withstmt2(self):
        input = """
        
        procedure main();
        begin
            with a:integer ; do
            begin
                a:=1;
                putInt(a + 1);
            end
        end
        
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_withstmt3(self):
        input = """
        
        procedure main();
        var a : integer;
        begin
            a:=2;
            with a:integer ; do
            begin
                a:=1;
                putInt(a);
            end
            putInt(A);
        end
        
        """
        expect = """12"""
        self.assertTrue(TestCodeGen.test(input,expect,534))
    
    def test_withstmt4(self):
        input = """
        
        procedure main();
        var a ,b: integer;
        begin
            a:=2;
            b:=4;
            with a:integer ;c:real; do
            begin
                a:=1;
                c:=b;
                putInt(a);
                putFloat(c + a);
            end
            putInt(A);
        end
        
        """
        expect = """15.02"""
        self.assertTrue(TestCodeGen.test(input,expect,535))
    
    def test_withstmt5(self):
        input = """
        
        procedure main();
        var a ,b: integer;
        begin
            a:=2;
            b:=4;
            with a:boolean ;c:boolean; do
            begin
                a:=true;
                c:=false;
                putbool(a and then c);
                putbool(c and then a);
                putbool(c or else a);
                putbool(a or else c);
            end
            putInt(A);
        end
        
        """
        expect = """falsefalsetruetrue2"""
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_whileStmt1(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        d:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            end
        putint(c);
        end"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_whileStmt2(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        d:=9;
        c:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            end
        putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    
    
    
    def test_whileStmt3(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:integer;
        begin 
        d:=0;
        c:=0;
        for i:=0 to 0 do 
            begin 
            c:=c+i;
           
            end
        putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    def test_whileStmt4(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            break;
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_whileStmt5(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=2;
        while d<=3 do 
            begin 
            break;
            c:=c+d;
            d:=d+1;
            break;
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_whileStmt6(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=2;
        while d<=3 do 
            begin 
            d:=d+1;
            continue;
            
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_IfStmt1(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        if d<c then 
        putint(d); else putint(c);
        end"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_IfStmt2(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        if d<c then c:=c+1; else c:=c-1-2;
        putint(c);
        end"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_IfStmt3(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        while d<>0 do
        begin
        if d<c then c:=c+1; else c:=c-1-2;
        d:=d-1;
        end
        putint(c);
        end"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_withStmt_mutil1(self):
        
        input = """
        var d,a: integer;
        function aaa(x:real;y:real): real;
        begin  
            return 2.0; 
        end
        var c:real;
        procedure main1(c:real);
        begin end
        procedure main(); 
        var a:real;
        begin 
        main1(2.0);
        a:=2; c:=2;
        with a:integer; do begin a:=4;  with a:real ; do begin a:=3;  end end
        a:=aaa(2.0,2.0);
        putfloat(2.0);
        end    
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_whileStmt(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            a:=0;
            while a < 10 do
            begin
                a:=a+1;
                putInt(a);
            end
        end
        
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_For_Stmt1(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=1 to 10 do
                putInt(a);
        end
        
        """
        expect = """12345678910"""
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_For_Stmt2(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=10 downto 1 do
                putInt(a);
        end
        
        """
        expect = """10987654321"""
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    def test_For_Stmt3(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=10 downto 1 do
                if a < 2 then continue;
                else putint(a);
        end
        
        """
        expect = """1098765432"""
        self.assertTrue(TestCodeGen.test(input,expect,551))
    
    def test_For_Stmt4(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=1 to 10 do
                if a < 4 then continue;
                else putint(a);
        end
        
        """
        expect = """45678910"""
        self.assertTrue(TestCodeGen.test(input,expect,552))
    
    def test_For_Stmt5(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=10 downto 1 do
                if a < 5 then break;
                else putint(a);
        end
        
        """
        expect = """1098765"""
        self.assertTrue(TestCodeGen.test(input,expect,553))
    
    def test_For_Stmt6(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=1 to 10 do
                if a > 7 then break;
                else putint(a);
        end
        
        """
        expect = """1234567"""
        self.assertTrue(TestCodeGen.test(input,expect,554))
    
    def test_For_Stmt7(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            a:=0;
            while a < 10 do
            begin
                a:=a+1;
                if (a > 2) and (a < 7) then continue;
                else
                putInt(a);
            end
        end
        
        """
        expect = """1278910"""
        self.assertTrue(TestCodeGen.test(input,expect,555))
    
    def test_If_break(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            a:=0;
            while a < 10 do
            begin
                a:=a+1;
                if  (a > 7) then break;
                else
                putInt(a);
            end
        end
        
        """
        expect = """1234567"""
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_For_downto(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        
        for i:=9 downto 1 do 
        begin 
        
        putint(i);
        end
        
        end"""
        expect = "987654321"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_For_exp_mod(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if i mod 2 =0 then putint(i);
        end
        end"""
        expect = "8642"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_For_exp_div_and_mod(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i div 2)mod 2 =0 then putint(i);
        end
        end"""
        expect = "98541"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_For_continue(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i =3) then continue;
            putint(i);
        end
        end"""
        expect = "98765421"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_Downto_break(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i =3) then break;
            putint(i);
        end
        end"""
        expect = "987654"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_For_assign(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            c:=c*2;
            
        end putint(c);
        end"""
        expect = "512"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_assign_epression(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            c:=c-1;c:=c+1;
           c  := --------c * 2;
        end putint(c);
        end"""
        expect = "512"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_If_Assign(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
           if i mod 2 =0 then c:=c+1;
           else c:=c-1;
        end putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_While_and_With(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            while i<>9 do begin i:=9; with a:integer; do putint(c); end
        end 
        
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_simple_None(self):
        
        input = """
        procedure main(); 
        begin 
        end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_If_Boolen_putInt(self):
        
        input = """
        procedure main(); 
        begin 
            if  true then 
                if true then putint(1);
                else  putint(2);
            else  putint(3);
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_Return_in_If(self):
        
        input = """
        procedure main1(); 
        begin 
            if  true then 
               return;
            else  return;
        end
        procedure main(); 
        begin 
        main1();
            if  true then 
               return;
            else  return;
        end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_CallStmt_Callexpr(self):
        input = """
        procedure main2(); 
        begin 
          
               return;
           
        end
        function main1():integer; 
        begin 
            if  true then 
               return 1;
            else  
            return 2;
            
        end
        procedure main(); 
        begin 
        main2();
            if  not true then 
               return;
            else  
            putint(main1());
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_Float_coer_int(self):
        
        input = """
        procedure main(); 
        var i,j:integer;
        begin 
        i:=7; j:=2;
            putfloatln(9/3.0);
             putfloatln(9.0/3.0);
             putfloatln(9.0/3);
            putfloatln(6/3+ 1.5/3);
             putfloatln(i /(j+5));
        end"""
        expect = "3.0\n3.0\n3.0\n2.5\n1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    
    def test_Assign_Call(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure foo(a : integer);
        begin
        a:=123;
        end
     
        procedure main(); 
        var a:integer;
        begin 
            
            a:=1;
        foo(a);
        putINT(a);
             
        end
        """
        expect="1"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_If_in_For(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=10 downto 1 do
                if a < 2 then continue;
                else putint(a);
        end
        
        """
        expect = """1098765432"""
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_Conitnue_in_FOr(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=1 to 10 do
                if a < 4 then continue;
                else putint(a);
        end
        
        """
        expect = """45678910"""
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_Downto_Break(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=10 downto 1 do
                if a < 5 then break;
                else putint(a);
        end
        
        """
        expect = """1098765"""
        self.assertTrue(TestCodeGen.test(input,expect,574))
    
    def test_Forto_Break_call(self):
        input = """
        procedure main();
        var a ,b: integer;
        begin
            for a:=1 to 10 do
                if a > 7 then break;
                else putint(a);
        end
        
        """
        expect = """1234567"""
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_Call_complex(self):
        input = """
        function foo(a,b:real;c:boolean):boolean;
                    Begin
                        return (A>=b) and c;
                    end
        procedure main();
                    Begin
                        putBool(foo(1+1,1.0+0.1,true));
                        putBool(foo(1+1,1.0+0.1,not true));
                        return;
                    end
        """
        expect = """truefalse"""
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_Call_complex2(self):
        input = """
        function foo(a,b:real;c:boolean):real;
                    Begin
                        if c then
                        return (A - b);
                        else return a+B;
                    end
        procedure main();
                    Begin
                        putFloat(foo(1+1,1.0+0.1,true));
                        putFloat(foo(1+1,1.0+0.1,not true));
                        return;
                    end
        """
        expect = """0.93.1"""
        self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_Pustring_simple(self):
        input = """
        procedure main();
            Begin
                putString("hello world !!!");
            end
        """
        expect = """hello world !!!"""
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_With_localpara(self):
        input = """
        procedure main();
                Begin
                    with a,b:integer; do
                    begin
                        b:=2;
                        a:=b+5;
                        putint(a);
                        putint(A+b);
                    end
                end
        """
        expect = """79"""
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_assign_and_if_in_WihtStmt(self):
        input = """
        procedure main();
                    Begin
                        with a,b:integer; do
                        begin
                            b:=1080;
                            a:=b mOD 1000;
                            if true then
                            putint(a);
                        end
                    end
        """
        expect = """80"""
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_Wiht_In_If(self):
        input = """
        procedure main();
                    Begin
                    if true then 
                        with a_:string;a,b:integer; do putint(1);
                    else with _a:string;a,b:integer; do putint(2);
                    end
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_mutilStmt1(self):
        input = """
        procedure main();
        var i:integer;
                    Begin
                    for i:= 2 to 3 do
                        with a,b:integer; do 
                        begin
                            b:=i;
                            a:=b*b;
                            putint(a);
                        end
                    end
        """
        expect = """49"""
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_mutilStmt2(self):
        input = """
        procedure main();
                    Begin
                        with i,b:integer; do 
                        for i:= 7 to 9 do putint(i);
                    end
        """
        expect = """789"""
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_mutilStmt3(self):
        input = """
        procedure main();
                    Begin
                        with n:integer; do begin
                            n:=7 ;

                            while (n>=7) and (n<=9) do begin putint(n); n:=n+1; end
                        end
                    end
        """
        expect = """789"""
        self.assertTrue(TestCodeGen.test(input,expect,584))
    
    def test_mutilStmt4(self):
        input = """
        procedure main();
        var n : integer;
                    Begin
                        n:=7 ;

                            while (n>=7) and (n<=9) do begin
                        with n:integer; do begin
                            n:=9;
                            begin putint(n); n:=n+1; end
                        end n:=n+1; end
                    end
        """
        expect = """999"""
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_mutilStmt5(self):
        input = """
        var a ,b,c: real; out:boolean;
        function foo(c:real): real;
        begin return 1.2;return 1.3; end
        procedure main();
        begin
                c:=a:=foo(1)+foo(foo(foo(foo(foo(1)))));
                putfloatln(c/2);putFloatln(a/2);
        end
        
        """
        expect = """1.2\n1.2\n"""
        self.assertTrue(TestCodeGen.test(input,expect,586)) 
    def test_mutilStmt6(self):
        input = """
        var a ,b,c: real; out:boolean;
        function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
        begin
                c:=1;
                if c<>3 then 
                    if c<0 then 
                    putfloatln(c/2);
                    else c:=foo(0);
                putfloatln(c);
        end
        
        """
        expect = """1.3\n"""
        self.assertTrue(TestCodeGen.test(input,expect,587)) 
    def test_mutilStmt7(self):
        input = """
        var a ,b,c: real; out:boolean;
        function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
        begin c:=0;
               while true do begin c:=3; if c=3 then break; else continue; end
                if c<>3 then begin end
                else while c=3 do begin putfloat(c);c:=c-1; break; end
        end
        
        """
        expect = """3.0"""
        self.assertTrue(TestCodeGen.test(input,expect,588)) 
    def test_mutilStmt8(self):
        input = """
        var a ,b,c: real; out:boolean;
        function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
        begin   c:=foo(1------------------------------------3);
               putfloatLN(c/c); 
                return;

        end
        
        """
        expect = """1.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,589)) 
    def test_mutilStmt9(self):
        input = """
        var a ,b,c: real; out:boolean;
        function foo(c:integer): boolean;
        begin if c mod 2 =0 then return TRUE; else return FaLSE; end
        procedure main();
        begin   out:=foo(1024);
               if out then putstring("so chan");

            else putstring("so 0 chan");
        end
        
        """
        expect = """so chan"""
        self.assertTrue(TestCodeGen.test(input,expect,590)) 
    def test_mutilStmt10(self):
        input = """
        var a ,b,c: real; out:boolean;
        
        procedure main();
        begin  
                putfloat(1/2/2);
        end
        
        """
        expect = """0.25"""
        self.assertTrue(TestCodeGen.test(input,expect,591)) 
    def test_mutilStmt11(self):
        input = """
        Function sum(n:integer):integer;
        var sum :integer;
        begin
            sum:=0;
            with i:integer; do
            for i:= 0 to n do sum := sum + i;
            return sum; 
        end
        procedure main();
        var a :integer;
        begin
            a:=123;
            
            putINT(SUM(a));
        end
        """
        expect = """7626"""
        self.assertTrue(TestCodeGen.test(input,expect,592))
    def test_mutilStmt12(self):
        input = """
        procedure main();
        var a,b :real;
        begin
            a:=b:=10000.01;
            if a= 0 then putString("ptvn");
            else putFloat(-b/a);
            a:=b:=0;
            if a= 0 then putString("ptvn");
            else putFloat(-b/a);
        end
        """
        expect = """-1.0ptvn"""
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_mutilStmt13(self):
        input = """
        Function tbc(n:integer):real;
        var sum :integer;
        begin
            sum:=0;
            with i:integer; do
            for i:= 0 to n do sum := sum + i;
            return sum/n; 
        end
        procedure main();
        var a,b :real;
        begin
            
            putFloat(tbc(10));
        end
        """
        expect = """5.5"""
        self.assertTrue(TestCodeGen.test(input,expect,594))
    def test_mutilStmt14(self):
        input = """
        var i :integer;
        function f (): integer;
        begin 
            return 200;
        end
        procedure main();
        var 
        main: integer; 
        begin 
            main := f (); 
            putIntLn(main); 
            with i :integer; 
            main:integer; 
            f :integer;
            do begin  
                main := f := i := 100; 
                putIntLn( i ); 
                putIntLn(main); 
                putIntLn(f ); 
            end  
            putIntLn(main);  
        end 
        var g: real ;
        """
        expect = """200\n100\n100\n100\n200\n"""
        self.assertTrue(TestCodeGen.test(input,expect,595))
    def test_mutilStmt15(self):
        input = """
        
        procedure main();
        Var 
            i,j : integer;
        BEGIN
              
             FOR i:= 1 TO 10 DO
             Begin
              FOR j:=1 TO i DO putString("*");
              PutLN();
            End
        END
        """
        expect = """*
**
***
****
*****
******
*******
********
*********
**********
"""
        self.assertTrue(TestCodeGen.test(input,expect,596))
    def test_mutilStmt16(self):
        input = """
        
        procedure main();
        Var 
            i,j : integer;
        BEGIN
              
            i:=10;
            FOR j:=1 TO i DO 
            with i :integer; do
            begin putString("*");
            break;
            end
            
            
        END
        """
        expect = """*"""
        self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_mutilStmt17(self):
        input = """
        
        procedure main();
        Var 
            i,j : integer;
        BEGIN
              
            i:=10;
            FOR j:=1 TO i DO 
            while (j <> i) do
            begin putString("*");
            break;
            end
            
            
        END
        """
        expect = """*********"""
        self.assertTrue(TestCodeGen.test(input,expect,598))
    def test_mutilStmt18(self):
        input = """
        procedure main();
        BEGIN
            notmain("*********");
        END
        procedure notmain(a:string);
        begin
            putString(a);
        end
        """
        expect = """*********"""
        self.assertTrue(TestCodeGen.test(input,expect,599))
    