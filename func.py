# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:08:40 2020

@author: root
"""
import time
def log(func):
    def wrapper(*args,**kw):
        print("当前时间:%s"%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        return func(*args,**kw)
    return wrapper
@log
def say_nothing():
    print("我正在乱说话...")
if __name__=="__main__":
    say_nothing()