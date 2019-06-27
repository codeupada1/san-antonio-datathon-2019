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

    print(train.shape, test.shape)