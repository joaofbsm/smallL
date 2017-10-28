package code.inter;  // Arquivo Stmt.java

public class Stmt extends Node {
    public Stmt() { }

    public static Stmt Null = new Stmt();

    public void gen(int b, int a) {}  // chamado com r\’otulos begin e after

    int after = 0;  // guarda r\’otulo after

    public static Stmt Enclosing = Stmt.Null;  // usado para comandos break
}
