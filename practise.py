# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 06:02:50 2019

@author: win10
"""
name = input("Enter the name:")
age =  int(input("your age:"))
year = int(input("what year it is :"))
oldyr = str((year - age)+100)
print(name + "will be 100 in " +oldyr)


import datetime
name = input("enter the name")
age = int(input("age:"))
now = datetime.datetime.now()
diff = str(100- int(age))
print(name + "You will be 100 in" +diff+ "years")

n = int(input("enter the number:"))
l = []
for i in range(0,n):
    l.append(int(input("enter the elements in the list")))
    print(l)
    
num = [1,2,3,4,5,78,13,45,67]

print([obj for obj in num if obj <= 5])




















