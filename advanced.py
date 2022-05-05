import sys
from typing import Any
sys.version

#import RE module
import re
print(re.match('www', 'www.huawei.com').span()) #match from start of text
print(re.match('com', 'www.huawei.com')) #it cannot match from the middle thus prints none but instead use search
print(re.search('com', 'www.huawei.com').span())

line = "cats are smarter than fish"
searchObj= re.search(r'(.*) are smarter than (.*)', line)
if searchObj:
    print('searchObj.group() :', searchObj.group())
    print('searchObj.group(1) :', searchObj.group(1))
    print('searchObj.group(2) :', searchObj.group(2))

else:
    print('nothing found!')

#re.compile(pattern).search(text) is same as re.search(pattern, text) 
pattern= re.compile(r'\d+') #match at least one digit
n=pattern.match('one12twothreee34four') #match from start, no match 
print(n)
m=pattern.search('one12twoothree34four')
print(m)
print(m.group())

phone="2020-0101-000 #this is a phone number"
num=re.sub(r'#.*', '', phone) #removes the '#' sign and everything after it
print("phone number: ", num)
num=re.sub(r'\D', '', phone) #remove everything that is not a digit
print("phone number: ", num)

#find all numbers in text
text='tomorrow is 2022/2/31, today is 2020/2/30'
num1=re.findall(r'\d+', text)
num2=re.findall(r'[0-9]{2,5}', text)
print(num1)
print(num2)
#find all alphabets 
s=re.findall(r'[a-zA-z]+', text)
print(s)
s=re.findall(r'[A-Za-z0-9]+', text)
print(s)
#find email address
email="email address is: claus@gmail.com"
t=re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.com', email)
print(t)
#find url
site="huawei website: https://huawei.com"
u=re.findall(r'https?://.*', site)
print(u)

html='aa<div>test1</div>bb<div>test2</div>cc'
res1=re.search('<div.*</div>', html) #find every div tag
res2=re.search('<div>.*?</div>', html) #find first div tag
print(res1.group())
print(res2.group())

#open file called 'text.txt'
"""
f=open("text.txt", 'w',encoding='utf8') #opens the text.txt file
inputs=input("input: ")
f.write(inputs)
f.close()

f=open('text.txt', 'r')
print(f.read(6)) #read 6 character from the current position(default is 0) 
print(f.read()) #read from current position to the end
f.close()
f=open("text.txt", 'a')
f.write(" I append more content!") #to add content
f.close()
f=open("text.txt", 'r')
print(f.read())
f.close()
#'with' is used to open file
with open('text1.txt','w') as f:
    f.write("Kami is cool\nthis is a pen\nI love you")
#to read file
with open("text1.txt", 'r') as f:
    print(f.read())
#open file
with open('text1.txt', 'r') as f:
    line=f.readline()
    print('read one line: %s' % (line))
    lines=f.readlines()
    print(lines)
"""

#catch errors or exceptions with try-except statement
"""
a=input()
try:
    b=[i for i in range(int(a))]
    print(b[4]/0)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("value error")
except IndexError:
    print("list index out of range")
finally:
    print("Kami is cool")
"""

#custom exception
class MyError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

#to throw an exception
# raise MyError("my exception")

#to assert a statement
"""
def func(a,b):
    assert a==b #if a is not equal to b, pyhton will throw an exception
func(1,2)
"""

# in Generators, use 'isinstance' function to check if an object is iterable
"""
import collections as c
print(isinstance([], c.iter))
print(isinstance('abc', c.iter))
print(isinstance(100, c.iter))
"""
l=[1,2,3,4,5]
l_iter=iter(l)
print(type(l_iter))
print(next(l_iter))
print(next(l_iter))

#yield is used to construct a generator for fibonacci sequence 
def fib(n):
    current=0
    num3, num4=0,1
    while current<n:
        num=num3
        num3, num4=num4, num3+num4
        current +=1
        yield num
    yield "done"

g=fib(5)

for x in g:
    print(x)

g=( x*2 for x in range(5))

for x in g:
    print(x)

def decorate(func):
    def decorated():
        print("I got decorated")
        func()
    return decorated

@decorate
def plain():
    print("I am plain")

plain()
#sys.exit([n]) is used to exit the program
import sys

for i in range(100):
    print(i)
    if i==5:
        sys.exit(0)

sys.path #list of strings that specifies the search path for modules
sys.platform #checks system platform

import os

print("process id: ", os.getpid())
print("parent process id: ", os.getppid())
cwd=os.getcwd()
print("current directory: ", cwd)
os.chdir("C:/")
print("new directory: ", os.getcwd())
print("all the files: ", os.listdir(cwd))



