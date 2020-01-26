# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
def quadratic(a, b, c):
    if a==0:
        print("这不是一元二次方程\n")
    if b**2-4*a*c<0:
        print('该方程没有解\n')
    elif b**2-4*a*c==0:
        print('该方程只有一个解\n')
        print('解为:{0}'.format((-b+math.sqrt(b**2-4*a*c))/(2*a)))
    else:
        print('该方程有二个解\n')
        print('解1为:{0} 解2为:{1}'.format((-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)))
if __name__=="__main__":
    quadratic(1,1,1)