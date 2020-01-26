# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:00:41 2020

@author: root
"""

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def message(self):
        print("name=%s age=%s"%(self.name,self.age))