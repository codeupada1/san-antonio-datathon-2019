import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

from scipy.stats import pearsonr

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, median_absolute_error

def create_pipe_data(num_days):

    '''
    Let's create data that replicates the history of flow of water through a pipe.
    '''

    pipe = pd.DataFrame(np.random.randint(19,101,size=(num_days, 1)), columns=['percent_flow'])
    pipe = pipe.sort_values(by=['percent_flow'], ascending=False)
    pipe.reset_index(drop=True, inplace=True)

    pipe_days = pd.Series(range(1,(num_days + 1)))
    pipe_days = pd.DataFrame(pipe_days, columns=['days'])

    pipe_df = pipe.merge(pipe_days, left_index=True, right_index=True)

    return pipe_df

def poly_regression(pipe_name, train_size):

    train = pipe_name[:int(pipe_name.shape[0] * train_size)]
    test = pipe_name[int(pipe_name.shape[0] * train_size):]

    X_train = train[['percent_flow']]
    y_train = train[['days']]

    X_test = test[['percent_flow']]
    y_test = test[['days']]

    print(X_train.shape)
    print('---')
    print(X_test.shape)
    print('---')
    print(y_train.shape)
    print('---')
    print(len(y_test))  

    poly_features = PolynomialFeatures(degree=2)

    ### transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train)

    ### fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train)
        
    ### predicting on training data-set
    y_train_predicted = poly_model.predict(X_train_poly)

    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_predicted))
    r2_train = r2_score(y_train, y_train_predicted)

    print("The model performance for the training set")
    print("-------------------------------------------")
    print("RMSE of training set is {}".format(rmse_train))
    print("R2 score of training set is {}".format(r2_train))

    y_test_predicted = poly_model.predict(poly_features.fit_transform(X_test))
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_predicted))
    r2_test = r2_score(y_test, y_test_predicted)
    print("The model performance for the test set")
    print("-------------------------------------------")
    print("RMSE of test set is {}".format(rmse_test))
    print("R2 score of test set is {}".format(r2_test))

    # print(train.shape, test.shape)