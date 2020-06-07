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
.var 1 is a I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is n I from Label0 to Label1
Label0:
	iconst_1
	istore_3
	iload_3
	istore_1
	iconst_1
	istore_2
Label4:
	iload_2
	iload_3
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_1
	iload_1
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iload_2
	iload_2
	invokestatic MPClass/notmain(II)V
	goto Label8
	goto Label7
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 6
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
