"""
import collections as c
print(isinstance([], c.iter))
print(isinstance('abc', c.iter))
print(isinstance(100, c.iter))
"""
import os

print("process id: ", os.getpid())
print("parent process id: ", os.getppid())
cwd=os.getcwd()
print("current directory: ", cwd)
os.chdir("C:/")
print("new directory: ", os.getcwd())
print("all the files: ", os.listdir(cwd))


import sys
"""
for i in range(100):
    print(i)
    if i==5:
        sys.exit(0)
"""
sys.path #list of strings that specifies the search path for modules
sys.platform