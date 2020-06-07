.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	iconst_1
	i2f
	fstore_1
	iconst_2
	i2f
	fstore_2
	fload_1
	fload_2
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	fload_1
	iconst_5
	i2f
	fcmpl
	ifge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
	goto Label6
Label7:
	goto Label5
Label4:
Label10:
	fload_2
	iconst_5
	i2f
	fcmpl
	ifge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	fload_2
	iconst_1
	i2f
	fadd
	fstore_2
	goto Label10
Label11:
Label5:
	fload_1
	invokestatic io/putFloat(F)V
	fload_2
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
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
