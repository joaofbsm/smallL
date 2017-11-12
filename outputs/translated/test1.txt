.version 52 0 
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
L4: 		ldc2_w 2.0
		dstore 5
L5: 		ldc2_w 6.0
		dstore 7
L6: 		ldc2_w 0.0
		ldc2_w 8.0
		dmul
		dstore 9
		sipush 1000
		newarray double
		astore 11
		dload 9
		ldc2_w 8.0
		ddiv
		dstore 9
		aload 11
		dload 9
		d2i
		ldc2_w 1.0
		dastore
L7: 		ldc2_w 1.0
		ldc2_w 8.0
		dmul
		dstore 13
		dload 13
		ldc2_w 8.0
		ddiv
		dstore 13
		aload 11
		dload 13
		d2i
		ldc2_w 2.0
		dastore
L8: 		ldc2_w 2.0
		ldc2_w 8.0
		dmul
		dstore 15
		dload 15
		ldc2_w 8.0
		ddiv
		dstore 15
		aload 11
		dload 15
		d2i
		ldc2_w 3.0
		dastore
L9: 		dload 1
		ldc2_w 1.0
		dadd
		dstore 1
L12: 		dload 1
		ldc2_w 8.0
		dmul
		dstore 17
		dload 17
		ldc2_w 8.0
		ddiv
		dstore 17
		aload 11
		dload 17
		d2i
		daload
		dstore 19
		dload 19
		dload 5
		dcmpg
		iflt L9
L11: 		dload 3
		ldc2_w 1.0
		dsub
		dstore 3
L14: 		dload 3
		ldc2_w 8.0
		dmul
		dstore 21
		dload 21
		ldc2_w 8.0
		ddiv
		dstore 21
		aload 11
		dload 21
		d2i
		daload
		dstore 23
		dload 23
		dload 5
		dcmpl
		ifgt L11
L13: 		dload 1
		dload 3
		dcmpl
		iflt L15
L16: 		goto L2
L15: 		dload 1
		ldc2_w 8.0
		dmul
		dstore 25
		dload 25
		ldc2_w 8.0
		ddiv
		dstore 25
		aload 11
		dload 25
		d2i
		daload
		dstore 7
L17: 		dload 1
		ldc2_w 8.0
		dmul
		dstore 27
		dload 3
		ldc2_w 8.0
		dmul
		dstore 29
		dload 29
		ldc2_w 8.0
		ddiv
		dstore 29
		aload 11
		dload 29
		d2i
		daload
		dstore 31
		dload 27
		ldc2_w 8.0
		ddiv
		dstore 27
		aload 11
		dload 27
		d2i
		dload 31
		dastore
L18: 		dload 3
		ldc2_w 8.0
		dmul
		dstore 33
		dload 33
		ldc2_w 8.0
		ddiv
		dstore 33
		aload 11
		dload 33
		d2i
		dload 7
		dastore
		goto L9
L2: 		return
	.end code 
.end method 
.sourcefile 'Main.java' 
.end class
