.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(FFZ)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c Z from Label0 to Label1
Label0:
	iload_2
	ifle Label2
	fload_0
	fload_1
	fsub
	freturn
	goto Label3
Label2:
	fload_0
	fload_1
	fadd
	freturn
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	iadd
	i2f
	ldc 1.0
	ldc 0.1
	fadd
	iconst_1
	invokestatic MPClass/foo(FFZ)F
	invokestatic io/putFloat(F)V
	iconst_1
	iconst_1
	iadd
	i2f
	ldc 1.0
	ldc 0.1
	fadd
	iconst_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic MPClass/foo(FFZ)F
	invokestatic io/putFloat(F)V
	return
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
