.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static notMain(IFF)I
.var 0 is d I from Label0 to Label1
.var 1 is e F from Label0 to Label1
.var 2 is f F from Label0 to Label1
Label0:
	fload_1
	fload_2
	fadd
	invokestatic io/putFloat(F)V
	iload_0
	ireturn
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
.var 3 is b Z from Label0 to Label1
.var 4 is z F from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	i2f
	fstore 4
	fload 4
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
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
