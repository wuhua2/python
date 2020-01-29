# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:17:27 2020

@author: root
"""
from blog import DataDeal
if __name__=="__main__":
    first_url="https://duanziwang.com/category/%E7%BB%8F%E5%85%B8%E6%AE%B5%E5%AD%90/"
    npath="/html/body/section/div/div/main/nav/a/@href"
    xpath={"joke":"//div[@class='post-content']/p/text()"}
    dataDeal=DataDeal()
    dataDeal.deal(first_url,npath,**xpath)