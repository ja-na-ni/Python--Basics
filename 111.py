# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:51:16 2019

@author: win10
"""

i = int(input())
j = int(input())
k = float(input())
l = float(input())
m = input()
n = input()
print(i+j)
print(k+l)
print(m+n)

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

#n = int(input().strip())
#for i in range(1,11):
 #   print('{0} * {1} = {2}'.format(n,i, n*1))
    
#string = 'android is awesome'
#print(string.strip('an'))

mc = float(input())
tpp = int(input())
tp = int(input())
tip = mc* (tpp/100)
tp = mc * (tp/100)
totalcost = mc+tip+tp
print(round(totalcost))

n = int(input())
if (n%2 == 1):
    print("Weird")
else:
    if (n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Not Weird")
    else:
        print("Weird")
        

n = int(input().strip())
for i in range(1,11):
    print(n, 'x', i, '=', n*i)
    
choices = ['pizza', 'pasta', 'salad', 'nachos']
list(enumerate(choices))
##[(0, 'pizza'), (1, 'pasta'), (2, 'salad'), (3, 'nachos')]

s = int(input())
for i in range(0,s):
    string = input()    
evel = []
oddl = []
for it,c in enumerate(string):
    if (it%2 ==0):
        evel.append(c)
    else:
        oddl.append(c)
print (''.join(evel),''.join(oddl))
    
ch = input()
wd = ch.lower()
first = wd[0]
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(ch,'is a vowel')
else:
    print(ch,'is a consonant')
    
class MathUtils:
#@staticmethod
    def average(a, b):
        return a + b/ 2
print(MathUtils.average(2, 1))

def is_palindrome(word):
    return word[::-1]==word
print(is_palindrome('Deleveled'))

#False since there is D in the begining of the word

print(5 * 2 // 3) #3
print(2 ** 3 ** 2) #512

x=25
y=21
z=22
if(x>y<z):
    print("True")
else:
    print("False")
#ANS : True

def fun(x):
    if(x>0):
        x=x-1
fun(x)
print(x, end="\t")
x=x-1
fun(x)
a=4
fun(a)




















    

























