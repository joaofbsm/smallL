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
		ldc2_w 8.0
		dmul
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
		ldc2_w 0.0
		dastore
L5: 		ldc2_w 2.0
		ldc2_w 8.0
		dmul
		dstore 9
		dload 9
		ldc2_w 8.0
		ddiv
		dstore 9
		aload 7
		dload 9
		d2i
		ldc2_w 1.5
		dastore
L6: 		ldc2_w 1.0
		ldc2_w 8.0
		dmul
		dstore 11
		dload 11
		ldc2_w 8.0
		ddiv
		dstore 11
		aload 7
		dload 11
		d2i
		daload
		dstore 13
		ldc2_w 2.0
		ldc2_w 8.0
		dmul
		dstore 15
		dload 15
		ldc2_w 8.0
		ddiv
		dstore 15
		aload 7
		dload 15
		d2i
		daload
		dstore 17
		dload 13
		dload 17
		dadd
		dstore 3
L2: 		return
	.end code 
.end method 
.sourcefile 'Main.java' 
.end class
