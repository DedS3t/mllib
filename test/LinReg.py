from mllib.models.LinearRegression import LinearRegression
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from mllib.helpers import train_test_split
from sklearn.preprocessing import MinMaxScaler

TYPE = "1d" # 1d (single dimension) or nd (multi variate)
if TYPE == "1d":
    data = pd.read_csv('./data/singledimdata.csv')
    X = data.iloc[:,0]
    y = data.iloc[:,1]
    reg = LinearRegression()
    reg.fit(X, y)
    plt.scatter(X, y)
    y_hat = reg.betas * X
    plt.plot([min(X), max(X)], [min(y_hat), max(y_hat)], color="red")
    plt.show()
elif TYPE == "nd":
    data = pd.read_csv('./data/multidimdata.csv')
    # transformas values into numeric
    diagnosis_map = {'M':1,'B':-1}
    data['diagnosis'] = data['diagnosis'].map(diagnosis_map)
    data.drop(data.columns[[-1,0]],axis=1,inplace=True)

    # normalization: converting a range of values into a certain interval ([-1,1] or [0,1]). Improves speed of learning
    Y = data.loc[:,'diagnosis']
    X = data.iloc[:,1:] 
    X_normalized=MinMaxScaler().fit_transform(X.values)
    X = pd.DataFrame(X_normalized)
    # split data
    # X.insert(loc=len(X.columns),column='intercept',value=1) # add intercept column
    X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
    X_train = np.array(X_train)
    y_train = np.reshape(np.array(y_train), (len(y_train), 1))
    reg = LinearRegression()
    reg.fit(np.array(X_train), np.array(y_train), lr = 0.00001, epochs = 100000)



