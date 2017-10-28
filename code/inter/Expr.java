package code.inter;  // Arquivo Expr.java

import code.lexer.*; 
import code.symbols.*;

public class Expr extends Node {
    public Token op;
    public Type type;

    Expr(Token tok, Type p) { op = tok;type=p;}

    public Expr gen() { return this; }

    public Expr reduce() { return this; }

    public void jumping(int t, int f) { emitjumps(toString(), t, f); }

    public void emitjumps(String test, int t, int f) {
        if(t!=0&&f!=0){
            emit("if " + test + " goto L" + t);
            emit("goto L" + f);
        }
        else if(t!=0)emit("if"+test+"gotoL"+t);
        else if(f!=0)emit("iffalse"+test+"gotoL"+f);
        else ; // nada, porque ambos t e f fall through
    }

    public String toString() { return op.toString(); }
 }
