.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label2
Label4:
.var 1 is a_ Ljava/lang/String; from Label4 to Label5
.var 2 is a I from Label4 to Label5
.var 3 is b I from Label4 to Label5
	iconst_1
	invokestatic io/putInt(I)V
Label5:
	goto Label3
Label2:
Label6:
.var 1 is _a Ljava/lang/String; from Label6 to Label7
.var 2 is a I from Label6 to Label7
.var 3 is b I from Label6 to Label7
	iconst_2
	invokestatic io/putInt(I)V
Label7:
Label3:
Label1:
	return
.limit stack 2
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
