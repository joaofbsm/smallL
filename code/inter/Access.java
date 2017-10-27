package inter;  // Arquivo Access.java

import lexer.*; 
import symbols.*;

public class Access extends Op {
    public Id array;
    public Expr index;

    public Access(Id a, Expr i, Type p) {  // p \’e o tipo de elemento ap\’os
        super(new Word("[]", Tag.INDEX), p);  // achatar o arranjo
        array = a; index = i;
    }
    
    public Expr gen() { return new Access(array, index.reduce(), type); }
    
    public void jumping(int t,int f) { emitjumps(reduce().toString(),t,f); }
    
    public String toString() {
        return array.toString() + " [ " + index.toString() + " ]";
    }
}