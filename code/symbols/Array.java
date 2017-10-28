package code.symbols;  // Arquivo Array.java

import code.lexer.*;

public class Array extends Type {
    public Type of;  // arranjo *of* type
    public int size = 1;  // n\’umero de elementos

    public Array(int sz, Type p) {
        super("[]", Tag.INDEX, sz*p.width); size = sz;  of = p;
    }

    public String toString() { return "[" + size + "] " + of.toString(); }
}
