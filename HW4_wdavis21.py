import math
import numpy as np

def f(x):
    #return np.cos(x)-x
    #return x**3-2*x**2-5
    #return x-0.8-0.2*np.sin(x)
    #return 4*x**2-math.e**x-math.e**(-x)
    return (1/x)-2

def fprime(x):
    #return -1*np.sin(x)-1
    #return 3*x**2-4*x
    #return 1-0.2*np.cos(x)
    #return 8*x+math.e**(-x)-math.e**x
    return -1/(x**2)


#p0 = math.pi/4
#p0 = 2
#p0 = math.pi/4
#p0=-3
#p0=0
#p0=1 #zero division error: float division by zero
#p0=3
#p0=5
#p0=1.4 #overflow erro; result was too larg
#tol = 10**(-6)
tol = 10**(-5)
max_it = 50

for i in range (1,max_it):
    p = p0-(f(p0)/fprime(p0))
    eb = abs(p-p0)
    print("i={}, p={}, f(p)={}".format(i,p,f(p)))
    if(eb < tol):
        print(p)
        break
    else:
        p0=p








