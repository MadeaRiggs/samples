from cProfile import label
from re import S, X
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import alphas


# matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
# plot y versus x as lines and/or markers. *args inclues data, color, format...et
x=np.arange(0, 3 * np.pi, 0.1)
y=np.sin(x)
plt.plot(x, y)
plt.show() #show graph
print(len(x))
print(plt.style.available) #check available styles
plt.style.use("seaborn-darkgrid") #choose style

#combining multiple graphs
"""
matplotlib.pyplot.subplot(* args，** kwargs)
add a subplot to the current figure.*args
*args can be three integers (nrows, ncols, index),
 or a 3-digit integer. The digits are interpreted as if given separately as thre
x=np.arange(0,3 *np.pi, 0.1)
"""


x=np.arange(0, 3 * np.pi, 0.1)
y=np.sin(x)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.subplot(2, 1, 1) #first subplot
plt.plot(x, y_sin) #plot the first subplot
plt.title('Sine') #title for first subplot
plt.subplot(2, 1, 2) #second subplot
plt.plot(x, y_cos) #plot second subplot
plt.title('Cosine') #title for second subplot
plt.show()

plt.style.use("seaborn-dark")
plt.figure(figsize=(8,6), dpi=80) # create a 8x6 (inches) figure, dpi means the resolution of the figure (dpi=80, 8
plt.savefig("exercise.png",dpi=72) #saves figure
#generate data
X=np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S=np.cos(X), np.sin(X)
plt.plot(X, C, color="blue",linewidth=1.0,label="Blue",linestyle="--") #draw a blue curve with customized format
plt.plot(X, S, color="green",linewidth=1.0,label="Green",linestyle="-.") #draw a green curve with customized format
plt.legend() #place a legend on the axes
plt.xlim(-4.0, 4.0) #set the scale of the x-axis
plt.xticks(np.linspace(-4,4,9, endpoint=True)) #set the current tick locations on x-axis
plt.ylim(-1.0,1.0) #set the scale of the y-axis
plt.yticks(np.linspace(-1,1,5, endpoint=True)) #set the current tick locations on y-axis
plt.show()
plt.figure(dpi=72)
plt.plot(X, C, color="blue", linewidth=3.5, linestyle="--")
plt.plot(X,S, color="red", linewidth=2.5, linestyle="-")
plt.show()

#scatter plot
a=np.random.randint(0,20,15)
b=np.random.randint(0,20,15)
print(a)
print(b)
# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=No
# A scatter plot of y vs. x with varying marker size and/or color.
plt.scatter(a, b, c='red', s=1000, marker='x') #plot a scatter
plt.show()

#bar plot
level=['Excellent', 'Good', 'Fair']
x=range(len(level)) #x-axis
y=[1,3,2] #y-axis
plt.figure(dpi=100) #create figure
# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', dat
plt.bar(x, y, width=0.5, color=['b', 'r', 'g']) #plot figure
plt.xticks(x, level)
#add grid
plt.grid(linestyle="--", alpha=1)
plt.show()

#histogram plot
t=np.random.randint(0,30,90)
print(t)
plt.figure(dpi=100)
group_num=14
plt.hist(t, facecolor="red", edgecolor="green", bins=group_num, alpha=0.5) 
plt.xticks(range(min(t),max(t))[::2])
plt.grid(linestyle="--", alpha=0.5)
plt.show()







