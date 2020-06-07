.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static sum(I)I
.var 0 is n I from Label0 to Label1
.var 1 is sum I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label6:
	iload_2
	iload_0
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_1
	iload_2
	iadd
	istore_1
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
	iload_1
	ireturn
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 123
	istore_1
	iload_1
	invokestatic MPClass/sum(I)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
