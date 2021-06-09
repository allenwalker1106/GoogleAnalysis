from random import randrange
import os, sys
import json

str_rootPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(str_rootPath+'/src')

from DataCrawler.crawler import Crawler

crawler = Crawler(True)
crawler.setGroupName('iqtree')
# crawler.crawThreadCode()
# print(crawler.arr_threadCode)

crawler.crawThreadData('qpAyooApcDA')
print(crawler.dict_groupData['qpAyooApcDA'])

crawler.exportJsonFile(str_rootPath+'/data/assert')