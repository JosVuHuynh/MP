.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Z
.field static b Z
.field static r F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_1
	ior
	putstatic MPClass.a Z
	getstatic MPClass.a Z
	putstatic MPClass.b Z
	iconst_1
	i2f
	putstatic MPClass.r F
	getstatic MPClass.a Z
	invokestatic io/putBool(Z)V
	getstatic MPClass.b Z
	invokestatic io/putBool(Z)V
	getstatic MPClass.a Z
	getstatic MPClass.b Z
	iand
	invokestatic io/putBool(Z)V
	getstatic MPClass.a Z
	getstatic MPClass.b Z
	ior
	invokestatic io/putBool(Z)V
	getstatic MPClass.r F
	iconst_1
	i2f
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	getstatic MPClass.b Z
	iand
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 7
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
