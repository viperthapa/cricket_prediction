from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report



# def pred_func(a,b,c,d):
#     X = np.loadtxt('scores/ten_over.txt',usecols=[4,0,1,2])
#     y = np.loadtxt('scores/ten_over.txt',usecols=[3])
#
#     logisticRegr = LogisticRegression()
#     x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#
#     logisticRegr.fit(x_train,y_train)
#
#     inputs = np.array([[a,b,c,d]])
#     res = logisticRegr.predict(inputs)
#
#     return res

def pred_func(n,a,b,c,d):
    raw_x = pd.read_csv('scores/two_innings.csv',usecols = [43,2*n+1,2*n+2])
    raw_y = pd.read_csv('scores/two_innings.csv',usecols = [44])

    X = raw_x.to_numpy()
    y = raw_y.to_numpy()

    dataset = np.array(np.ones((len(X),1)))
    dataset = np.hstack((dataset,X))

    logisticRegr = LogisticRegression()
    x_train, x_test, y_train, y_test = train_test_split(dataset, y, test_size=0.25, random_state=0)

    logisticRegr.fit(x_train,y_train)

    inputs = np.array([[a,b,c,d]])
    res = logisticRegr.predict(inputs)

    return res


def pred_target(n,a,b,c):
    one_x = pd.read_csv('scores/one_innings.csv',usecols=[2*n+1,2*n+2])
    one_y = pd.read_csv('scores/two_innings.csv',usecols=[43])

    ar_x = one_x.to_numpy()
    ar_y = one_y.to_numpy()

    one_data = np.array(np.ones((len(ar_x),1)))
    one_data = np.hstack((one_data,ar_x))

    linearRegr = LinearRegression()
    x_train, x_test, y_train, y_test = train_test_split(one_data, ar_y, test_size=0.25, random_state=0)

    linearRegr.fit(x_train,y_train)

    inputs = np.array([[a,b,c]])
    res = linearRegr.predict(inputs)

    return int(res)
