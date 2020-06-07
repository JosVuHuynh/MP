.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iconst_4
	istore_2
Label2:
.var 3 is a I from Label2 to Label3
.var 4 is c F from Label2 to Label3
	iconst_1
	istore_3
	iload_2
	i2f
	fstore 4
	iload_3
	invokestatic io/putInt(I)V
	fload 4
	iload_3
	i2f
	fadd
	invokestatic io/putFloat(F)V
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 5
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
