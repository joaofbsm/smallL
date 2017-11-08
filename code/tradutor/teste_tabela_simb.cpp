tabela.hpp
tabela.cpp
main.cpp 

void teste1( Tabela t )
{
    cout << endl << "----- Impressao do Teste 1 ----- " << endl;
    t.entrada_bloco();
    t.instala("a", "integer");
    t.instala("b", "integer");
    t.instala("c", "integer");
    t.imprime();
    t.saida_bloco();
}

void teste2( Tabela t )
{
    cout << endl << "----- Impressao do  Teste 2 ----- " << endl;
    t.entrada_bloco();
    t.instala("i", "INTEGER");
    t.imprime();
    t.saida_bloco();
}

void teste3( Tabela t )
{
    cout << endl << "----- Impressao do Teste 3 ----- " << endl;
    t.entrada_bloco();
    t.instala("a", "integer");
    t.imprime();
    t.saida_bloco();
}

void teste4( Tabela t )
{
    cout << endl << "----- Impressao do Teste 4 ----- " << endl;

}

void teste5( Tabela t )
{
    cout << endl << "----- Impressao do Teste 5 ----- " << endl;
}

int main(int argc, char **argv){
    Tabela t;
    teste1(t); t.limpa();
    teste2(t); t.limpa();
    teste3(t); t.limpa();
    teste4(t); t.limpa();
    teste5(t); t.limpa();
    return 0; 
}