# importing the packages that would be necessary
import numpy as np # for numeric computation
import matplotlib.pyplot as plt # for plotting
######################################################

# first we need to define the function

def f(x):
    return np.exp(x) - np.exp(2.2087)

def bissection(f, a, b):

# settting the parameters
    tol = 0.0001

    if f(a)*f(b) > 0:
        print("wrong choice")
    else:
        k = ( a +  b)/2
        err = np.abs(f(k))
        while err > tol:
            if f(k) > 0:
                b = k
            else:
                a = k
            k = (a+b)/2
            err = np.abs(f(k))

        return np.around(k,5)


print(bissection(f, 0, 4))

############################################################################################################################################

# exercise 2 (Solving Nonlinear Equations - Newtons Method)

# the objective function will be given by

def d(x,c):
    return x**(-5) - x**(-3) - c

# question a)

x = np.arange(0.6, 10, 1) # defining the x-axis

plt.plot(x, d(x,1))
plt.hlines(y = 0, xmin = 0.6, xmax=10)
# by the graphic we can vizualize that the
# root is between 0.6 and 1

# defining the derivate
def  d_f(x):
    return -5*(x**(-6)) + 3*(x**(-4))

# finding the root of the function d, by newton method

def newton_root(d, d_f, ϵ, maxint, m_0):
    m = [m_0]
    for i in np.arange(0,maxint,1):
        m.append(m[i] - d(m[i],1)/ d_f(m[i]))
        if np.abs(θ[i+1]-θ[i]) < ϵ:
           break
    return m[-1],  np.round(d(m[-1],1))

# examples of different initial guess
newton_root(d,d_f,0.00001,1000, 0.6)
newton_root(d,d_f, 0.00001,1000, 2)
newton_root(d,d_f, 0.00001,1000, 3) # gives error d_f() is aproximately 0
newton_root(d,d_f, 0.00001,1000, 0.9)

# writing the same function but make depend of the parameter
# c of the function
def newton_root_c(d, d_f, ϵ, maxint, m_0, c):
    m = [m_0]
    for i in np.arange(0,maxint,1):
        m.append(m[i] - d(m[i],c)/ d_f(m[i]))
        if np.abs(θ[i+1]-θ[i]) < ϵ:
           break
    return m[-1],  d(m[-1],c)

# running a for, this calculates the root and check if it is
# really a root for d
for i in range(0,10):
    print(newton_root_c(d, d_f, 0.0001, 1000, 0.7, i))
