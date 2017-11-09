#include <cstring>
#include <cstdio>
#include <iostream>

using namespace std;

#include "quadruplas.hpp"
#include "tradutor.hpp"
#include "tabela_simb_floresta.hpp"


void leArqEntrada( string file_name, Quadrupla &Q ){
    
    string s;
    Quadrupla q;
    ifstream input( file_name.c_str(), ios::in );
    
    if ( !input ) {
        cout << "O arquivo " << file_name << " nao existe. O programa terminara agora!" << endl;
        exit(0); 
    
    } else {
        while ( getline( input, s ) ) {
            q = q.stringToQuadrupla( s );
            Q.addQuadrupla( q );
        }
    }

    input.close();
}

int main( int argc, char *argv[] ){
    string file_name_in;
    string file_name_out;
    Tradutor T;
    Quadrupla Q;
    
    if( argc < 3 ) {
        cout << "Escreva o nome do arquivo de entrada: " << endl;
        cin >> file_name_in;
        cout << "Escreva o nome do arquivo de saida: " << endl;
        cin >> file_name_out;
    
    } else {
        file_name_in = argv[1];
        file_name_out = argv[2];
    }
    
    leArqEntrada( file_name_in, Q );
    
    cout << endl;
    Q.imprimeQuadruplas();
    T.traduzQuadruplas( Q );
    T.imprimeProgramaTAM( file_name_out );
    cout << endl;
    
    return 0; 
}