import os
import re

import pandas as pd
from bs4 import BeautifulSoup

from kneighbors import Kneighbors
from kneighborsC import KneighborsC


class Training(object):

    global knn
    knn = KneighborsC()

    def __init__(self):
        pass

    def run_training(self):
        #cria um arquivo de saida para o treinamento
        with open('/var/www/trvarfinder.com.br/public_html/py/trf/saida_treinamento.csv', "w") as output:
            files = os.listdir('/var/www/trvarfinder.com.br/public_html/py/trf/')

            #para cada arquivo de treinamento, inclui no arquivo final de treino
            for file in files:
                if re.match(".+\d\.csv", file):
                    with open('/var/www/trvarfinder.com.br/public_html/py/trf/' + file, "r") as saida_file:
                        #Escreve no arquivo o contedo:
                        output.writelines(saida_file)
                    os.remove("/var/www/trvarfinder.com.br/public_html/py/trf/" + file)

        #treina o algoritmo com o saida treinamento
        knn.do_train("/var/www/trvarfinder.com.br/public_html/py/saida_treinamento.csv")

    def run_test(self):
        #cria um arquivo de saida para o treinamento
        with open('/var/www/trvarfinder.com.br/public_html/py/saida_teste.csv', "w") as output:
            files = os.listdir('/var/www/trvarfinder.com.br/public_html/py/trf/')

            #para cada arquivo de teste, inclui no arquivo final de teste
            for file in files:
                if re.match("teste.\.csv", file):
                    with open('/var/www/trvarfinder.com.br/public_html/py/trf/' + file, "r") as saida_file:
                        # Escreve no arquivo o conteúdo:
                        output.writelines(saida_file)
                    os.remove("/var/www/trvarfinder.com.br/public_html/py/trf/" + file)


        #testa o algoritmo com o saida teste
        knn.do_test("/var/www/trvarfinder.com.br/public_html/py/trf/saida_teste.csv")

    def run_trf(self, fasta_url, training_mode, variable):
        # executa a chamada para o gerar os .html
        url = '/var/www/trvarfinder.com.br/public_html/py/trf/trf ' + fasta_url + ' 2 5 5 80 10 40 2000 -l 6'
        os.system(url)

        files = os.listdir('/var/www/trvarfinder.com.br/public_html/py/trf/')

        #deleta os .txt que no estão sendo utilizados
        for file in files:
            if re.match(".+\.txt\.html", file):
                os.remove("/var/www/trvarfinder.com.br/public_html/py/trf/" + file)
                files.remove(file)
            else:
                if re.match(".+summary.+\.html", file):
                    os.remove("/var/www/trvarfinder.com.br/public_html/py/trf/" + file)
                    files.remove(file)

        tr_table_files = []
        tr_table_out = []

        if training_mode == 1:
            #conta quantos arquivos .csv j existem no diretrio, para no sobrescrever
            num_csv = 0
            for file in files:
                if re.match(".+\.csv", file):
                    num_csv += 1

            #conta quantos arquivos de entrada .hmtl e sada .csv sero usados
            i = num_csv
            for file in files:
                if re.match(".+\.html", file):
                    tr_table_files.append(file)
                    tr_table_out.append("/var/www/trvarfinder.com.br/public_html/py/trf/treinamento" + str(i) + ".csv")
                    i += 1
        else:
            # pode substituir
            i = 0

            for file in files:
                if re.match(".+\.html", file):
                    tr_table_files.append(file)
                    tr_table_out.append("/var/www/trvarfinder.com.br/public_html/py/trf/teste" + str(i) + ".csv")
                    i += 1


        # tr_table_files tem todos os arquivos corretos terminados em .html
        # para cada .html gera um .csv
        i = 0
        for file in tr_table_files:
            self.__create_csv_file('/var/www/trvarfinder.com.br/public_html/py/trf/' + file, tr_table_out[i], i, variable)
            i += 1

        #se no for treinamento, ao rodar o TRF j realiza a classificao/regresso
        if training_mode == 0:
            self.run_test()

        return 1

    def __create_csv_file(self, url, output_file, num_csv, variable):
        soup = ""

        with open(url) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        #remove o html gerado
        os.remove(url)

        repeats_table = soup.find('table')

        # gerando a lista em colunas repeat_id,purity,unit_size,unit_number,trf_score,score,var
        repeat_id = []
        start = []
        end = []
        period_size = []
        copy_number = []
        consensus_size = []
        purity = []
        percent_indels = []
        trf_score = []
        a = []
        c = []
        g = []
        t = []
        entropy = []
        var = []

        i = 0
        for row in repeats_table.findAll("tr"):  # para tudo que estiver em <tr>
            cells = row('td')  # encontra todos os TDs

            if len(cells) == 12 and cells[0].find(text=True) != "Indices":  # nmero de colunas
                repeat_id.append(i)
                i += 1

                split = cells[0].find(text=True).split("--")
                start.append(split[0])
                end.append(split[1])

                period_size.append(cells[1].find(text=True))
                copy_number.append(cells[2].find(text=True))
                consensus_size.append(cells[3].find(text=True))
                purity.append(cells[4].find(text=True))
                percent_indels.append(cells[5].find(text=True))
                trf_score.append(cells[6].find(text=True))
                a.append(cells[7].find(text=True))
                c.append(cells[8].find(text=True))
                t.append(cells[9].find(text=True))
                g.append(cells[10].find(text=True))
                entropy.append(cells[11].find(text=True))
                if variable == 1:
                    var.append(1)
                else:
                    var.append(0)

        df = pd.DataFrame()

        df['repeat_id'] = repeat_id
        df['start'] = start
        df['end'] = end
        df['period'] = period_size
        df['copy_number'] = copy_number
        df['consensus_size'] = consensus_size
        df['purity'] = purity
        df['indels'] = percent_indels
        df['trf_score'] = trf_score
        df['a'] = a
        df['c'] = c
        df['t'] = t
        df['g'] = g
        df['entropy'] = entropy
        df['var'] = var

        if num_csv == 0 and variable == 1:
            df.to_csv(output_file, index=False)
        else:
            df.to_csv(output_file, index=False, header=False)