.version 52 0 
.class public super Main 
.super java/lang/Object 

.method public <init> : ()V 
    .code stack 1 locals 1 
L0:     aload_0 
L1:     invokespecial Method java/lang/Object <init> ()V 
L4:     return 
L5:     
    .end code 
.end method 

.method public static main : ([Ljava/lang/String;)V 
    .code stack 4 locals 50 
L0:     ldc2_w +1.0 
L3:     dstore 1 
L5:     ldc2_w +10.0 
L8:     dstore 3 
L10:    dload 1 
L12:    dload 3 
L14:    dcmpg 
L15:    ifge L50 
L18:    ldc2_w +0.0 
L21:    ldc2_w +8.0 
L24:    dmul 
L25:    dstore 5 
L27:    sipush 1000 
L30:    newarray double 
L32:    astore 7 
L34:    dload 5 
L36:    ldc2_w +8.0 
L39:    ddiv 
L40:    dstore 5 
L42:    aload 7 
L44:    dload 5 
L46:    d2i 
L47:    dload 3 
L49:    dastore 
L50:    return 
L51:    
    .end code 
.end method 
.sourcefile 'Main.java' 
.end class 
