// Inclusao dupla
// x.h inclui a.h
// y.h inclui a.h
// z.h inclui x.y e y.h
// Se nao tiver esse ifndef, inclui
// textualmente o a.h duas vezes e define
// tudo duas vezes.
// Esse e o famoso Header Guard.
// Era isso que estava acontecendo.
#ifndef QUADRUPLAS_HPP
#define QUADRUPLAS_HPP

constexpr int NUM_OPERANDOS = 3;

class Quadrupla
{
    private:
        string op;
        string ops[NUM_OPERANDOS];
        
    public:
        Quadrupla();
        string get_operador( void );
        void set_operador( string novo );
        string get_operado_pos( int pos );
        void set_ops( int pos, string v );
        Quadrupla stringToQuadrupla( string s );
        void imprimeQuadruplas();
                                            /* operador */
                                            /* operandos 0, 1 e 2 */
                                            /* construtor */
        Quadrupla( string op, string a, string b, string c); /* construtor */
    
};

#endif // !QUADRUPLAS_HPP