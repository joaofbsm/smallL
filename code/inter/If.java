package code.inter;  // Arquivo If.java

import code.symbols.*;

public class If extends Stmt {
    Expr expr; Stmt stmt;

    public If(Expr x, Stmt s) {
        expr=x; stmt=s;
        if( expr.type != Type.Bool ) expr.error("boolean required in if");
    }
    
    public void gen(int b, int a) {
        int label = newlabel(); // r\’otulo do c\’odigo para stmt
        expr.jumping(0, a);     // segue se for true, vai para a se for false
        emitlabel(label); stmt.gen(label, a);
    }
}
