.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_0
	ireturn
Label4:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo(I)I
	iload_0
	iadd
	ireturn
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_2
	iadd
	iconst_2
	iadd
	iconst_2
	iadd
	iconst_2
	iadd
	invokestatic MPClass/foo(I)I
	invokestatic io/putInt(I)V
	return
Label1:
	return
.limit stack 2
.limit locals 1
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
