# -*- coding: utf-8 -*-
"""
For creating graph on python

Make sure to pre install scipy and pylab packages on your machine before using
this code.
"""
import scipy as np
from pylab import *
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)
plot(x,c),plot(x,s)
show()
