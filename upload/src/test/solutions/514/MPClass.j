.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.0
	ldc 2.0
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ldc 2.0
	ldc 1.0
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	invokestatic io/putBool(Z)V
	ldc 1.0
	ldc 1.0
	fcmpl
	iflt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_2
	iconst_1
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ior
	invokestatic io/putBool(Z)V
	iconst_0
	iconst_1
	iconst_0
	iand
	ior
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 14
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
