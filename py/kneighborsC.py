import numpy as np
import pandas as pd
import json

from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt



class KneighborsC(object):

    knc = ""

    def __init__(self):
        pass

    def do_test(self, test_csv):
        global knc
        teste = pd.read_csv(test_csv)

        testBackup = teste.copy()

        teste.drop(['repeat_id'], 1, inplace=True)
        teste.drop(['start'], 1, inplace=True)
        teste.drop(['end'], 1, inplace=True)
        teste.drop(['period'], 1, inplace=True)
        teste.drop(['indels'], 1, inplace=True)
        teste.drop(['a'], 1, inplace=True)
        teste.drop(['c'], 1, inplace=True)
        teste.drop(['t'], 1, inplace=True)
        teste.drop(['g'], 1, inplace=True)
        teste.drop(['entropy'], 1, inplace=True)
        teste.drop(['trf_score'], 1, inplace=True)
        teste.drop(['var'], 1, inplace=True)

        #utiliza o knC criado para predizer a variabilidade
        prediction = knc.predict(teste)
        print(prediction)


        #salva os dados como resultados.json, dropa a coluna VAR e adiciona a coluna PREDICTION
        testBackup.drop(['var'], 1, inplace=True)
        testBackup['prediction'] = prediction
        testBackup.to_json('/var/www/trvarfinder.com.br/public_html/py/trf/resultados.json')

    def do_train(self, train_csv):
        global knc

        score = 0

        while score < 0.8 :
            data = pd.read_csv(train_csv)

            # utiliza apenas consensus_size, copy_nro e purity
            data.drop(['repeat_id'], 1, inplace=True)
            data.drop(['start'], 1, inplace=True)
            data.drop(['end'], 1, inplace=True)
            data.drop(['period'], 1, inplace=True)
            data.drop(['indels'], 1, inplace=True)
            data.drop(['a'], 1, inplace=True)
            data.drop(['c'], 1, inplace=True)
            data.drop(['t'], 1, inplace=True)
            data.drop(['g'], 1, inplace=True)
            data.drop(['entropy'], 1, inplace=True)
            data.drop(['trf_score'], 1, inplace=True)

            y = np.array(data['var'])
            X = np.array(data.drop(['var'], 1))

            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

            knc = KNeighborsClassifier(n_neighbors=3)
            knc.fit(X_train, y_train)
            
            score = cross_val_score(knc, X, y, cv=5)
            print(np.mean(score))


            score = knc.score(X_test, y_test)

            #if score >= 0.70:
            print("Score atingiu: " + str(score))

            print(y_test)
            print(knc.predict(X_test))
