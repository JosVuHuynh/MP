.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_2
	istore_2
	iload_1
	iload_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	i2f
	invokestatic io/putFloat(F)V
	goto Label5
Label4:
	iload_1
	i2f
	iload_2
	i2f
	fdiv
	invokestatic io/putFloat(F)V
Label5:
	iconst_1
	i2f
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 4
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
