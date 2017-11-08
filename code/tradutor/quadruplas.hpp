class Quadrupla
{
    private:
        string op;
        string ops[NUM_OPERANDOS];
        string get-operador( void );
        void set-operador( string novo );
        string get-operado-pos( int pos );
        void set-ops( int pos, string v );
        Quadrupla stringToQuadrupla( string s );
        void imprimeQuadrupla();
                                            /* operador */
                                            /* operandos 0, 1 e 2 */
                                            /* construtor */
        Quadrupla( string op, string a, string b, string c); /* construtor */
    
    public:
        Quadrupla();
};