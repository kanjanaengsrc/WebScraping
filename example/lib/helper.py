# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

class Connect:
    def __init__(self,url,headers,payload):
        self.url = url
        self.headers = headers
        self.payload = payload
        self.sess = None
        self.status_code = None
        
    def doAuthen(self):
        with requests.Session() as self.sess:
            rez = self.sess.post(self.url,headers=self.headers,data=self.payload)
            return rez.status_code
    def getHTML(self,link):
        return (self.sess.get(link)).text

class MySoup:
    def __init__(self,html_text):
        self.soup = BeautifulSoup(html_text,'html.parser')
    
    def printParagraph(self,data):
        match = re.split(r'\r\n\s+',data)
        for i in match:
            if(i == None):
                continue
            print(i)
    
    def getMyStudent(self):
        content = self.soup.find_all('div',attrs={'class':'carbox-content'})
        if(len(content)== 0):
            print('You got no student')
        else:
            print('You got ',len(content),' of students')
        for row in content:
            print(re.search(r'\S.*$',row.h3.text).group(0))
            self.printParagraph(row.p.text)
            print('*************')