#!/usr/bin/python3
import numpy as np
import pandas as pd
from sklearn import svm

def pred(country, houseType, factor):
    fileName = country + houseType
    df = pd.read_excel("/var/www/html/houseData/" + fileName + ".xlsx")
    data = df.drop(['地段位置或門牌', '總價(萬元)', '型態'], axis=1)
    n = len(data)*4//5
    
    trainX = data[:n].values
    trainY = df['總價(萬元)'][:n].values

    if (fileName == 'tynHouse'):
        param = {'C': 9582, 'gamma': 0.0001680934761177432, 'epsilon': 0.017118174185304022}
    elif (fileName == 'tnnApart'):
        param = {'C': 7390, 'gamma': 0.00010650118681829898, 'epsilon': 0.21043214504765137}
    elif (fileName == 'tnnHouse'):
        param = {'C': 9180, 'gamma': 0.00010819941031417474, 'epsilon': 0.7791398478366648}
    else:
        param = {'C': 6374, 'gamma': 0.0016285719572013196, 'epsilon': 0.09808762344218226}

    regr = svm.SVR(**param)
    regr.fit(trainX, trainY)
    predY = regr.predict(factor)

    return predY
