from cmath import e
from distutils.util import run_2to3
from turtle import dot
import numpy as np

"""
a=np.array([1,2,3,4,5]) #creates an array and makes a copy of the object
a=np.array([1,2], dtype=np.float32)
print("data not changed: ", np.array(a, dtype=np.float32)is a)
print("data changed: ", np.array(a, dtype=np.float64)is a)
print("data not changed: ", np.asarray(a, dtype=np.float32)is a)
print("data not changed: ", np.asarray(a, dtype=np.float64)is a)
print("one dimensional array: ", a) #one-dimensional array
b=np.array([[1,2,3],[4,5,6]]) #multi-dimensional array
print("multidimensional array: ", b)

c=np.zeros([2,2]) #creates an array full of zeros
print("array full of zeros: ", c)
d=np.ones([2,2]) #creates an array full of ones
print("array full of ones: ", d)
e=np.empty([3,4]) #creates an array whose initial content is random and depends on the stateof the memory.
print("array whose initial content is random: ", e)

print(np.eye(5)) #return a 2-D array with ones on the diagonal and zero elsewhere
e=np.asarray([1,2,3,4,5,6]) #convert the input to an array and does not make a copy of the object unless necessary
print("one-dimensional array: ", e)

f=np.arange(10,20,2) #creates sequences of numbers and returns an array with the start(start of interval), stop(end of interval) and step(spacing between values)
print("sequences of numbers in array: ", f)

g=np.linspace(0,99,10) #returns evenly spaced numbers over a specified interval with start stop and interval
print(g)

a=np.array([[1,2],[3,4],[5,6]])
print(a.shape) #tuple of integers showing size of array in each dimension
print(a.size) #total number of elements of the array
print(a.ndim) #number of axes/dimensions of the array 
print(a.dtype) #describes the type of elements in the array

#indexing
a=np.array([[1,2],[3,4]])
b=a[0][1]
print("a: ", a)
print("b: ", b)

#slicing
a=np.arange(10)
print(a[2:8:2])
print(a[2:8])
print(a[2])
print(a[2:])

#reshape array without changing its data
a=np.arange(6)
b=a.reshape(2,3)
print(a)
print(b)

#broadcasting which shows how numpy treats arrays during arithmetic operations 
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([1,2,3]) #two dimensions are compatible when they are equal or one of them is 1
print(a.shape)
print(b.shape)
np.array([b,b,b])
c=a+b
print(c)
c=a*b
print(c)
print("a:\n", a)
print("broadcasting:\n", c)
"""

"""
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a.flat[:]) #numpy flatter instance that acts similar to but is not a subclass of Python's built-in iterator object
print(np.transpose(a)) #returns a view of the array with axes transposed
a=np.arange(6).reshape(2,3)
b=np.arange(7,13).reshape(2,3)
print(a)
print(b)
print(np.concatenate((a,b), axis=0)) #joins a sequence of arrays along an existing axis
print(np.concatenate((a,b), axis=1))

a=np.arange(12).reshape(2,2,3)
f=np.transpose(a,(2,1,0))
print(f)
a=np.array([[1,2,3],[4,5,6]])
e=np.append(a,[[7,8,9]],axis=0)
g=np.append(a,[[7,8,9]]) #appends values to the end of an array
b=np.array([3,4])
h=np.array([5,6])
c=np.stack((b,h),0) #joins a sequence of arrays along a new axis with the index as first dimension 
d=np.stack((b,h),1) #joins a sequence of arrays along a new axis with the index as last dimension 
print("c\n", c)
print("d\n", d)
print("e\n", e)
print("g\n", g)

a=np.arange(6).reshape(2,3)
b=np.insert(a,2,[7,8],axis=1)
c=np.insert(a,2,[7,8]) #insert values along the given axis before the given indices
d=np.delete(a,1,axis=1) #returns a new array with sub-arrays along an axis deleted by deleting indices of the specified axis  
e=np.delete(a,1) #returns a new array with sub-arrays along an axis deleted by deleting the specified index
print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)
"""
import numpy.matlib
a=np.matlib.zeros((2,2)) #matrix full of zeros
b=np.matlib.ones((2,2)) #matrix full of ones
c=np.matlib.eye(3) #returns a matrix with ones on the diagonal and zeros eleswhere 
print("a=", a)
print("b=", b)
print("c=", c)
#transfer an array to an matrix
d=np.array([[1,2],[3,4]])
d=np.mat(a)
print(d)
print(type(d))
#transfer a matrix to an array
e=np.mat([[1,2,3],[4,5,6]])
f=e.getA()
print("matrix e=", e)
print(type(e))
print("array f=", f)
print(type(f))
g=np.matlib.rand(3,3) #creates a random matrix
print("g=", g)

h=np.array([[1,0],[0,1]])
i=np.array([[1,1],[2,2]])
print(np.dot(h,i)) #used when both variables are 2-D array
print(a@b) #used when both variables are 2-D array
print(np.multiply(h,i)) #used when either variable is a Scalar/0-D array
print(h*i) #used when either variable is a Scalar/0-D array

a=np.array([1,2,3])
b=np.mat(a) #interpretes input as a matrix
c=np.matrix(a) #interpretes input as a matrix but its not advised
d=np.asmatrix(a) #interpretes input as a matrix
print("array a=", a)
print("matrix b=", b)
print("matrix c=", c)
print("matrix d=", d)
a=np.matrix([[2,0,0],
            [0,1,0],
            [0,0,2]])
b=a.I
print("matrix a=", a)
print("matrix b=", b)
a=np.matrix([[1,2],
             [3,4]])
b=np.linalg.det(a) #find determinant of a matrix
print("matrix a=", a)
print("b=", b)
c=a.sum(axis=0) #finds sum of matrix
d=a.sum(axis=1)
print("c=", c)
e=a.max() #finds maximum value of matrix
f=a.min() #finds minimum value of matrix
print("e=", e)
print("f=", f)

r1=np.random.rand(2,2) #random valuesin a given shape
r2=np.random.rand(2,2)
r3=np.random.randint(0,5) #returns random intergers from low(inclusive) to high(exclusive)
"""
a : If an ndarray, a random sample is generated from its elements. If an int, the randomsample is generated as if a was np.arange(n)
size : Output shape.
replace : boolean, optional; Whether the sample is with or without replacement
p : 1-D array-like, optional; The probabilities associated with each entry in a. If not giventhe sample assumes a uniform distribution over all entries in a.
"""
r4=np.random.choice([1,2,3,4,5], (2,2), p=[0.1, 0, 0.3, 0.6, 0]) 
print("r1=","\n",r1)
print("r2=","\n",r2)
print("r3=","\n",r3)
print("r4=", r4)
a=np.array([1,2,3,4,5])
np.random.shuffle(a) #modify a sequence in place by shuffling its contents 
b=np.random.permutation([1,2,3,4,5]) #randomly permute a sequence or return a permuted range
print("a=", "\n", a)
print("b=", "\n", b)
r5=np.random.normal(0,0.1,5) #draw random samples from a normal/Gaussian distribution
r6=np.random.uniform(0,5,2) #draw random samples from a uniform distribution
r7=np.random.poisson(5,2) #draw random samples from a poisson distribution
print("r5=", "\n",r5)
print("r6=", "\n",r6)
print("r7=", "\n",r7)
a=np.array([0,30,45,60,90])
b=np.sin(a*np.pi/180) #sine element
c=np.cos(a*np.pi/180) #cosine element
print("b=", b)
print("c=", c)
a=np.array([1.0,1.5,2.0,2.55])
b=np.around(a)
c=np.around(a, decimals=1) #evenly round to the given number of decimals specified
d=np.floor(a) #return floor of the input element-wise by returning the value below the elements
e=np.ceil(a) #return ceiling of the input element-wise by returning the value above the elements
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)
a=np.array([1,2,3,4])
b=np.array([4,3,2,1])
c=np.add(a,b)
d=np.subtract(a,b)
e=np.multiply(a,b)
f=np.divide(a,b)
g=np.mod(a,b)
h=np.power(a,b)
i=np.array([[6, 7, 2], [0, 1, 5]])
j=np.amin(a,0) #returns minimum of an array or minimum along an axis
 #k=np.amax(a,1) #returns maximum of an array or maximum along an axis
l=np.median(a) #compute and return the median of the array elements  along the specified axis 
m=np.mean(a) #compute the arithmetic mean along the specified axis 
n=np.sort(a) #return a sorted copy of an array
p=np.sort(a,axis=0) #return a sorted copy of an array along the axis by sortiing according to indices 
print("c=", c)
print("d=", d)
print("e=", e)
print("f=", f)
print("g=", g)
print("h=", h)
print("i=", i)
print("j=", j)
#print("k=", k)
print("l=", l)
print("m=", m)
print("n=", n)
print("p=", p)


