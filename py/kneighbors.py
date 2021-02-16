import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

class Kneighbors(object):

    knr = ""

    def __init__(self):
        pass

    def do_test(self, test_csv):
        global knr
        example = pd.read_csv('/var/www/trvarfinder.com.br/public_html/py/trf/saida_teste.csv')
        example.drop(['repeat_id'], 1, inplace=True)
        example.drop(['start'], 1, inplace=True)
        example.drop(['end'], 1, inplace=True)
        example.drop(['period'], 1, inplace=True)
        example.drop(['indels'], 1, inplace=True)
        example.drop(['a'], 1, inplace=True)
        example.drop(['c'], 1, inplace=True)
        example.drop(['t'], 1, inplace=True)
        example.drop(['g'], 1, inplace=True)

        teste = example.drop(['var'], 1)

        print("Resultados")
        prediction = knr.predict(teste)
        print("Score provável: " + str(knr.score(teste, example['var'])))
        print(prediction)
        print(example['var'])
        print("-----")

    def do_train(self, train_csv):
        global knr

        score = 0

        while score < 0.70 :
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

            knr = KNeighborsRegressor(n_neighbors=1, algorithm='auto')
            knr.fit(X_train, y_train)

            score = knr.score(X_test, y_test)

            #if score >= 0.70:
            print("Score atingiu: " + str(score))

            print(y_test)
            print(knr.predict(X_test))
