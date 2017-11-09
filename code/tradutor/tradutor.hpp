#include <map>
#include <vector>
#include "quadruplas.hpp"
#include "tabela_simb_floresta.hpp"

class Tradutor {
	private:
		Tabela tabela;
		string instrucao;
		vector<string> instrucoesTAM;
		map<string, string (*)(Quadrupla &q, Tabela &t)> opcodes;
	public:
		Tradutor();
		string getInstrucao();
		void setInstrucao( string s );
		void traduzQuadruplas( Quadrupla Q );
		string traduzQuadrupla( Quadrupla q );
		void adicionaInstrucao( string inst );
		void imprimeProgramaTAM( string file_name );
};


