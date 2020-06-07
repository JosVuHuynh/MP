.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static notMain(F)V
.var 0 is d F from Label0 to Label1
.var 1 is e I from Label0 to Label1
Label0:
	ldc 9.9
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y I from Label0 to Label1
.var 3 is b Z from Label0 to Label1
Label0:
	ldc 1.2
	invokestatic MPClass/notMain(F)V
	iconst_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 4
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
