.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	bipush 7
	istore_1
Label2:
	iload_1
	bipush 7
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iload_1
	bipush 9
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ifle Label3
Label8:
.var 2 is n I from Label8 to Label9
	bipush 9
	istore_2
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	iconst_1
	iadd
	istore_2
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
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
