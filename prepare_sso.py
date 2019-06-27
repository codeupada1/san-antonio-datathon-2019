#!/usr/bin/env python

"""
This script contains code used by the following jupytr notebooks:

1. master-sso.ipynb
2.
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
    return df.rename(index=str, columns={'inspkey':'inspection_key',
                                         'servno':'service_number',
                                         'reportdate':'report_date',
                                         'spill_st_name':'spill_street_name',
                                         'total_gal':'total_gallons',
                                         'galsret':'gallons_returned',
                                         'gal':'gallons_1',
                                         'spill_start':'spill_start_1',
                                         'spill_stop':'spill_stop_1',
                                         'hrs':'hours_1',
                                         'unitid':'unit_id_1',
                                         'unitid2':'unit_id_2',
                                         'earz_zone':'edwards_zone',
                                         'expr1029':'expr_1029',
                                         'pipediam':'pipe_diameter',
                                         'pipelen':'pipe_length',
                                         'pipetype':'pipe_type',
                                         'instyear':'installation_year',
                                         'dwndpth':'downstream_depth',
                                         'upsdpth':'upstream_depth',
                                         'rainfall_less3':'rainfall_less_3',
                                         'spill address': 'spill_address_full',
                                         'sewerassetexp':'sewer_asset_exp',
                                         'prevspill_24mos':'previous_spill_24mos',
                                         'unittype':'unit_type',
                                         'assettype':'asset_type',
                                         'lastclnd':'last_cleaned',
                                         'responsetime':'response_time',
                                         'responsedttm':'response_datetime',
                                         'public notice':'public_notice',
                                         'timeint':'time_int',
                                         'hrs_2':'hours_2',
                                         'gal_2':'gallons_2',
                                         'hrs_3':'hours_3',
                                         'gal_3':'gallons_3'
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
    df = remove_columns(df, columns=[ 'sso_id',
                                      'inspection_key',
                                      'service_number',
                                      'comments',
                                      'ferguson',
                                      'expr_1029',
                                      'downstream_depth',
                                      'upstream_depth',
                                      'sewer_asset_exp',
                                      'previous_spill_24mos',
                                    ])
    df['spill_street_address'] = df['spill_address'].map(str)+ ' ' + df['spill_street_name']
    df = df.drop(columns=['spill_address', 'spill_street_name'])
    df['multiple_spills'] = np.where(df['spill_start_2'].isnull(), False, True)
    df = df.drop(columns=['spill_start_2',
                          'spill_stop_2',
                          'hours_2',
                          'gallons_2',
                          'spill_start_3',
                          'spill_stop_3',
                          'hours_3',
                          'gallons_3',
                          'gallons_1',
                          'spill_address_full'
                          ])
    df = df.rename(index=str, columns={ "spill_start_1": "spill_start",
                                        "spill_stop_1": "spill_stop",
                                        "hours_1": "hours"})
    df = lowercase_column_values( df, 'unit_type',
                                'asset_type',
                                'cause',
                                'actions',
                                'watershed',
                                'discharge_to',
                                'discharge_route',
                                'pipe_type',
                                'root_cause',
                                )
    df = titlecase_column_values(df, 'spill_street_address')
    df[['council_district',
        'edwards_zone',
        'num_spills_24mos',
        'time_int'
        ]] = df[['council_district',
                                   'edwards_zone',
                                   'num_spills_24mos',
                                   'time_int'
                                   ]].fillna(0.0).astype(int)
    df['installation_year'] = df['installation_year'].fillna(9999).astype(int)
    df[['gallons_returned',
        'hours',
        'pipe_diameter',
        'pipe_length',
        'inches_no',
        'rainfall_less_3',
        'response_time',
        ]] = df[['gallons_returned',
                 'hours',
                 'pipe_diameter',
                 'pipe_length',
                 'inches_no',
                 'rainfall_less_3',
                 'response_time'
                 ]].fillna(0.0)
    df[['actions',
        'unit_id_1',
        'unit_id_2',
        'discharge_to',
        'discharge_route',
        'pipe_type',
        'spill_street_address',
        'unit_type',
        'asset_type',
        'root_cause',
        'steps_to_prevent',
      ]] = df[[ 'actions',
                'unit_id_1',
                'unit_id_2',
                'discharge_to',
                'discharge_route',
                'pipe_type',
                'spill_street_address',
                'unit_type',
                'asset_type',
                'root_cause',
                'steps_to_prevent',
                ]].fillna('na')
    df['report_date'] = pd.to_datetime(df['report_date'])
    df['response_datetime'] = pd.to_datetime(df['response_datetime'])
    df['last_cleaned'] = pd.to_datetime(df['last_cleaned'])

    df.to_csv('data/cleaned_sso_df.csv', index=False)

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

