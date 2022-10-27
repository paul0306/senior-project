#!/usr/bin/python3
import numpy as np
import pandas as pd
from xgboost import XGBRegressor

def pred(country, houseType, factor):
    fileName = country + houseType
    df = pd.read_excel("./houseData/" + fileName + ".xlsx")
    data = df.drop(['地段位置或門牌', '總價(萬元)', '型態'], axis=1)
    n = len(data)*4//5
    
    trainX = data[:n].values
    trainY = df['總價(萬元)'][:n].values

    if (fileName == 'tpeApart'):
        param = {'eta': 0.09878995029050915, 'min_child_weight': 1, 'max_depth': 9, 'gamma': 0.9186071192341262, 'subsample': 0.6221400736407773, 'colsample_bytree': 0.9881327614723773}
    elif (fileName == 'tpeHouse'):
        param = {'eta': 0.1379454043904626, 'min_child_weight': 10, 'max_depth': 3, 'gamma': 0.7393243825876435, 'subsample': 0.7139961932572817, 'colsample_bytree': 0.9920808431727819}
    elif (fileName == 'tynApart'):
        param = {'eta': 0.19183959966868047, 'min_child_weight': 3, 'max_depth': 4, 'gamma': 0.9402315352185174, 'subsample': 0.9995472921483681, 'colsample_bytree': 0.7104007674222794}
    elif (fileName == 'txgApart'):
        param = {'eta': 0.046399351096729095, 'min_child_weight': 2, 'max_depth': 9, 'gamma': 0.7799707114061424, 'subsample': 0.771152860221269, 'colsample_bytree': 0.8336224633799082}
    elif (fileName == 'txgHouse'):
        param = {'eta': 0.15345445163479923, 'min_child_weight': 1, 'max_depth': 3, 'gamma': 0.6994427366672115, 'subsample': 0.7048669936705431, 'colsample_bytree': 0.5563918515982558}
    else:
        param = {'eta': 0.09360304301568259, 'min_child_weight': 2, 'max_depth': 3, 'gamma': 0.13511543286134453, 'subsample': 0.704747049179695, 'colsample_bytree': 0.600925805441046}

    xgbrModel = XGBRegressor(**param)
    xgbrModel.fit(trainX,trainY)
    predY = xgbrModel.predict(factor)

    return predY