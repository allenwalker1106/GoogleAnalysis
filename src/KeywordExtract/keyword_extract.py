import  json
import pandas as pd 
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class KeywordExtractor:
    def __init__(self):

        pass


    def sort_coo(self,coo_matrix):
        tuples = zip(coo_matrix.col,coo_matrix.data)
        return sorted(tuples,key=lambda x: (x[1],x[0]),reverse=True)


    def extract_topn_from_vector(self,features_names,sorted_items, topn=10):
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []
        for idx, score in sorted_items:
            score_vals.append(round(score,3))
            feature_vals.append(features_names[idx])

        result = {}
        for idx in range(len(feature_vals)):
            result[feature_vals[idx]] = score_vals[idx]
        
        return result