import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def remove_features(df, features):
    for feature in features:
        df = df.drop(feature, axis=1)
    return df

def standardize_feature(df, feature, standard):
    df[feature] = df[feature].apply(lambda x: standard(x))
    return df

def count_vectorize(df, features, name='vector'):
    arr = []
    for i, r in df.iterrows():
        arr.append(' '.join([str(r[f]) for f in features]))
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(arr)

    for f in features:
        df = df.drop(f, axis=1)
    
    for i in range(len(cv_matrix.toarray()[0])):
        df.insert(len(df.columns), name + str(i), cv_matrix.toarray()[:,i], True)
    
    return df
    
