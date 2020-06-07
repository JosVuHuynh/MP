.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MPClass.a I
	iconst_4
	putstatic MPClass.b I
	bipush 12
	invokestatic io/putInt(I)V
	getstatic MPClass.a I
	getstatic MPClass.b I
	invokestatic MPClass/notmain(II)V
	invokestatic MPClass/notmain2()V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static notmain(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static notmain2()V
Label0:
	bipush 12
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 0
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
