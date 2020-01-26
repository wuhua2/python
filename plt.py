# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:46:01 2019

@author: root
"""
import numpy as np
import matplotlib.pyplot as plt
ls=list(range(1,11))
y=[l**2-5*l-20 for l in ls]
plt.style.use('ggplot')
plt.plot(ls,y,'r')
plt.ylabel('y')
plt.show()
