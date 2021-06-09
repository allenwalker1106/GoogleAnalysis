from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from datetime import date 
import json
import re 
import nltk
import io

class TextProcess:

    def __init__(self,bool_debugMode = False):
        self.bool_debugMode = bool_debugMode
        self.c_stemmer = PorterStemmer()
        self.arr_stopWords = set(stopwords.words('english'))
        self.c_lemma = WordNetLemmatizer()
        self.arr_month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Dec', 'Nov', 'Oct']
        pass

    def cleanURL(self,str_line):
        str_urlClear= re.sub(r'http\S+',' ',str_line)

        if(self.bool_debugMode):
            self.writeLog('=========cleanURL=========') 
            self.writeLog('Input name:')
            self.writeLog('str_line')
            self.writeLog('Input type:')
            self.writeLog(type(str_line))
            self.writeLog('Input value:')
            self.writeLog(str_line)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('str_urlClear')
            self.writeLog('Output type:')
            self.writeLog(type(str_urlClear))
            self.writeLog('Output value:')
            self.writeLog(str_urlClear)
            self.writeLog('=========cleanURL=========')  

        return str_urlClear
        pass

    def cleanSymbol(self,str_line):
        str_symbolClear= re.sub(r'[^a-zA-Z]',' ',str_line)

        if(self.bool_debugMode):
            self.writeLog('=========cleanSymbol=========') 
            self.writeLog('Input name:')
            self.writeLog('str_line')
            self.writeLog('Input type:')
            self.writeLog(type(str_line))
            self.writeLog('Input value:')
            self.writeLog(str_line)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('str_symbolClear')
            self.writeLog('Output type:')
            self.writeLog(type(str_symbolClear))
            self.writeLog('Output value:')
            self.writeLog(str_symbolClear)
            self.writeLog('=========cleanSymbol=========')  

        return str_symbolClear
        pass
    
    def cleanStopWord(self,arr_token):
        arr_clearStopwords =[ token for token in arr_token if token not in self.arr_stopWords ]

        
        if(self.bool_debugMode):
            self.writeLog('=========cleanStopWord=========') 
            self.writeLog('Input name:')
            self.writeLog('cleanStopWord')
            self.writeLog('Input type:')
            self.writeLog(type(arr_token))
            self.writeLog('Input value:')
            self.writeLog(arr_token)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_clearStopwords')
            self.writeLog('Output type:')
            self.writeLog(type(arr_clearStopwords))
            self.writeLog('Output value:')
            self.writeLog(arr_clearStopwords)
            self.writeLog('=========cleanStopWord=========')  


        return arr_clearStopwords

    def tokenize(self,str_line):
        arr_token = word_tokenize(str_line)
        
        if(self.bool_debugMode):
            self.writeLog('=========tokenize=========') 
            self.writeLog('Input name:')
            self.writeLog('str_line')
            self.writeLog('Input type:')
            self.writeLog(type(str_line))
            self.writeLog('Input value:')
            self.writeLog(str_line)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_token')
            self.writeLog('Output type:')
            self.writeLog(type(arr_token))
            self.writeLog('Output value:')
            self.writeLog(arr_token)
            self.writeLog('=========tokenize=========')  


        return arr_token

        pass

    def stemming(self,arr_token):
        arr_stemming = [self.c_stemmer.stem(token) for token in arr_token]
        
        if(self.bool_debugMode):
            self.writeLog('=========stemming=========') 
            self.writeLog('Input name:')
            self.writeLog('arr_token')
            self.writeLog('Input type:')
            self.writeLog(type(arr_token))
            self.writeLog('Input value:')
            self.writeLog(arr_token)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_stemming')
            self.writeLog('Output type:')
            self.writeLog(type(arr_stemming))
            self.writeLog('Output value:')
            self.writeLog(arr_stemming)
            self.writeLog('=========stemming=========')  
        
        return arr_stemming 

        pass

    def lengthFilter(self,arr_token):
        arr_filterToken = [token for token in arr_token if len(token) > 2]

        if(self.bool_debugMode):
            self.writeLog('=========LengthFilter=========') 
            self.writeLog('Input name:')
            self.writeLog('arr_token')
            self.writeLog('Input type:')
            self.writeLog(type(arr_token))
            self.writeLog('Input value:')
            self.writeLog(arr_token)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_filterToken')
            self.writeLog('Output type:')
            self.writeLog(type(arr_filterToken))
            self.writeLog('Output value:')
            self.writeLog(arr_filterToken)
            self.writeLog('=========LengthFilter=========')  
        
        return arr_filterToken

        pass
    
    def lemmatization(self,arr_token):
        arr_lemma=  [self.c_lemma.lemmatize(word=str_word,pos='v') for str_word in arr_token] 

        if(self.bool_debugMode):
            self.writeLog('=========lemmatization=========') 
            self.writeLog('Input name:')
            self.writeLog('arr_token')
            self.writeLog('Input type:')
            self.writeLog(type(arr_token))
            self.writeLog('Input value:')
            self.writeLog(arr_token)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_lemma')
            self.writeLog('Output type:')
            self.writeLog(type(arr_lemma))
            self.writeLog('Output value:')
            self.writeLog(arr_lemma)
            self.writeLog('=========lemmatization=========')  
        
        return arr_lemma

        pass
   
    def processText(self,str_line):
        str_textData= str_line.lower()
        str_textData = self.cleanURL(str_textData)
        str_textData= self.cleanSymbol(str_textData)
        arr_token= self.tokenize(str_textData)
        arr_token = self.cleanStopWord(arr_token)
        arr_token = self.lemmatization(arr_token)
        arr_token = self.lengthFilter(arr_token)
        str_textData = ' '.join(arr_token)

        if(self.bool_debugMode):
            self.writeLog('=========processText=========') 
            self.writeLog('Input name:')
            self.writeLog('str_line')
            self.writeLog('Input type:')
            self.writeLog(type(str_line))
            self.writeLog('Input value:')
            self.writeLog(str_line)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_lemma')
            self.writeLog('Output type:')
            self.writeLog(type(str_textData))
            self.writeLog('Output value:')
            self.writeLog(str_textData)
            self.writeLog('=========processText=========')  
        

        return str_textData

        pass

    def procecssDictionary(self,dict_data):
        dict_sampleData = dict(dict_data)
        for key in dict_data:
            topic = dict_data[key]['topic']
            initializeDate = dict_data[key]['initializeDate']
            timeStamp = dict_data[key]['timeStamp']
            content = dict_data[key]['content']
            str_combineText = topic + ' '.join(content)
            str_processText = self.processText(str_combineText)
            dict_sampleData[key]['content']=str_processText
        if(self.bool_debugMode):
            self.writeLog('=========procecssDictionary=========') 
            self.writeLog('Input name:')
            self.writeLog('dict_data')
            self.writeLog('Input type:')
            self.writeLog(type(dict_data))
            self.writeLog('Input value:')
            self.writeLog(dict_data)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('arr_lemma')
            self.writeLog('Output type:')
            self.writeLog(type(dict_sampleData))
            self.writeLog('Output value:')
            self.writeLog(dict_sampleData)
            self.writeLog('=========procecssDictionary=========') 
        return dict_sampleData
        pass


    def convertTime(self,str_line):
        arr_time=re.findall(r'(\w+)\s+(\d+),\s+(\d+),\s+(\d+):\d+:\d+\s+(\w+)',str_line)[0]
        int_time = (self.arr_month.index(arr_time[0]))*30*24+int(arr_time[1])*24+int(arr_time[2])*365*24+int(arr_time[3])
        if(arr_time[4]=='PM'):
            int_time+=12

        if(self.bool_debugMode):
            self.writeLog('=========convertTime=========') 
            self.writeLog('Input name:')
            self.writeLog('str_line')
            self.writeLog('Input type:')
            self.writeLog(type(str_line))
            self.writeLog('Input value:')
            self.writeLog(str_line)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('int_time')
            self.writeLog('Output type:')
            self.writeLog(type(int_time))
            self.writeLog('Output value:')
            self.writeLog(int_time)
            self.writeLog('=========convertTime=========')  
        
        return int_time

        pass

    def writeLog(self,str_logString):
        try:
            str_filePath = 'log/'+str(date.today())+'.log'
            fs_logStream = open(str_filePath,'a')
            str_date = '['+str(date.today())+'][textProcess.py] '
            fs_logStream.write(str_date+str(str_logString)+'\n')
            fs_logStream.close()

        except:
            print('=========writeLog=========')
            print('except call')
            print('=========writeLog=========')

        pass
