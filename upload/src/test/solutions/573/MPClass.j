.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is m I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	iconst_3
	istore_1
	iconst_1
	istore_2
	iload_1
	ineg
	istore_3
Label4:
	iload_3
	iload_2
	ineg
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload_3
	iconst_2
	ineg
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	iload_3
	ineg
	invokestatic io/putInt(I)V
	goto Label3
	goto Label10
Label9:
	iload_3
	invokestatic io/putInt(I)V
	goto Label2
Label10:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
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
