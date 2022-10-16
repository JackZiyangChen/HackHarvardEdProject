import pandas as pd
import numpy as np


def get_index_by_attribute(df, attribute, value):
    return df[df[attribute] == value].index[0]

def dataframe_to_dict(df):
    res = {}
    for i, r in df.iterrows():
        res[i] = serialize_row(r, df.columns)
    return res

def serialize_row(row, column_names):
    data = {}
    for col in column_names:
        data[col] = row[col]

    return data

def get_dataframe_from_dictlist(dlist):
    df = pd.DataFrame(dlist)
    return df