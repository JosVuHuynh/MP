.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static notMain(IZZ)Z
.var 0 is d I from Label0 to Label1
.var 1 is e Z from Label0 to Label1
.var 2 is f Z from Label0 to Label1
Label0:
	iload_1
	iload_2
	iand
	invokestatic io/putBool(Z)V
	iload_0
	i2f
	ldc 1.2
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ireturn
Label1:
	return
.limit stack 3
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
	ldc 8.9
	fstore 4
	iconst_1
	istore_3
	iload_1
	fload 4
	iconst_1
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_3
	invokestatic MPClass/notMain(IZZ)Z
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 6
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
