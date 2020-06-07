.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i F
.field static n I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 40
	putstatic MPClass.n I
	iconst_1
	i2f
	putstatic MPClass.i F
Label2:
	getstatic MPClass.i F
	getstatic MPClass.n I
	i2f
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MPClass.i F
	getstatic MPClass.i F
	fadd
	putstatic MPClass.i F
	goto Label2
Label3:
	getstatic MPClass.i F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 4
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
