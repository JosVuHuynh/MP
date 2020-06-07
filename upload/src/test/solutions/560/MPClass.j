.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static notmain(I)V
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
.var 4 is d I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iconst_1
	istore_2
	iload_1
	iload_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_2
	invokestatic MPClass/notmain(I)V
	goto Label5
Label4:
	iload_2
	istore_1
	iconst_1
	istore 4
	iload 4
	istore_3
	iload_1
	invokestatic MPClass/notmain(I)V
	iload_3
	invokestatic MPClass/notmain(I)V
Label5:
Label1:
	return
.limit stack 3
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
