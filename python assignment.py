# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:00:19 2019

@author: win10
"""
"""1:) Write a python program using string functions to validate email ID:
a. It should begin with small/capital characters
b. Should have ‘@’ symbol followed by few characters, 
followed by ‘.’ And followed by another set of characters.
If these conditions are met, print – “the email ID is valid”. 
Else print “Invalid email. Please enter the correct email ID” and ask the user to print another email ID.@@"""

def validate(emailId):
    if(emailId[0].isalpha()):
        if('@' in emailId and '.' in emailId):
            at = emailId.rindex('@')
            dot = emailId.rindex('.')
            if(at<dot and dot-at>2):
                if(dot!= emailId[len(emailId)-1]):
                    return 1
                else:
                    return 0
            else:
                return 0
         else: 
             return 0
    else: 
       return 0
valid =0
while(valid!=1):
    emailId = input("enter the mail")
    valid = validate(emailID)
    if(valid ==0 ):
        print("email Id is valid ")
    else:
        print("email Id is not valid")
            
""" 2:) Write a Python program using string functions to check the password’s strength. The password should
a. Be at least 8 characters long.
b. Contain at least one upper character
c. Contain at least one lower character
d. Contain at least one number.
e. Contain at least one special character.
If the password satisfies all the above condition, print Password is strong"""

def validatePwd(pwd):
    upper=lower=num=sp=0
    if(len(pwd)>=8):
        for ch in pwd:
            if ch.isupper():
                upper =1
            if ch.islower():
                lower =1
            if ch.isnumeric():
                num =1
            if ch.isalnum()!=True:
                sp = 1
        if(upper==1 and lower==1 and num==1 and sp==1):
            return 1
        else:
            return 0
        else:
            return 0

valid = 0
while(valid!=1):
    password = input("enter the password")
    valid = validatePwd(password)
    if(valid == 0):
        print("password is weak,renenter")
    else:
        print("password is strong")

""" 3:) Get the student id, name and marks in Python test 1 and 2 from the student and store 
    it in a dictionary in the following format.
Student = {id:7,"name":"Roy","marks”: [90,97]}
In this example Roy has scored 90 in test 1 and 97 in test 2.
Find the best mark scored by him and display the test in which he has scored the best mark.
Expected Output:
97 in Test 2"""

student = {}
student["ID"]= int(input("id no:"))
student["name"]= input("name:")
mark1 = int(input("mark 1:"))
mark2 = int(input("mark2:"))
l = [mark1, mark2]
student["marks"]=1
if(mark1>mark2):
    print(mark1,"test 1 is higher")
else:
    print(mark2, "test 2 is higher")



""" 4:)Write a Python program to print all unique values in a dictionary.
Example Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}] 
Expected Output : Unique Values: [{'S005', 'S002', 'S007', 'S001', 'S009'}] """

l = [{'V':'S001'},{"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}] 
uniqval = set(val for dic in l for val in dic.values())
print("unique values:",uniqval)

""" 5:) """

from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 













