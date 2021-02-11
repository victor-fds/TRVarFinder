import os
import re
import sys

import training


def create_fasta_file(tr):
    with open('C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/teste.fasta', "w") as output:
        output.writelines(">Teste rápido\n")
        output.writelines(tr)
    output.close()

def clean_csv_from_path():
    files = os.listdir('C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/')

    # inicia o programa
    for file in files:
        if re.match(".\.csv", file):
            os.remove("C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/" + file)


tr_class = training.Training()
clean_csv_from_path()

#treina o algoritmo usando a base atual
fasta_input = "C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/instaveis.fasta"
tr_class.run_trf(fasta_input, 1, 1)
fasta_input = "C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/conservados.fasta"
tr_class.run_trf(fasta_input, 1, 0)

tr_class.run_training()
 
#realiza um teste com o teste.fasta
tr_class.run_trf("C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/testar.fasta", 0, 1)
