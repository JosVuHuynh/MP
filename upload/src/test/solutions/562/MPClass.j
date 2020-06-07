.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_1
	ifle Label2
	iconst_0
	ifle Label3
	iconst_1
	istore_1
	goto Label4
Label3:
	iconst_1
	ifgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	istore_1
Label4:
Label2:
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 9
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
