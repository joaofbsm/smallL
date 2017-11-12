.version 50 0 
.class public super Main 
.super java/lang/Object 

.method public <init> : ()V 
	.code stack 1 locals 1 
L0:		aload_0 
L1:		invokespecial Method java/lang/Object <init> ()V 
L4:		return 
L5:     
	.end code 
.end method 

.method public static main : ([Ljava/lang/String;)V
	.code stack 4 locals 50

L1: 		ldc2_w 1.0
		dstore 1
L3: 		ldc2_w 10.0
		dstore 3
L4: 		dload 1
		dload 3
		dcmpg
		ifge L2
L5: 		ldc2_w 0.0
		dstore 5
		sipush 1000
		newarray double
		astore 7
		dload 5
		ldc2_w 8.0
		ddiv
		dstore 5
		aload 7
		dload 5
		d2i
		dload 3
		dastore
L2: 		return
		return
	.end code 
.end method 
.sourcefile 'Main.java' 
.end class
