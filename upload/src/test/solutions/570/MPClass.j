.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static notmain(II)V
.var 0 is i I from Label0 to Label1
.var 1 is j I from Label0 to Label1
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

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label0:
	iconst_2
	istore_2
Label2:
	iload_2
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_1
	istore_1
Label8:
	iload_1
	iload_2
	if_icmpgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
	iload_1
	iload_1
	invokestatic MPClass/notmain(II)V
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label7:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label2
Label3:
Label1:
	return
.limit stack 6
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
