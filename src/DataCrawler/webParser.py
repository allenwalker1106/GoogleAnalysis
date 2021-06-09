from html.parser import HTMLParser
from datetime import date
import json
import io
import re

class WebParser(HTMLParser):

    def __init__(self,bool_debugMode = False):
        HTMLParser.__init__(self)
        self.initialize(bool_debugMode)
        
        pass

    def initialize(self,bool_debugMode):
        self.bool_debugMode=bool_debugMode
        self.int_commentSectionCounter =0
        self.bool_inCommentSection = False

        self.int_dateSectionCounter =0
        self.bool_inDateSection=False

        self.int_topicSectionCounter =0
        self.bool_inTopicSection=False
        
        self.arr_postData =[] 
        self.arr_date=[]
        self.arr_topic=[]
        
        self.str_comment=''
        self.str_date=''
        self.str_topic=''
        if(self.bool_debugMode):
            self.writeLog('=========initialize=========') 
            self.writeLog('List of changed variable:')
            self.writeLog('var name:')
            self.writeLog('self.int_commentSectionCounter')
            self.writeLog('var type:')
            self.writeLog(type(self.int_commentSectionCounter))
            self.writeLog('var value:')
            self.writeLog(self.int_commentSectionCounter)
            self.writeLog('var name:')
            self.writeLog('self.bool_inCommentSection')
            self.writeLog('var type:')
            self.writeLog(type(self.bool_inCommentSection))
            self.writeLog('var value:')
            self.writeLog(self.bool_inCommentSection)
            self.writeLog('self.int_dateSectionCounter')
            self.writeLog('var type:')
            self.writeLog(type(self.int_dateSectionCounter))
            self.writeLog('var value:')
            self.writeLog(self.int_dateSectionCounter)
            self.writeLog('self.bool_inDateSection')
            self.writeLog('var type:')
            self.writeLog(type(self.bool_inDateSection))
            self.writeLog('var value:')
            self.writeLog(self.bool_inDateSection)
            self.writeLog('self.int_topicSectionCounter')
            self.writeLog('var type:')
            self.writeLog(type(self.int_topicSectionCounter))
            self.writeLog('var value:')
            self.writeLog(self.int_topicSectionCounter)
            self.writeLog('self.arr_postData')
            self.writeLog('var type:')
            self.writeLog(type(self.arr_postData))
            self.writeLog('var value:')
            self.writeLog(self.arr_postData)
            self.writeLog('self.arr_date')
            self.writeLog('var type:')
            self.writeLog(type(self.arr_date))
            self.writeLog('var value:')
            self.writeLog(self.arr_date)
            self.writeLog('self.arr_topic')
            self.writeLog('var type:')
            self.writeLog(type(self.arr_topic))
            self.writeLog('var value:')
            self.writeLog(self.arr_topic)
            self.writeLog('self.str_comment')
            self.writeLog('var type:')
            self.writeLog(type(self.str_comment))
            self.writeLog('var value:')
            self.writeLog(self.str_comment)
            self.writeLog('self.str_date')
            self.writeLog('var type:')
            self.writeLog(type(self.str_date))
            self.writeLog('var value:')
            self.writeLog(self.str_date)
            self.writeLog('self.str_topic')
            self.writeLog('var type:')
            self.writeLog(type(self.str_topic))
            self.writeLog('var value:')
            self.writeLog(self.str_topic)
            self.writeLog('=========initialize=========')  
            

    def feed(self,str_data):
        self.initialize(self.bool_debugMode)
        HTMLParser.feed(self,str_data)
        pass
    
    def handleStartDiv(self, arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='ptW7te'): 
                self.bool_inCommentSection = True

        if(self.bool_inCommentSection):
            self.int_commentSectionCounter+=1

        pass

    def handleEndDiv(self):
        if(self.bool_inCommentSection):
            self.int_commentSectionCounter-=1
            if(not self.int_commentSectionCounter):
                self.bool_inCommentSection=False
                self.arr_postData.append(self.str_comment)
                self.str_comment=''
        pass

    def handleDivData(self,str_data):
        str_data = str_data.strip().replace('\n',' ')
        str_data = re.sub(r'\s+',' ',str_data)
        if(len(str_data)>2):
            self.str_comment +=str_data+' '
        if(self.bool_debugMode):
            self.writeLog('=========handleDivData=========') 
            self.writeLog('Input name:')
            self.writeLog('str_data')
            self.writeLog('Input type:')
            self.writeLog(type(str_data))
            self.writeLog('Input value:')
            self.writeLog(str_data)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('self.str_comment')
            self.writeLog('Output type:')
            self.writeLog(type(self.str_comment))
            self.writeLog('Output value:')
            self.writeLog(self.str_comment)
            self.writeLog('=========handleDivData=========') 
        pass

    def handleStartSpan(self,arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='zX2W9c'):
                self.bool_inDateSection = True
            if(self.bool_inDateSection):
                self.int_dateSectionCounter +=1
        pass

    def handleEndSpan(self):
        if(self.bool_inDateSection):
            self.int_dateSectionCounter-=1
            if(not self.int_dateSectionCounter):
                self.bool_inDateSection=False
                self.arr_date.append(self.str_date)
                self.str_date=''
        pass

    def handleSpanData(self,str_data):
        self.str_date+=str_data
        if(self.bool_debugMode):
            self.writeLog('=========handleSpanData=========') 
            self.writeLog('Input name:')
            self.writeLog('str_data')
            self.writeLog('Input type:')
            self.writeLog(type(str_data))
            self.writeLog('Input value:')
            self.writeLog(str_data)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('self.str_date')
            self.writeLog('Output type:')
            self.writeLog(type(self.str_date))
            self.writeLog('Output value:')
            self.writeLog(self.str_date)
            self.writeLog('=========handleSpanData=========')  
        pass

    def handleStartTopic(self,arr_attribute):
        for attribute in arr_attribute:
            if(attribute[0]=='class' and attribute[1]=='KPwZRb'):
                self.bool_inTopicSection = True
            if(self.bool_inTopicSection):
                self.int_topicSectionCounter +=1
        pass

    def handleEndTopic(self):
        if(self.bool_inTopicSection):
            self.int_topicSectionCounter-=1
            if(not self.int_topicSectionCounter):
                self.bool_inTopicSection=False
                self.arr_topic.append(self.str_topic)
                self.str_topic=''
        pass

    def handleTopicData(self,str_data):
        self.str_topic+=str_data
        if(self.bool_debugMode):
            self.writeLog('=========handleTopicData=========') 
            self.writeLog('Input name:')
            self.writeLog('str_data')
            self.writeLog('Input type:')
            self.writeLog(type(str_data))
            self.writeLog('Input value:')
            self.writeLog(str_data)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('self.str_topic')
            self.writeLog('Output type:')
            self.writeLog(type(self.str_topic))
            self.writeLog('Output value:')
            self.writeLog(self.str_topic)
            self.writeLog('=========handleTopicData=========')  
        pass

    def handle_starttag(self,str_tag,arr_attribute):
        if(str_tag =='div'):
            self.handleStartDiv(arr_attribute)
        elif(str_tag=='span'):
            self.handleStartSpan(arr_attribute)
        elif(str_tag =='h1'):
            self.handleStartTopic(arr_attribute)
        pass

    def handle_endtag(self,str_tag):
        if(str_tag =='div'):
            self.handleEndDiv()
        elif(str_tag=='span'):
            self.handleEndSpan()
        elif(str_tag=='h1'):
            self.handleEndTopic()
        pass

    def handle_data(self,str_data):
        if(self.bool_inCommentSection):
            self.handleDivData(str_data)
        elif(self.bool_inDateSection):
            self. handleSpanData(str_data)
        elif(self.bool_inTopicSection):
            self.handleTopicData(str_data)
        if(self.bool_debugMode):
            self.writeLog('=========handle_data=========') 
            self.writeLog('Input name:')
            self.writeLog('str_data')
            self.writeLog('Input type:')
            self.writeLog(type(str_data))
            self.writeLog('Input value:')
            self.writeLog(str_data)
            self.writeLog(' ')
            self.writeLog('Output name:')
            self.writeLog('str_data')
            self.writeLog('Output type:')
            self.writeLog(type(str_data))
            self.writeLog('Output value:')
            self.writeLog(str_data)
            self.writeLog('=========handle_data=========')  
        pass

    def toDictionary(self):
        dict_data = {
            'topic':self.arr_topic[0],
            'initializeDate':self.arr_date[0],
            'timeStamp':self.arr_date[-1],
            'content':self.arr_postData
        }

        return dict_data

    def writeLog(self,str_logString):
        try:
            str_filePath = 'log/'+str(date.today())+'.log'
            fs_logStream = open(str_filePath,'a')
            str_date = '['+str(date.today())+'][web_parser.py] '
            fs_logStream.write(str_date+str(str_logString)+'\n')
            fs_logStream.close()

        except:
            print('=========writeLog=========')
            print('except call')
            print('=========writeLog=========')

        pass


