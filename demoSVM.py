import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt

def mape(actual, pred):
    return np.mean(np.abs((actual - pred) / actual)) * 100

def rmse(actual, pred):
    return np.sqrt(np.square(np.subtract(actual, pred)).mean())

def main():
    df = pd.read_excel("桃園大樓.xlsx")
    data = df.drop(['地段位置或門牌', '總價(萬元)', '型態'], axis=1)
    n = len(data)*4//5
    
    trainX = data[:n].values.tolist() 
    trainY = df['總價(萬元)'][:n].values.tolist()
    testX = data[n:]
    
    param = {'C': 9786, 'gamma': 0.00013420323222871787, 'epsilon': 0.24590924795429966}
    regr = svm.SVR(**param)
    regr.fit(trainX, trainY)
    predY = regr.predict(testX)
    actualY = df['總價(萬元)'][n:].values.tolist()
    
    print(mape(actualY, predY))
    print(rmse(actualY, predY))
    
if __name__ == '__main__':
    main()
