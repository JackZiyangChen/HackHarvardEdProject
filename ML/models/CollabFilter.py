from xml.dom.expatbuilder import parseString
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

from ML.models.cleaning import count_vectorize
import json



class CollabFilter:

    def __init__(self):
        self.df = pd.DataFrame()
        self.df_clean = pd.DataFrame()
        self.result = pd.DataFrame()
        self.cosine_matrix = np.array([])

    def populate_df(self, arr):
        self.df = pd.DataFrame(arr)
        return self

    def clean_data(self):
        # note: DO NOT sort df
        return self

    def run(self):
        print(self.df_clean)
        matrix = self.df_clean.to_numpy()
        self.cosine_matrix = cosine_similarity(matrix)


    def get_similar(self, index, n=10):
        similarity_list = list(enumerate(self.cosine_matrix[index]))
        similarity_list.sort(key=lambda x: x[1], reverse=True)
        # print(similarity_list)
        self.result = pd.DataFrame(columns=self.df.columns)
        for i in similarity_list[1:n+1]:
            # self.result = self.result.join(self.df.iloc[i[0]].toframe())

            self.result = pd.concat([self.result, self.df.iloc[i[0]].to_frame().T], ignore_index=True)
            # self.result.append(self.df.iloc[i[0]])
        print(self.result.head(5))
        return self.result



class CollegeCollegeRecommender(CollabFilter):

    def __init__(self):
        super().__init__()


    def clean_data(self):
        # clean anomolies
        self.df_clean = self.df.copy()
        def clean_anomolies(df):
            df['region'].replace(np.nan, 'national', inplace=True)
            df['ranks'].replace(-2, 999, inplace=True)
            df['ranks'].replace(-1, 999, inplace=True)
            # df['computerScienceRepScore'].replace([np.nan,'< 2.0'], 0, inplace=True)
            # df['engineeringRepScore'].replace([np.nan,'< 2.0'], 0, inplace=True)
            # df['businessRepScore'].replace([np.nan,'< 2.0'], 0, inplace=True)
            # df['nursingRepScore'].replace([np.nan,'< 2.0'], 0, inplace=True)


            # df['computerScienceRepScore'] = pd.to_numeric(df['computerScienceRepScore'])
            # df['engineeringRepScore'] = pd.to_numeric(df['engineeringRepScore'])
            # df['businessRepScore'] = pd.to_numeric(df['businessRepScore'])
            # df['nursingRepScore'] = pd.to_numeric(df['nursingRepScore'])

            # df['computerScienceRepScore'] = df['computerScienceRepScore'] - 4.0
            # df['engineeringRepScore'] = df['engineeringRepScore'] - 4.0
            # df['businessRepScore'] = df['businessRepScore'] - 4.0
            # df['nursingRepScore'] = df['nursingRepScore'] - 4.0
            return df

        self.df_clean = clean_anomolies(self.df_clean)

        drop = ['id','name','urlname','location']
        numeric = ['ranks','tuition','totalUndergraduate','costAfterAid','percentReceivingAid',
        'acceptanceRate','hsGpa','engineeringRepScore','businessRepScore', 'computerScienceRepScore', 'nursingRepScore']
        qualitative = ['ranking-type', 'region', 'fundingType']
        

        # drop unneeded features
        for f in drop:
            self.df_clean = self.df_clean.drop(f, axis=1)

        # extract all qualitative features using count vectorizer
        self.df_clean = count_vectorize(self.df_clean, qualitative, 'vector')
        print(self.df_clean.head(5))
        

        # standardize quantitative features


        

        return self



class UserUserRecommender(CollabFilter):

    def __init__(self):
        super().__init__()

    def clean_data(self):
        pass        

    