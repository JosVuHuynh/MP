.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iconst_4
	istore_2
Label2:
.var 3 is a Z from Label2 to Label3
.var 4 is c Z from Label2 to Label3
	iconst_1
	istore_3
	iconst_0
	istore 4
	iload_3
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iload 4
Label5:
	invokestatic io/putBool(Z)V
	iload 4
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iload_3
Label7:
	invokestatic io/putBool(Z)V
	iload 4
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iload_3
Label9:
	invokestatic io/putBool(Z)V
	iload_3
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iload 4
Label11:
	invokestatic io/putBool(Z)V
Label3:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
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
