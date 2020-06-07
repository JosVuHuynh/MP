.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	ldc 10000.01
	fstore_2
	fload_2
	fstore_1
	fload_1
	iconst_0
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "ptvn"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label5
Label4:
	fload_2
	fneg
	fload_1
	fdiv
	invokestatic io/putFloat(F)V
Label5:
	iconst_0
	i2f
	fstore_2
	fload_2
	fstore_1
	fload_1
	iconst_0
	i2f
	fcmpl
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "ptvn"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label9
Label8:
	fload_2
	fneg
	fload_1
	fdiv
	invokestatic io/putFloat(F)V
Label9:
Label1:
	return
.limit stack 6
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
