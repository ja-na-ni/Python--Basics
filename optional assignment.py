# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:28:40 2019

@author: win10
"""

1.)

n = input("enter the string")
for i in n:
    print(i)
    
2.)
n = input()
count = 0
for i in n:
    count = count + 1
    
print(count)

3.)
def swapnum(a,b):
    x = b[:1] + a[1:]
    y = a[:1] + b[1:]
    
    return x + ' ' + y
print(swapnum('abc','xyz'))

4.)
def longest(wordlist):
    wordlen = []
    for n in wordlist:
        wordlen.append((len(n), n))
    wordlen.sort()
    return wordlen[-1][1]

print(longest(["hi", "hello world", "good"]))

5;)
def upp(str1):
    uppe = 0
    for i in str1[:4]: 
3        if i.upper() == i:
            uppe += 1
    if uppe >= 2:
        return str1.upper()
    else:
        return str1.lower()
    return str1

print(upp('heLLo'))
print(upp('heLlo'))
