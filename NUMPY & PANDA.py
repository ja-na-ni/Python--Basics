# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:39:02 2019

@author: win10
"""

@@@ NUMPY & PANDA@@@@
import pandas as pd
s1 = pd.Series(["python","java"])
s2 = pd.Series(["lists","arrays"])
s1[0]

s3 = pd.Series([1,2,3])
s3 = s3+10
x = pd.DataFrame([s1,s2]) #multidimensional array
d = {'a': 1,'b':2,'c':3,'d':4} #dictionary
s1 = pd.Series(d) #add dictionary in single dimensional arry
s1['a'] #call the value using the key
df1 = pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})
dict1 = {'a' :1,'b':2,'c':3,'d':4}
dict2 = {'a':5,'b':6,'c':7,'d':8,'e':9}
df = pd.DataFrame([dict1,dict2]) #''nan'' - is the null value in python

df = pd.read_csv('employees.csv')
df.info()
df.head() #prints first 5 rows ..if we want more than that we have to specify the number 
df.head(10)
df.describe()#to get basic statistical information about quantitative data
df['First Name'][0]

$$$ INTERGER LOCATION - ILOC$$$
df.iloc[:,0] #entire first row
df.iloc[0:6,0] #first 5 rows of first column
df.iloc[0,0]#frst row first column
df.iloc[4:7,1:4]

$$$ LOCATION- LOC $$$
df.loc[:5,"Gender"] #first 5 rows from column gender
df.loc[0:2,"First Name"]


res =df[df['Salary']>50000]

import numpy as np
np.mean(res['Salary'])

res = res.dropna()

r = res.groupby('Gender')
r['Salary'].agg(np.mean)
r.get_group('Male')['Salary'].agg(np.mean)



1.

import pandas as pd
mv = pd.read_csv('movies_metadata.csv',error_bad_lines=False,encoding='ISO-8859-1')

mv = pd.read_csv('movies_metadata.csv',encoding='latin-1')
2.
mv['release_date'] #reads ony that column
mv['release_date'][0] #columns first element
type(mv['release_date'][0]) #type of string
mv['release_date']= pd.to_datetime(mv['release_date']) #typecasting
new = mv[mv['release_date']>pd.to_datetime('1995-10-01')]
res =mv[mv['release_date']>'1995-01-01']
3.
aa = mv.sort_values(["runtime"], axis =0 ,ascending= False)
4.
df1 = mv[(mv['revenue']>2000000)&(mv['budget']<1000000)]
5.
type(mv['genres'][0])
s1 = 'sad'
s2= 'pandas'
s2.find(s1)
hv = 'Comedy' in mv['genres']
jj = mv['genres'].str.find('Comedy') #"find" function gives the position where the match is occuring

l =[]
for i in range(len(mv)):
    if ('Comedy' in mv['genres'][i]):
        l.append(i)
        
l = []
for i in range(len(mv)):
    if(mv['genres'][i].find('Comedy')!= -1):
        l.append(i)
        
comedy = mv.iloc[l]
comedy= comedy.reset_index(drop=True) #to reset the index 


6.
pop = mv.nlargest(15, ['popularity']) #6th question
7.
df2 = mv[(mv['tagline'].isnull())]
8.
df3 = mv[mv['original_language'] == 'en']

1. read football.csv
df = pd.read_csv('football.csv')

2.find the num of teams participated in footbal matches
len(df.Team)
res = []
res = df['Team'][:]
res.count()

3. sort the teams by the number of red cards they recieved nd print
df = df.sort_values(by ='Red Cards')
df

4.calculate the mean red cards of all teams
import numpy as np
re = df['Red Cards']
np.mean(df['Red Cards'])

5. minimum & maximum number of goals
df['Goals'].min()
df['Goals'].max()
np.min(df['Goals'])
np.max(df['Goals'])

6.what is the mean shooting accuracy based on the number of goals
type(df['Shooting Accuracy'][0])
df['Shooting Accuracy'][0].replace("%","")

for i in range(len(df)):
    df['Shooting Accuracy'][i]=float(df['Shooting Accuracy'][i].rstrip('%'))
np.mean(df['Shooting Accuracy'])

7.what is the total number shots based on number of players used














