Quadruplas::Quadruplas(){
    quadruplas.resize(0);
}

Quadrupla Quadruplas::getQuadrupla( int pos ){
    return quadruplas[pos];
}

void Quadruplas::addQuadrupla( Quadrupla q ){
    quadruplas.push_back(q);
}

int Quadruplas::getNumQuadruplas(){
    return quadruplas.size();
}

      /* retorna operador */
      /* muda operador para novo */
        /* retorna operando pos */
/* muda valor do operando pos para v */
/* retorna a quadrupla representada por s */

void Quadruplas::imprimeQuadruplas(){
    
    Quadrupla q;
    
    cout << "Impressao das quadruplas" << endl;
    cout << "---------------------" << endl;
    
    for ( unsigned int i = 0; i < quadruplas.size(); i++ ){
        q = quadruplas[i];
        q.imprimeQuadrupla();
    }
    
    cout << "---------------------" << endl << endl;
}