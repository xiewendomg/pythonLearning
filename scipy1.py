# -*- coding:utf-8 -*
from scipy.optimize import fsolve
def f(x):
    x1=x[0]
    x2=x[1]

    2 * x1 - x2 ** 2 ==1
    x1 ** 2 - x2==2
    return [2*x1-x2**2-1,x1**2-x2-2]
result=fsolve(f,[1,1])

print(result)