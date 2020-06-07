'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *   Name:Vũ Văn Huynh MSSV:1511328
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [     Symbol("getInt",MType(list(),IntType()),CName(self.libName)),
                     Symbol("putInt",MType([IntType()],VoidType()),CName(self.libName)),
                     Symbol("putIntLn",MType([IntType()],VoidType()),CName(self.libName)),
                     Symbol("getFloat",MType(list(),FloatType()),CName(self.libName)),
                     Symbol("putFloat",MType([FloatType()],VoidType()),CName(self.libName)),
                     Symbol("putFloatLn",MType([FloatType()],VoidType()),CName(self.libName)),
                     Symbol("putBool",MType([BoolType()],VoidType()),CName(self.libName)),
                     Symbol("putBoolLn",MType([BoolType()],VoidType()),CName(self.libName)),
                     Symbol("putString",MType([StringType()],VoidType()),CName(self.libName)),
                     Symbol("putStringLn",MType([StringType()],VoidType()),CName(self.libName)),
                     Symbol("putLn",MType(list(),(VoidType())),CName(self.libName))  
                    
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
   
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        self.key=0
        for x in ast.decl:
            e = self.visit(x, e)
        self.key=1

        for y in ast.decl:
            if not isinstance(y,VarDecl):
                e = self.visit(y, e)
        glo_env=e.sym
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), glo_env, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name.lower() == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x:x.varType,consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        #newGlenv=reduce(lambda x,y:emit.printout(emit.emitVAR(frame.getNewIndex,b.variable.name,b.varType,frame.getStartLabel,frame.getEndLabel,frame)),Symbol(b.variable.name,b.varType,Index(frame.index()-1))+x,ast.param,)
        varPara=SubBody(frame,glenv)
        for x in consdecl.param:
            varPara=self.visit(x,varPara)

        varLocal=SubBody(frame,varPara.sym)
        for y in consdecl.local:
            varLocal=self.visit(y,varLocal)

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, varLocal.sym)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitVarDecl(self,ast,o):
        subctxt = o
        frame=subctxt.frame
        genv=subctxt.sym
        if not frame:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name,ast.varType,False,""))
            return SubBody(None,[Symbol(ast.variable.name,ast.varType,CName(self.className))]+subctxt.sym)
        else:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),ast.variable.name,ast.varType,frame.getStartLabel(),frame.getEndLabel(),frame))
            sym=Symbol(ast.variable.name,ast.varType,Index(frame.getCurrIndex()-1))
            return SubBody(frame,[sym]+genv)
    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        if self.key==0:
            return SubBody(None, [Symbol(ast.name.name, MType(list(map(lambda y:y.varType,ast.param)),ast.returnType),CName(self.className))] + subctxt.sym)
        else:
            self.genMETHOD(ast, subctxt.sym, frame)
            return SubBody(None, [Symbol(ast.name.name, MType(list(map(lambda y:y.varType,ast.param)),ast.returnType),CName(self.className))] + subctxt.sym)
    
    def visitCallExpr(self,ast,o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        lst=list()
        for x in nenv:
            if isinstance(x.mtype,MType):
                lst.append(x)

        sym = self.lookup(ast.method.name.lower(), lst, lambda x:x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        returnType=sym.mtype.rettype
        
        paramIndex=-1
        i2f=""
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, False))

            paramIndex+=1
            if isinstance(typ1,IntType) and isinstance(sym.mtype.partype[paramIndex],FloatType):
                i2f=self.emit.emitI2F(frame)
            in_ = (in_[0] + str1+i2f,[])
            i2f=""
        result=in_[0]+self.emit.emitINVOKESTATIC(cname+"/"+sym.name,ctype,frame)

        return (result,returnType)

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        lst=list()
        for x in nenv:
            if isinstance(x.mtype,MType):
                lst.append(x)

        sym = self.lookup(ast.method.name.lower(),lst, lambda x:x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        returnType=sym.mtype.rettype
        paramIndex=-1
        i2f=""
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, False))
            paramIndex+=1
            if isinstance(typ1,IntType) and isinstance(sym.mtype.partype[paramIndex],FloatType):
                i2f=self.emit.emitI2F(frame)
            in_ = (in_[0] + str1+i2f, [])
            i2f=""
        result=in_[0]+self.emit.emitINVOKESTATIC(cname+"/"+sym.name,ctype,frame)
        self.emit.printout(result)
       

    def visitId(self,ast,o):
        subctxt=o
        sym=self.lookup(ast.name.lower(),o.sym,lambda x:x.name.lower())
        frame=subctxt.frame
        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame),sym.mtype
            elif not isinstance(sym.value,CName):
                return self.emit.emitWRITEVAR(sym.name,sym.mtype,sym.value.value,frame),sym.mtype
            else:
                return "",VoidType()
        else:
            if type(sym.value) is CName:
                return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name,sym.mtype,o.frame),sym.mtype
            elif not isinstance(sym.value,CName):
                return self.emit.emitREADVAR(sym.name,sym.mtype,sym.value.value,frame),sym.mtype
            else:
                return "",VoidType()
    
    

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)
        bufer=""
        genOp=""
        typ=None
        if ast.op.lower()!='andthen' and ast.op.lower()!='orelse':
            
            if ast.op in ['+','-','*']:
                if isinstance(lt,IntType) and isinstance(rt,FloatType):
                    bufer=lc+self.emit.emitI2F(frame)+rc
                    typ=FloatType()
                elif isinstance(lt,FloatType) and isinstance(rt,IntType):
                    bufer=lc+rc+self.emit.emitI2F(frame)
                    typ=FloatType()
                else:
                    bufer=lc+rc
                    typ=lt
            elif ast.op in ['=','<>','<','<=','>','>=']:
                typ=BoolType()
                if isinstance(lt,IntType) and isinstance(rt,FloatType):
                    bufer=lc+self.emit.emitI2F(frame)+rc
                elif isinstance(lt,FloatType) and isinstance(rt,IntType):
                    bufer=lc+rc+self.emit.emitI2F(frame)
                else:
                    bufer=lc+rc
                    
            elif ast.op in ['/']:
                typ=FloatType()
                if isinstance(lt,IntType) and isinstance(rt,IntType):
                    bufer=lc+self.emit.emitI2F(frame)+rc+self.emit.emitI2F(frame)  
                elif isinstance(lt,IntType) and isinstance(rt,FloatType):
                    bufer=lc+self.emit.emitI2F(frame)+rc
                elif isinstance(lt,FloatType) and isinstance(rt,IntType):
                    bufer=lc+rc+self.emit.emitI2F(frame)
                else:
                    bufer=lc+rc
            elif ast.op.lower() in ['div','mod']:
                if isinstance(lt,IntType) and isinstance(rt,IntType):
                    bufer=lc+rc
                    typ=IntType()

            elif ast.op.lower() in ['and','or']:
                if isinstance(lt,BoolType) and isinstance(rt,BoolType):
                    bufer=lc+rc
                    typ=BoolType()
            if ast.op=="+":
                genOp=self.emit.emitADDOP("+",typ,frame)
            elif ast.op=="-":   
                genOp=self.emit.emitADDOP("-",typ,frame)
            elif ast.op=="*":
                genOp=self.emit.emitMULOP("*",typ,frame)
            elif ast.op=="/":
                genOp=self.emit.emitMULOP("/",typ,frame)
            elif ast.op.lower()=="div":
                genOp=self.emit.emitDIV(frame)
            elif ast.op.lower()=="mod":
                genOp=self.emit.emitMOD(frame)
            elif ast.op.lower()=="and":
                genOp=self.emit.emitANDOP(frame)
            elif ast.op.lower()=="or":
                genOp=self.emit.emitOROP(frame)
            elif ast.op in ['=','<>','<','<=','>','>=']:
                if type(lt) is type(rt):
                    genOp=self.emit.emitREOP(ast.op,lt,frame)
                else:

                    genOp=self.emit.emitREOP(ast.op,FloatType(),frame)
        else:
            
            typ=BoolType()
            #SHORT CICRUIT
            rightLaBel = frame.getNewLabel()
            outLaBel = frame.getNewLabel()
            if (ast.op.lower() == "andthen"):
                bufer+=lc
                bufer+=self.emit.emitIFTRUE(rightLaBel, frame)  
                bufer+=self.emit.emitPUSHICONST(0,frame) 
                bufer+=self.emit.emitGOTO(outLaBel,frame)
                bufer+=self.emit.emitLABEL(rightLaBel, frame)
                bufer+=rc
                bufer+=self.emit.emitLABEL(outLaBel,frame)
                return bufer,typ
            elif (ast.op.lower() == "orelse"):
                bufer+=lc
                bufer+=self.emit.emitIFFALSE(rightLaBel, frame) 
                bufer+=self.emit.emitPUSHICONST(1,frame) 
                bufer+=self.emit.emitGOTO(outLaBel,frame)
                bufer+=self.emit.emitLABEL(rightLaBel, frame) 
                bufer+=rc
                bufer+=self.emit.emitLABEL(outLaBel,frame)
                return bufer,typ
        return bufer+genOp, typ
        
        

    def visitUnaryOp(self,ast,o):
        ctxt=o
        frame =ctxt.frame
        op=ast.op
        rc,rt=self.visit(ast.body,o)
      
        if op=="-":
            return rc+self.emit.emitNEGOP(rt,frame),rt
        else:
            return rc+self.emit.emitNOT(rt,frame),rt

    def visitAssign(self,ast,o):
        rc,rt = self.visit(ast.exp,Access(o.frame,o.sym,False,False))
        lc,lt = self.visit(ast.lhs,Access(o.frame,o.sym,True,False))
        if type(rt)is IntType and type(lt) is FloatType:
            self.emit.printout(rc+self.emit.emitI2F(o.frame)+lc)
        else:
            self.emit.printout(rc+lc)

    def visitIf(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        lenv=subtxt.sym
        els=ast.elseStmt
        access=Access(frame,lenv,False,False)
        self.emit.printout(self.visit(ast.expr,access)[0])
        if els==[]:
            label2=frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(label2, frame))
            for x in ast.thenStmt:
                self.visit(x,o)
            self.emit.printout(self.emit.emitLABEL(label2, frame))
        else:
            label1=frame.getNewLabel()
            label2=frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(label1, frame))
            for x in ast.thenStmt:
                self.visit(x,o)
            self.emit.printout(self.emit.emitGOTO(label2, frame))
            self.emit.printout(self.emit.emitLABEL(label1, frame))
            for y in ast.elseStmt:
                self.visit(y,o)
            self.emit.printout(self.emit.emitLABEL(label2, frame))
        
        
       

    def visitWhile(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        lenv=subtxt.sym
        access=Access(frame,lenv,False,False)
        frame.enterLoop()
        bk = frame.getBreakLabel()
        cont = frame.getContinueLabel()
        self.emit.printout(self.emit.emitLABEL(cont, frame))
        self.emit.printout(self.visit(ast.exp,access)[0])
        self.emit.printout(self.emit.emitIFFALSE(bk, frame))
        for x in ast.sl:
           self.visit(x,o)
        self.emit.printout(self.emit.emitGOTO(cont, frame))
        self.emit.printout(self.emit.emitLABEL(bk, frame))
        frame.exitLoop()
    
    def visitWith(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        frame.enterScope(False)
        retVarDecl=SubBody(frame,subtxt.sym)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        for x in ast.decl:
            retVarDecl=self.visit(x,retVarDecl)
        for y in ast.stmt:
            self.visit(y,retVarDecl)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        frame.exitScope()

    def visitFor(self,ast,o):
        if ast.up:
                up,op='<=','+'
        else:
                up,op='>=','-'
        bufer=""
        frame=o.frame
        frame.enterLoop()
        loopLabel=frame.getNewLabel()
        
        #sinh mã cho assign id=expr1
        expr1,lt=self.visit(ast.expr1,Access(o.frame,o.sym,False,False))
        # self.emit.emitLABEL(loopLabel,frame)
        expr2,rt=self.visit(ast.expr2,Access(o.frame,o.sym,False,False))
        bufer+=expr1
        bufer+=self.visit(ast.id,Access(o.frame,o.sym,True,False))[0]   
        bufer+=self.emit.emitLABEL(loopLabel,frame)

        #sinh mã cho binary <=,>= id,expr2
        bufer+=self.visit(ast.id,Access(o.frame,o.sym,False,False))[0] 
        bufer+=expr2
        bufer+=self.emit.emitREOP(up,IntType(),frame)
        bufer+=self.emit.emitIFFALSE(frame.getBreakLabel(),frame)
        self.emit.printout(bufer)
        for x in ast.loop:
            self.visit(x,o)
        bufer=""
        bufer+=self.emit.emitLABEL(frame.getContinueLabel(),frame)
        bufer+=self.visit(ast.id,Access(o.frame,o.sym,False,False))[0]
        bufer+=self.emit.emitPUSHICONST(1, frame)
        bufer+=self.emit.emitADDOP(op,IntType(),frame)
        bufer+=self.visit(ast.id,Access(o.frame,o.sym,True,False))[0] 
        bufer+=self.emit.emitGOTO(loopLabel,frame)
        bufer+=self.emit.emitLABEL(frame.getBreakLabel(),frame)
        self.emit.printout(bufer)
        frame.exitLoop()
        


    def visitBreak(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))

    def visitReturn(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        resultTyp=frame.returnType
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(),Frame))
        else:
            c,t=self.visit(ast.expr,Access(frame,subtxt.sym,False,False))
            self.emit.printout(c)
            if isinstance(resultTyp,FloatType) and isinstance(t,IntType):
                self.emit.printout(self.emit.emitI2F(frame))
                self.emit.printout(self.emit.emitRETURN(FloatType(),frame))
            else:
                self.emit.printout(self.emit.emitRETURN(t,frame))

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitStringLiteral(self,ast,o):
        #ast:StringLiteral
        ctxt=o
        frame=ctxt.frame
        return self.emit.emitPUSHCONST( ast.value,StringType(),frame), StringType()
        
    def visitBooleanLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()