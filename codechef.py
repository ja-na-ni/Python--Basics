# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:20:20 2019

@author: win10
"""

n = int(input())
re=[]
for i in range(n):
    x,y,z = map(int,input().split())
    if(z%2 == 0):
        x *=z
        y*=z
    else:
        if((z//2)!=0):
            y *= (z//2)*2
            x*=(z//2)*2
            x*=2
        else:
            x*=2
    re.append(max(x,y)//min(x,y))

for i in re:
    print(i)

n = int(input())
for i in range(n):
    x,y = list(map(int,input().split()))
    s = input()
    chef = sum([1 for ch in s if ch >= 'A'and ch<= 'Z'])<= y
    brother = sum([1 for ch in s if ch >= 'a' and ch<='z'])<= y
    if (chef and brother):
        print ("both")
    elif(chef):
        print ("chef")
    elif (brother):
        print ("brother")
    else:
        print ("none")

n = int(input())
for i in range(n):
    x = int(input("number of test cases"))
    for j in range(x):
        x = list(map(int,input().split()))
        y = []
        y = sorted(x)
        x.append(y)
        print(y)
        print(y[0]+y[1])

y = []
n = int(input("Number of values to be present in the list:"))
ele = list(map(int,input("enter the number to be appended to the list:").strip().split()))[:n]
y = sorted(ele)
ele.append(y)
print(y[-2])
    
n = int(input())
re = []
for i in range(n):
    x,y = map(int,input().split())
    z = []
    for j in range(0,x):
        a = list(map(int,input().split()))
        z = sorted(a)
        a.append(y)
        if(y == 1):
            del(z[0])
            del(z[-1])
            avg = sum(z)/len(z)
            re.append("{:.6f}".format(avg))
            break
        elif(y == 0):
            avg = sum(z)/len(z)
            re.append("{:.6f}".format(avg))
            break
        else:
            break 
for j in re:
    print (j)
        
        
        
        



























