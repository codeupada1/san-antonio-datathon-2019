#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

1. master-sso.ipynb
2. dd-aqi.ipynb
3.

"""



# ===========
# ENVIRONMENT
# ===========


import os
import sys

import pandas as pd
import numpy as np



# ===========
# PREPARATION
# ===========


def missing_values_col(df):
    """
    This functions returns the total missing values and
    the percent missing values by column.
    """
    null_count = df.isnull().sum()
    null_percentage = (null_count / df.shape[0]) * 100
    empty_count = pd.Series(((df == ' ') | (df == '')).sum())
    empty_percentage = (empty_count / df.shape[0]) * 100
    nan_count = pd.Series(((df == 'nan') | (df == 'NaN')).sum())
    nan_percentage = (nan_count / df.shape[0]) * 100
    return pd.DataFrame({'num_missing': null_count, 'missing_percentage': null_percentage,
                         'num_empty': empty_count, 'empty_percentage': empty_percentage,
                         'nan_count': nan_count, 'nan_percentage': nan_percentage})


def missing_values_row(df):
    """
    This functions returns the total missing values and
    the percent missing values by row.
    """
    null_count = df.isnull().sum(axis=1)
    null_percentage = (null_count / df.shape[1]) * 100
    return pd.DataFrame({'num_missing': null_count, 'percentage': null_percentage})


def handle_missing_threshold(df, prop_required_column = .3, prop_required_row = .9):
    """
    This functions removes columns and rows whose
    count of missing values exceeds threshold.
    """
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df


def count_values(df):
    """
    This function counts the value of columns in a dataframe.
    """
    for col in df.columns:
        n = df[col].unique().shape[0]
        col_bins = min(n, 10)
        print(f"{col}:")
        if df[col].dtype in ['int64', 'float64'] and n > 10:
            print(df[col].value_counts(bins=col_bins, sort=False))
        else:
            print(df[col].value_counts())
        print("\n")

def remove_columns(df, columns):
    return df.drop(columns=columns)


def fill_with_zeroes(df, *cols):
    """
    This functions returns the column names as input and
    return the dataframe with the
    null values in those columns replace by 0.
    """
    for col in cols:
        df[col] = df[col].fillna(0)
    return df


def fill_with_median(df, *cols):
    """
    This function fills the NaN values with
    respective median values.
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].median())
    return df


def fill_with_none(df, *cols):
    """
    This function fills the NaN values with
    'None' string value.
    """
    for col in cols:
        df[col] = df[col].fillna('None')
    return df

def fill_with_unknown(df, *cols):
    """
    This functions fills the NaN values with
    'Unknown' string value.
    """
    for col in cols:
        df[col] = df[col].fillna('Unknown')
    return df

def lowercase_columns(df):
    """
    This function returns a lowercase version of the column values.
    """
    df.columns = map(str.lower, df.columns)
    return df

def lowercase_column_values(df, *columns):
    """
    This function returns a lowercase version of the column values.
    """
    for col in columns:
        df[col] = df[col].str.lower() 
    return df

def titlecase_column_values(df, *columns):
    """
    This function returns a titlecase version of the values.
    """
    for col in columns:
        df[col] = df[col].str.title() 
    return df


def rename_columns_all(df):
    """
    takes in selected dataframe and renames columns to intuitive non-capitalized titles
    """
    return df.rename(index=str, columns={'airmonitor name':'monitor_name',
                                         'airmonitor active':'active',
                                         'airmonitor address zip':'zip',
                                         'airmonitor address state':'state',
                                         'airmonitor address city':'city',
                                         'airmonitor address street':'street',
                                         'airmonitorreading timestamp':'timestamp',
                                         'airmonitorreading temperature':'temperature',
                                         'airmonitorreading humidity':'humidity',
                                         'airmonitorreading no2':'nitrogen_dioxide',
                                         'airmonitorreading no2 aqi':'nitrogen_dioxide_aqi',
                                         'airmonitorreading so2':'sulfur_dioxide',
                                         'airmonitorreading so2 aqi':'sulfur_dioxide_aqi',
                                         'airmonitorreading o3':'trioxygen',
                                         'airmonitorreading o3 aqi':'trioxygen_aqi',
                                         'airmonitorreading co':'carbon_monoxide',
                                         'airmonitorreading co aqi':'carbon_monoxide_aqi',
                                         'airmonitorreading voc':'volatile',
                                         'airmonitorreading voc aqi':'volatile_aqi',
                                         'airmonitorreading pm2point5':'particulate5',
                                         'airmonitorreading pm2point5 aqi':'particulate5_aqi',
                                         'airmonitorreading pm10': 'particulate10',
                                         'airmonitorreading pm10 aqi':'particulate10_aqi',
                                         'airmonitorreading airmonitorreading finalaqi':'final_aqi',
                                          })
def lowercase_and_rename(df):
    """
    This function changes the column names' case to lowercase
    and renames the column.
    """
    return rename_columns_all(lowercase_columns(df))

def ready_df1(df):
    """
    This function prepares the dataframe for EDA.
    """
    df = remove_columns(df, columns=[ 'nitrogen_dioxide',
                                      'nitrogen_dioxide_aqi',
                                      'sulfur_dioxide',
                                      'sulfur_dioxide_aqi',
                                      'trioxygen',
                                      'trioxygen_aqi',
                                      'volatile',
                                      'volatile_aqi',
                                    ])
    df['fahrenheit'] = 9.0/5.0 * df['temperature'] + 32
    df = df.drop(columns=['temperature'])
    df = df.rename(index=str, columns={'fahrenheit':'temperature'})
    df['carbon_monoxide'] = df['carbon_monoxide'].fillna(0).astype(int)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df



# ==================================================
# MAIN
# ==================================================


def clear():
      os.system("cls" if os.name == "nt" else "clear")

def main():
    """Main entry point for the script."""
    pass


if __name__ == '__main__':
    sys.exit(main())










__authors__ = ["Joseph Burton", "Ednalyn C. De Dios", "Sandy Graham"]
__copyright__ = "Copyright 2019, Codeup Data Science"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainers__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"

