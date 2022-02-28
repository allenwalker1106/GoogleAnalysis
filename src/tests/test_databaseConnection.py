from random import randrange
import os, sys
import json
import requests
from requests.structures import CaseInsensitiveDict

str_rootPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str_rootPath+'/src')


from DataCrawler.crawler import Crawler



strct_header = CaseInsensitiveDict()
strct_header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
strct_header["Content-Type"] = "application/json"






str_url = 'http://127.0.0.1:5000/search_by_id'

crawler = Crawler(True)
crawler.setGroupName('iqtree')
crawler.crawThreadCode()
arr_threadCode = crawler.arr_threadCode
str_groupName= 'iqtree'
for  thread_code in arr_threadCode :
    requestData = json.dumps(dict({
        'thread_code':thread_code,
        'group_name':'iqtree'
    }))
    print(requestData)
    print(requests.post(str_url,headers=strct_header,data=requestData))
    # break;

# print(crawler.arr_threadCode)