# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:32:52 2020

@author: Dell
"""


import scipy as np
from pylab import *
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
plot(x,c),plot(x,s)
show()