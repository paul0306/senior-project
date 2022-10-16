# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

def mape(actual, pred):
    return np.mean(np.abs((actual - pred) / actual)) * 100

def rmse(actual, pred):
    return np.sqrt(np.square(np.subtract(actual, pred)).mean())

def main():
    df = pd.read_excel("高雄透天.xlsx")
    data = df.drop(['地段位置或門牌', '總價(萬元)', '型態'], axis=1)
    n = len(data)*4//5
    
    trainX = data[:n].values
    trainY = df['總價(萬元)'][:n].values
    testX = data[n:]
    
    # eta=0.01~0.2, min_child_weight, max_depth=3~10, gamma, subsample=0.5~1, colsample_bytree=0.5~1
    #     0.3              1                6            0         1                1
    # best=  0.03          5                6            0        0.5               1
    param = {'eta': 0.09360304301568259, 'min_child_weight': 2, 'max_depth': 3, 'gamma': 0.13511543286134453, 'subsample': 0.704747049179695, 'colsample_bytree': 0.600925805441046}
    xgbrModel = XGBRegressor(**param)
    xgbrModel.fit(trainX,trainY)
    predY = xgbrModel.predict(testX)
    actualY = df['總價(萬元)'][n:].values
    
    print(mape(actualY, predY))
    print(rmse(actualY, predY))
    
    # plt.rcParams['font.sans-serif'] = ['mingliu']
    # plt.rcParams['axes.unicode_minus'] = False
    # plt.plot(actualY, label="actual")
    # plt.plot(predY, label="pred")
    # plt.title("XGBoost模型(宜蘭透天)")
    # plt.xlabel("資料數")
    # plt.ylabel("總價")
    # plt.legend()
    # plt.show()
    
    # df = pd.DataFrame(coef)
    # df.to_excel("桃園透天相關係數(XGBoost).xlsx")
    
if __name__ == '__main__':
    main()