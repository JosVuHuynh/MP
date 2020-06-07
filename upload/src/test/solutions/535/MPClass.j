.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is r F from Label0 to Label1
.var 2 is a I from Label0 to Label1
Label0:
	iconst_2
	ineg
	istore_2
	iconst_1
	i2f
	fstore_1
	fload_1
	fneg
	fneg
	invokestatic io/putFloat(F)V
	iload_2
	ineg
	invokestatic io/putInt(I)V
	iconst_1
	ineg
	ineg
	ineg
	ineg
	ineg
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 3
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
