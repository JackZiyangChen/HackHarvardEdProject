import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



class CollabFilter:

    def __init__(self):
        self.df = pd.DataFrame()
        self.df_clean = pd.DataFrame()
        self.result = pd.DataFrame()
        self.cosine_matrix = np.array([])

    def clean_data(self):
        # note: DO NOT sort df
        return self

    def run(self):
        matrix = self.df_clean.to_numpy()
        self.cosine_matrix = cosine_similarity(matrix)
        self.result = pd.DataFrame(self.cosine_matrix)

    def get_similar(self, index, n=10):
        return self.result[index].sort_values(ascending=False)[1:n+1]



class CollegeCollegeRecommender(CollabFilter):

    def __init__(self):
        super()

    def clean_data(self):
        pass



class UserUserRecommender(CollabFilter):

    def __init__(self):
        super()

    def clean_data(self):
        pass        

    