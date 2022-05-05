print('hello world')
print("hello world")
#triple quotes allows string to span multiple lines 
print(""" hello 
world""")

# comment for one line
"""
comment for multiple lines or multiline strings and docstrings
""" 

a=10
b=2
#switching values
a,b=b,a
print(a)
print(b)

def func1():
    a=1
    b=1
    print(a)
    print(b)
"""
s= input("input:")#reading from standard input
print(s)#writing to standard output

help(print)
#print(...)

a=1
id(a)#id function returns the “identity” of an object
print(id(a))
type(a)#return the type of an object
print(type(a))
del(a)#deletes an object
len("kami") #returns number of items of an object
print(len("kami"))
"""

s="python\""  #escape sequence to insert characters that are illegal in a string
print(s)
t="py\nthon"  #escape sequence to start a new line
print(t)

b=r"C:\Desktop\software"  #r or R is used to ignore escape sequences(\) in strings to make it a raw string
print(b)

s="python is good"
print(s[0]) #first character
print(s[-1]) #last character
print(s[0:4:2]) #slicing operator(:) is used to index a range of charcters
print(s.split (" "))
print(s.replace('py' ,'kami'))
print(s.lower())
print(s.upper())
print("=".join(['python', 'is', 'cool'])) #joins the string by the value inside the quotes
print("My name is %s, age is %d" %("Polo", 45))

a="hello"
b=" world"
c=3
print(a+b) #concatenates strings
print(a*c) #repeats string for a given number of times

pets=['cat', 'dog', 'bird']
pets.append('fish') #add an item to list
print(pets)
pets.remove('dog') #delete one or more items from list
print(pets)
pets.insert(0,'seal') #insert item at the specified index
print(pets)
print(pets.pop(0)) #removes and returns the removed item
print(pets) #returns remaining items

for i, x in enumerate(pets): #obtains an index list by showing index of item along with item
    print(i, x)
d=[40, 50, 20, 10,30]
d.sort() #sort elements in a given list
print(d)
d.reverse() #reverses order of items in a list 
print(d)
d=[i*2 for i in pets] #repeats objects in a list by multiplying by the number specified
print(d)

l=[0, 1, 2, 3, 4,5]
print(l[::2]) 
"""slicing returns a slice object that can be used to slice strings, object where 
l[start:end:step]
start where slicing starts
end where slicing ends
step which determines increment between each index for slicing
"""
print(l[1:4:2])

t=(1, [a,b], "kami") #tuple which stores heterogeneous list
print(t)
print(type(t))
 # t[1]=0 is wrong since tuple does not support item assignment

#creating a dictionary in 3 ways:
x={'food':'spam', 'quantity':4, 'color':'blue'}
x2=dict(food='spam', quantity=4, color='pink')
x3=dict([('food', 'spam'), ('quantity', 4), ('color', 'pink')])
print(x)
print(x2)
print(x3)
#to extract values in a dictionary
print(x['food']) 
print(x.get('food'))
print(x.get('a')) #if the value is not found, it prints none
print(x.get('a', 'cannot find a')) #it will print the last value
print(x.keys()) #extract all keys
print(x.values()) #extract all keys
print(x.items()) #extract keys and their value pairs
x['space']='large' #insert an item to dictionary
print(x)
x['space']='small' #change an item in a dictionary
print(x)

#2 ways of creating a set
example_set={'kami', 'teacher'}
example_set2=set(['kami', 'teacher'])
print(example_set)
print(example_set2)
print('data' in example_set) #'in' keyword is used to check a value is present in a specified set 
print('kami' in example_set)
example_set.add('chill') #add an element to a set
print(example_set)
example_set.remove('teacher') #removes an element from a set
print(example_set)
list1=[1,2,1,2,4,5]
print(list(set(list1))) #a set has no duplicate elements

example_set=frozenset(example_set)
 # example_set.add('cat') is wrong because 'frozenset' keyword ensures it is an unchangeable set
example_set2.add('cat')
print(example_set)
print(example_set2)

#deep copy and shallow copy has not been understood, revisit later

#assignment operators
a=5
a+=1
print("a+1= ", a)
a-=1
print("a-= ", a)
a*=2
print("a*2= ", a)
a/=2
print("a/2= ", a)

#comparison operators
print(1>=2)
print(1<=2)
print(1!=2)
print(1==2)

#membership operators
a=[1,2,3]
print(1 in a)
print(4 in a)
#identity operators
a=[1,3]
b=a
c=a.copy()
print(a is b)
print(a is c)
print(a == b == c)
"""
marks=input("Enter marks") #input is used as a string here
type(marks)
marks=float(marks) #convert string to a float number
if 100>=marks>=90:
    print("A")
elif 90>marks>=80:
    print("B")
elif 80>marks>=60:
    print("C")
elif 60>marks>=0:
    print("F")
else:
    print("Incorrect!")

"""
if 0:
    print("false")
if 1:
    print("true")
if "kami" :
    print("kami")
if None:
    print("None") 

i=0
while i<9:
    i+=1
    if i==3:
        print("skip this loop")
        continue #skips this part of code of the loop
    print(i)
else:
    print("loop ends")

i=0
while i<9:
    i+=1
    if i==5:
        print("terminate loop") #ends loop without executing the rest of code
        break
    print(i)
else:
    print("loop ends")

times= ["first", "second", "third"]
for i in times:
    print(i)
else:
    print("end loop")

"""
#multiplication table
for i in range(1,10): #outer loop
    for j in range(1,i+1): #inner loop
        print("%dx%d=%-2d"%(j,i,j*i), end=" ") #string formatting
        print()
"""
#default arguments
def func():
    print("hello world")
    func()

def f(a=8, b=2, *args, **kwargs):
    print("a: %d" %(a))
    print("b: %d" %(b))
    print("args:",args)
    for key, value in kwargs.items():
        print("%s is %s" %(key, value))
    print()
f()

#positional arguments
f(0,4)

#keyword arguments
f(b=4, a=0)

#arbitrary positional arguments
def f(a=8, b=2, *args, **kwargs):
    print("a: %d" %(a))
    print("b: %d" %(b))
    print("args:",args)
    for key, value in kwargs.items():
        print("%s is %s" %(key, value))
    print()
f(1,2,3,4,5)
#arbitrary keyword arguments
f(cat='animal', dog='animal', cheese='food')

#single return value
def func(a,b):
    return a+b
a=func(2,3)
print("a:", a)

#multiple return value
def func ():
    return 1,2,3
a=func()
print("a:",a)

#fibonacci sequenceclea
def fibs(num):
    result=[0,1]
    for i in range(2,num):
        a=result[i-1]+result[i-2]
        result.append(a)
    return result
fibs(5)
