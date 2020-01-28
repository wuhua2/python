# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:31:34 2020

@author: root
"""
import requests
from user_agent import UserAgent
class Crawl():
    def __init__(self):
        self.headers={}
    def crawlUrl(self,url):
        self.headers["user-agent"]=UserAgent.random()
        r=requests.get(url,headers=self.headers)
        if r.status_code==requests.codes.ALL_OK:
            result=r.text
        return result
from lxml import etree
class CrawlDeal():
    def __toHtml(self,result):
        return etree.HTML(result)
    def toModel(self,result,**xpath):
        model={}
        modelList=[]
        names=[]
        list_len=0
        html=self.__toHtml(result)
        for k,v in xpath.items():
            names.append(k)
            model[k]=html.xpath(v)
            list_len=len(model[k])
        for i in range(list_len):
            obj={}
            for name in names:
                obj[name]=model.get(name).pop()
            modelList.insert(0,obj)
        return modelList
if __name__=="__main__":
    crawl=Crawl()
    result=crawl.crawlUrl("https://www.cnblogs.com/pick/2/")
    deal=CrawlDeal()
    xpath={"title":"//div[@class='post_item_body']/h3/a/text()",
           "url":"//div[@class='post_item_body']/h3/a/@href"
           }
    blog_list=deal.toModel(result,**xpath)
    print(blog_list)