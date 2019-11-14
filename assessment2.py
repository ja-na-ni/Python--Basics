# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:32:35 2019

@author: win10
"""

ASSESSMENT 2:
 
1:
    
n = int(input("Enter the number"))
def palindrome(n):
    for i in range(0,n):
        res = n
        rev = 0
        while(n>0):
            a = n%10
            rev = (rev*10)+ a
            n = n//10
        print(rev)
        if(res == rev):
            print(rev,"is a palindrome")
        else:
            print(rev,"is not a palindrome")
#palindrome(n)
    
2.)

a = input("first string :")
b = input("second string :")
def anag(a,b):
    n1 = len(a)
    n2 = len(b)
    if n1 != n2:
        return 0
    a = sorted(a)
    b = sorted(b)
    for i in range(0,n1):
        if a[i] != b[i]:
            return 0
    return 1
if anag(a,b):
    print("the strings are anagram")
else:
    print("the strings are not anagram")
    
3.) 
    
y = input()
z = len(y)
for i in range(z):
    c = ord(y[i])
    c = c+3
    print(chr(c))
4.)
x = [23,34,45,12,2,7,15,5,17,19]
new_list = []
if x > 1:
    for i in x:
        if (x % i) == 0:
            x = x//i
            break
        else:
            new_list.append(x)
print(new_list)
        
sympPy library --"isprime" function

abs(0-2) #absolute fucntion













