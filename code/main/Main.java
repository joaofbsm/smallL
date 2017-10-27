package Main;  // Arquivo Main.java

import java.io.*; 
import code.lexer.*; 
import code.parser.*;

public class Main { 
public static void Main(String[] args) throws IOException {
    Lexer lex = new Lexer();
    Parser parse = new Parser(lex);
    parse.program();
    System.out.write("\n");
    }
}
