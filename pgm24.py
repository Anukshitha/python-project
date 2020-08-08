#Random Password Generator

from random import *
print("Random Password Generator")
print("You can create a random password in this software")

a=input("Enter your name: ")
b=input("Enter your birth date: ")
c=input("Enter your birth month: ")
d=input("Enter your birth year: ")
e=input("Enter the name of your favourtie sports person: ")

lst=[]
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
lst.append(e)
shuffle(lst)
lst2=[]

for i in lst:
    for j in i:
        lst2.append(j)
var=""

shuffle(lst)


for i in lst2:
    print(i)
    print("the factorial of",lst2)

    

