.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static cv(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	fload_0
	fload_0
	fadd
	fload_1
	fadd
	fload_1
	fadd
	freturn
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	bipush 12
	i2f
	fstore_1
	ldc 0.01
	fstore_2
	ldc "cv hcn la: "
	invokestatic io/putString(Ljava/lang/String;)V
	fload_1
	fload_2
	invokestatic MPClass/cv(FF)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
