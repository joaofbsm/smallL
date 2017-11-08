void Tradutor::imprimeProgramaTAM( string file_name ){
    ofstream output( file_name.c_str(), ios::out );
	
	cout << "Impressao do Programa TAM" << endl;
	cout << "------------------------" << endl;
	for ( unsigned int i = 0; i < instrucoesTAM.size(); i++ ){
		cout << instrucoesTAM[i];
        output << instrucoesTAM[i];
		cout << "------------------------" << endl;
    	output.close();
}