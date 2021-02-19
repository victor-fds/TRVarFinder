import os
import re
import sys

import training


def create_fasta_file(tr):
    with open('/var/www/trvarfinder.com.br/public_html/py/trf/teste.fasta', "w") as output:
        output.writelines(">Teste rápido\n")
        output.writelines(tr)
    output.close()

def clean_csv_from_path():
    files = os.listdir('/var/www/trvarfinder.com.br/public_html/py/trf/')

    # inicia o programa
    for file in files:
        if re.match(".+\.csv", file):
            os.remove("/var/www/trvarfinder.com.br/public_html/py/trf/" + file)


clean_csv_from_path()

print("teste " + sys.argv[1])

tr_class = training.Training()

#treina o algoritmo usando a base atual
fasta_input = "/var/www/trvarfinder.com.br/public_html/py/trf/instaveis.fasta"
tr_class.run_trf(fasta_input, 1, 1)
fasta_input = "/var/www/trvarfinder.com.br/public_html/py/trf/conservados.fasta"
tr_class.run_trf(fasta_input, 1, 0)

tr_class.run_training()
 
#realiza um teste com o teste.fasta
#param = sys.argv[1]
tr_class.run_trf("/var/www/trvarfinder.com.br/public_html/py/trf/testar.fasta", 0, 1)
