# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:31:34 2020

@author: root
"""
import requests
from user_agent import UserAgent
from lxml import etree
class Crawl():
    def __init__(self):
        self.headers={}
    def crawlUrl(self,url):
        self.headers["user-agent"]=UserAgent.random()
        r=requests.get(url,headers=self.headers)
        if r.status_code==requests.codes.ALL_OK:
            html=etree.HTML(r.text)
        return html

class CrawlDeal():
    def toModel(self,html,**xpath):
        model={}
        modelList=[]
        names=[]
        list_len=0
        for k,v in xpath.items():
            names.append(k)
            model[k]=html.xpath(v)
            #假设种类数据一样多，否则装配数据有问题
            list_len=len(model[k])
        for i in range(list_len):
            obj={}
            for name in names:
                obj[name]=model.get(name).pop()
            modelList.insert(0,obj)
        return modelList
import time
from urllib.parse import urljoin
#数据存储等继承类
class DataDeal():
    def __init__(self):
        self.urlList=[]
        self.crawl=Crawl()
        self.crawlDeal=CrawlDeal()
    def deal(self,fisrt_url,npath,**xpath):
        #添加首页
        self.urlList.append(fisrt_url)
        #用于防止重复爬取尾页
        temp_next_page="next"
        while len(self.urlList)>0:
            html=self.crawl.crawlUrl(self.urlList.pop())
            dataList=self.crawlDeal.toModel(html,**xpath)
            #保存数据
            self.saveData(*dataList)
            #得到下一页
            next_page=html.xpath(npath)
            if len(next_page)>0:
                next_page=urljoin(fisrt_url,next_page.pop())
                if temp_next_page!=next_page:
                    self.urlList.append(next_page)
                    temp_next_page=next_page
                    print(temp_next_page)
                    print("下一页：%s"%next_page)
    def saveData(self,*dataList):
        for data in dataList:
            print("--------------------------------------------")
            print(data)
        time.sleep(2)
if __name__=="__main__":
    dataDeal=DataDeal()
    npath="//*[@id='paging_block']/div/a[last()]/@href"
    xpath={"title":"//div[@class='post_item_body']/h3/a/text()",
           "url":"//div[@class='post_item_body']/h3/a/@href"
           }
    fisrt_url="https://www.cnblogs.com/sitehome/p/198"
    dataDeal.deal(fisrt_url,npath,**xpath)