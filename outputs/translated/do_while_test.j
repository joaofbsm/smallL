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
	.code stack 4 locals 100

L1: 		ldc2_w 1.0
		dstore 1
L3: 		ldc2_w 10.0
		dstore 3
L4: 		dload 1
		ldc2_w 1.0
		dadd
		dstore 1
L5: 		dload 1
		dload 3
		dcmpg
		iflt L4
L2: 		return
	.end code 
.end method 
.sourcefile 'Main.java' 
.end class
