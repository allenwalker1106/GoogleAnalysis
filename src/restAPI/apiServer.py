from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from flask import  render_template  
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np
import datetime
import flask
import io
import sys,os
import keras
import pickle


str_rootPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str_rootPath+'/src')


from DataCrawler.crawler import Crawler
from TextProcess.textProcess import TextProcess
from KeywordExtract.keyword_extract import KeywordExtractor
from DatabaseConnection.data_handle import DataHandle

app = flask.Flask(__name__,template_folder=str_rootPath+'/src/webApp/templates')
CORS(app)
model = None
tokenizer = None
tfidf=None
vectorizer = None

crawler = Crawler()
data_handle = DataHandle()
keyword_extractor = KeywordExtractor()
textProcessor = TextProcess()

int_maxLength=500
f_threshold = 0.45
arr_tags=['Reading from folder','Automatic model selection','Substitution model options','Bug report','Rate heterogeneity options','Ascertainment bias correction option','Partition model options','Mixture model options','Heterotachy model options','Site specific frequency model options','Polymorphism aware model options','Automatic partition merging','Tree search parameters','Constrained tree search','Ultrafast bootstrap parameters','Nonparametric bootstrap','Single branch tests','Tree topology tests','Concordance factor','Phylogenetic dating','Ancestral sequence reconstruction','Constructing consensus tree','Propose feature','Likelihood mapping analysis','Utilizing multi core CPUs','Inferring site specific rates','Reducing impact of severe model violations with UFBoot']


def loadTfidModel():
    global tfidf
    global vectorizer
    tfidf = pickle.load(open(str_rootPath+'/data/model/keywordExtractor/tfidf.pkl','rb'))
    vectorizer = pickle.load(open(str_rootPath+'/data/model/keywordExtractor/vectorizer.pkl','rb'))
    pass


def loadTokenizer():
    global tokenizer 
    tokenizer = Tokenizer(num_words=5000)
    with open(str_rootPath+'/data/model/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

def loadModel():
    global model
    model = keras.models.load_model(str_rootPath+'/data/model/TagPredictModel.h5')

def extractData(str_threadCode):
    crawler.crawThreadData(str_threadCode)

def normalize(arr_pred):
    global f_threshold
    arr_res=[]
    for dat in arr_pred:
        if(dat>=f_threshold):
            arr_res.append(1)
        else:
            arr_res.append(0)
    return arr_res

def processText(dict_data):
    return(textProcessor.procecssDictionary(dict_data))

def predictTag(str_textData):
    global model
    x = tokenizer.texts_to_sequences([str_textData])
    x=pad_sequences(x, padding='post', maxlen=int_maxLength)
    pred = model.predict(x)[0]
    pred = normalize(pred)
    return pred

def extractKeyword(str_textData,int_numberKeyword=10):
    global vectorizer
    global tfidf
    feature_names = vectorizer.get_feature_names()
    tf_idf_vector=tfidf.transform(vectorizer.transform([str_textData]))
    sorted_items = keyword_extractor.sort_coo(tf_idf_vector.tocoo())
    keywords = keyword_extractor.extract_topn_from_vector(feature_names,sorted_items,int_numberKeyword)
    return keywords

@app.route('/search_by_tag',methods=['POST'])
def search_by_tag():
    data={'success':False}
    if(flask.request.method=='POST'):
        if(flask.request.json):
            dict_data=dict()
            searchable_tag=[]
            try:
                str_tag      = flask.request.json['tag']
            except:
                str_tag      = ''
            try:
                str_startDate       = flask.request.json['start_date']
                str_startDate=datetime.datetime.strptime(str_startDate,'%Y-%m-%d')
            except:
                str_startDate       = ''
            try:
                str_endDate         = flask.request.json['end_date']
                str_endDate=datetime.datetime.strptime(str_endDate,'%Y-%m-%d')
            except:
                str_endDate         = ''
            
            filter_result = data_handle.getItemByTag(str_tag,str_startDate,str_endDate)
            response = [] 
            for item in filter_result: 
                response.append(item)
        
            data['response']=list(response)
            data['success']= True

    return flask.jsonify(data)


@app.route('/search_by_keyword',methods=['POST'])
def search_by_keyword():
    data={'success':False}
    if(flask.request.method=='POST'):
        if(flask.request.json):
            dict_data=dict()
            searchable_tag=[]
            try:
                str_keyword      = flask.request.json['keyword']
            except:
                str_keyword      = ''
            try:
                str_startDate       = flask.request.json['start_date']
                str_startDate=datetime.datetime.strptime(str_startDate,'%Y-%m-%d')
            except:
                str_startDate       = ''
            try:
                str_endDate         = flask.request.json['end_date']
                str_endDate=datetime.datetime.strptime(str_endDate,'%Y-%m-%d')
            except:
                str_endDate         = ''
            
            filter_result = data_handle.getItemByKeyword(str_keyword,str_startDate,str_endDate)
            response = [] 
            for item in filter_result: 
                response.append(item)

            data['response']=list(response)
            data['success']= True

    return flask.jsonify(data)


@app.route('/search_by_id',methods=['POST'])
def search_by_id():
    data={'success':False}
    if(flask.request.method=='POST'):
        if(flask.request.json):
            dict_data=dict()
            searchable_tag=[]
            try:
                str_threadCode      = flask.request.json['thread_code']
            except:
                str_threadCode      = ''
            try:
                str_groupName       = flask.request.json['group_name']
            except:
                str_groupName       = 'iqtree'
            try:
                str_startDate       = flask.request.json['start_date']
            except:
                str_startDate       = ''
            try:
                str_endDate         = flask.request.json['end_date']
            except:
                str_endDate         = ''
            try:
                int_displayNumber   = flask.request.json['display_number']
            except:
                int_displayNumber   = 10

            crawler.setGroupName(str_groupName)
            
            crawler.crawThreadData(str_threadCode)  
            
            dict_data[str_threadCode] = crawler.dict_groupData[str_threadCode]
            
            dict_data = processText(dict_data)

            keywords = extractKeyword(dict_data[str_threadCode]['content'],int_displayNumber)
            
            predict_result = predictTag(dict_data[str_threadCode]['content'])   

            for index in range(len(predict_result)):
                if(predict_result[index]):
                    searchable_tag.append(arr_tags[index])




            data['thread_code']=str_threadCode
            data['group_name'] =str_groupName
            data['keywords'] = list(keywords.keys())
            data['keywords_props']=keywords
            data['searchable_tag']=searchable_tag
            data['tags']= predict_result
            data['init_date']= dict_data[str_threadCode]['initializeDate']
            data['last_update'] = dict_data[str_threadCode]['timeStamp']
            # data['dict_data']= dict_data
            data['success'] = True
            data_handle.insertOne(data)
    
    return flask.jsonify(data)
    
if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    loadTokenizer()
    loadModel()
    loadTfidModel()
    app.run()
