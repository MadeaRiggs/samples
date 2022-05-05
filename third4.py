from re import A
from tkinter import N
from scipy.constants import *
print(pi)
print(c)
print(speed_of_light)
print(h)
print(G)
print(electron_mass)

import scipy.fft
import numpy as np

a=np.exp(2j * np.pi * np.arange(8) /8)
print(a)
b=scipy.fft.fft(a) #computes the 1-D Discrete Fourier Transform
print(b)
print(scipy.fft.ifft(b)) #computes the 1-D inverse Discrete Fourier Transform

#sub-package for objects used in interpolation
from scipy import interpolate as intp
import matplotlib.pyplot as plt

"""
x=np.linspace(0, 4, 12)
y=np.cos(x**2/3 + 4)
plt.plot(x, y, 'o')
plt.show()
#interp1d(x, y[, kind, axis, copy, …]): Interpolate a 1-D function
f1=intp.interp1d(x, y, kind='linear') #'kind' Specifies the type of interpolation as a string
f2=intp.interp1d(x, y, kind='cubic')
xnew=np.linspace(0, 4, 300)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic', 'nearest'], loc='best')
plt.show()
"""


#UnivariateSpline(x, y[, w, bbox, k, s, ext, …]): 1-D smoothing spline fit to a given set of datapoints.
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

"""
#with no smootin factor
x=np.linspace(-3, 3, 50)
y=np.exp(-x**2) + 0.1 * np.random.randn(50) #add noise by random method 
plt.plot(x, y, 'ro', ms=5)
plt.show()

plt.plot(x, y, 'ro', ms=5)
xs=np.linspace(-3, 3, 1000)
spl=UnivariateSpline(x, y)
spl.set_smoothing_factor(0)
plt.plot(xs, spl(xs), 'yellow', lw=3) #yellow line
plt.show()

plt.plot(x, y, 'ro', ms=5)
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'green', lw=3) #green line
plt.show()

plt.plot(x, y, 'ro', ms=5)
spl.set_smoothing_factor(100)
plt.plot(xs, spl(xs), 'blue', lw=3) #blue line
plt.show()
"""

#solving a linear system
from scipy import linalg
a=np.array([[1,3,5], [2,5,1], [2,3,8]])
b=np.array([10,8,3])
print(a)
print(b) 
"""
solution to the linear system
𝑥 + 3𝑦 + 5𝑧 = 10
2𝑥 + 5𝑦 + 𝑧 = 8
2𝑥 + 3𝑦 + 8𝑧 = 3
"""
x=linalg.solve(a,b)
print(x)

#finding Determinant of array A
A=np.array([[1,2], [3,4]])
print(A)
print(linalg.det(A))

#finding Eigenvalues and Eigenvectors which find scalars and corresponding vectors of a square matrix
B=np.array([[3,4], [7,8]])
eigenvalue,eigenvector=linalg.eig(B)
print(eigenvalue)
print(eigenvector)

#finding Singular Value Decomposition(SVD) which is similar to Eigenvalue and Eigenvector but for matrices that are not square 
C=np.array([[1,2,3], [4,5,6]])
print(C)
M,N=C.shape
U,s,Vh=linalg.svd(C)
Sig=linalg.diagsvd(s,M,N)
print(Sig)
print(Vh)
print(U.dot(Sig.dot(Vh))) #checks computation
print(U@Sig@Vh)












