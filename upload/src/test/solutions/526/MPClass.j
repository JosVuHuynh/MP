.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static r F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass.a I
	iconst_1
	i2f
	putstatic MPClass.r F
	getstatic MPClass.a I
	invokestatic io/putInt(I)V
	getstatic MPClass.r F
	getstatic MPClass.a I
	i2f
	fadd
	invokestatic io/putFloat(F)V
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
