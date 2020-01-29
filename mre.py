# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:14:48 2020

@author: root
"""
import re
m=re.match(r"^(\d{3})\-(\d{3,8})$","010-12345")
if m:
    print("匹配")
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
else:
    print("不匹配")
