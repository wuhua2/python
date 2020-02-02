# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:35:51 2020

@author: root
"""

import requests
from lxml import etree

if __name__=="__main__":
    r=requests.get("https://www.cnblogs.com/")
    html=etree.HTML(r.text)
    #查找Next
    print(html.xpath("//a[starts-with(text(),'Next')]/text()"))
    print(html.xpath("//a[starts-with(text(),'Next')]/@href"))