import pymongo
import os 
import json
from os.path import join, dirname
from dotenv import load_dotenv
import datetime
import re
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

str_databaseURL = 'mongodb://localhost:27017/'

str_databaseName = os.environ.get("DATABASE_NAME")
str_collectionName = os.environ.get("DATABASE_COLLECTION_NAME")


class DataHandle :
    def __init__(self):
        self.client = pymongo.MongoClient(str_databaseURL)
        self.database = self.client[str_databaseName]
        self.collection = self.database[str_collectionName]
        pass 

    def insertOne(self,dict_data):
        insert_data = dict({
            'thread_code': dict_data['thread_code'],
            'init_date':datetime.datetime.strptime(re.findall(r'\s*(\w+\s+\d+,\s+\d+,\s+\d+:\d+:\d+\s+\w+)\s*',dict_data['init_date'])[0],'%b %d, %Y, %H:%M:%S %p'),
            'last_update':datetime.datetime.strptime(re.findall(r'\s*(\w+\s+\d+,\s+\d+,\s+\d+:\d+:\d+\s+\w+)\s*',dict_data['last_update'])[0],'%b %d, %Y, %H:%M:%S %p'),
            'tags':dict_data['tags'],
            'keywords':dict_data['keywords'],
            'keywords_props': dict_data['keywords_props'],
            'searchable_tag':dict_data['searchable_tag']
        })
        filter = {'thread_code': dict_data['thread_code']}
        self.collection.update_one(filter,{'$set':insert_data},upsert=True)
        # self.collection.up
        pass

    def insertAll(self,dict_data):
        arr_insertData= []
        for data in dict_data:

            insert_data = dict({
                'thread_code': data['thread_code'],
                'init_date':data['init_date'],
                'last_update':data['last_update'],
                'tags':data['tags'],
                'keywords':data['keywords'],
                'keywords_props': data['keywords_props'],
                'searchable_tag':data['searchable_tag']
            })
            self.insertOne(insert_data)
        pass

    def getItemByTag(self,str_tag,str_startDate='',str_endDate=''):
        if(len(str(str_startDate))!= 0 and len(str(str_endDate))!=0):
            filter = {'searchable_tag':{'$in':[str_tag]},'last_update':{'$gt':str_startDate,'$lt':str_endDate}}
        else:
            filter = {'searchable_tag':{'$in':[str_tag]}}
        result = self.collection.find(filter,{'_id':0})
        return result

    def getItemByKeyword(self,str_keyword,str_startDate='',str_endDate=''):
        if(len(str(str_startDate))!= 0 and len(str(str_endDate))!=0):
            filter = {'keywords':{'$in':[str_keyword]},'last_update':{'$gt':str_startDate,'$lt':str_endDate}}
        else:
            filter = {'keywords':{'$in':[str_keyword]}}
        result = self.collection.find(filter,{'_id':0})
        # print(filter)
        return result


    def getItemByThreadID(self,str_threadID):
        filter = {'thread_code':str_threadID}
        result = self.collection.find(filter,{'_id':0})
        return result
