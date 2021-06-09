from random import randrange
import os, sys
import json

str_rootPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str_rootPath+'/src')

from TextProcess.textProcess import TextProcess

text_processor = TextProcess(bool_debugMode=True)

dict_data= json.load(open((str_rootPath+'/data/assert/iqtree.json'),'r'))

arr_keys = list(dict_data.keys())

str_randomKey = arr_keys[randrange(0,len(arr_keys))]

dict_threadData = dict_data[str_randomKey]

str_textData = dict_threadData['topic']+' '.join(dict_threadData['content'])

str_processedText = text_processor.processText(str_textData)

print(str_processedText)