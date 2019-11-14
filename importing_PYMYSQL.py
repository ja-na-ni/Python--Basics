# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 01:20:56 2019

@author: win10
"""

import pymysql as pms
db = pms.connect('localhost','root','Pillayar@8','sample')
import pandas as pd
query = "select * from employee;"
df = pd.read_sql(query,con = db)
df = pd.read_sql(' SELECT * FROM employee',con = db)
df1 = pd.read_sql(' SELECT * FROM department',con = db)
df2 = pd.read_sql(' SELECT * FROM project',con = db)
df4 = pd.read_sql(' SELECT * FROM projact',con = db)
df1 = pd.DataFrame({'employee':[1,2,3,4],'group':['a','b','b','hr']})
df3 = pd.merge(df2,df4, how= 'right')
dr = pd.DataFrame({'name':['a','b','c'],'food':['beans','bread','chocolate']})
dr1 = pd.DataFrame({'name':['c','d'],'drink':['milk','juice']})
dr2 = pd.merge(dr,dr1,how = 'right')
dr3 = pd.merge(dr,dr1,how = 'left')
cursor = db.cursor()
query1 = "alter table employee modify firstnme varchar(50)"
cursor.execute(query1)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings    # We want to suppress warnings
import os
IBM_hrdata = pd.read_csv('D:\statistics\HRDATA.csv')
IBM_hrdata.info()
IBM_hrdata.head()
# to find categorical data
Nunique = IBM_hrdata.nunique()
Nunique = Nunique.sort_values()
Nunique

sns.set_color_codes()
ax= sns.distplot(IBM_hrdata['Age'],color = 'y')
plt.show() 

sns.distplot(IBM_hrdata['TotalWorkingYears'],color = 'g')
plt.show() 

sns.distplot(IBM_hrdata['YearsAtCompany'],color = 'y')
plt.show() 


sns.countplot(x=IBM_hrdata['Age'], hue="Attrition", data=IBM_hrdata,color = 'g')
plt.xticks( rotation=90)
plt.show()

data_df1=pd.DataFrame(IBM_hrdata[['MaritalStatus','PerformanceRating','JobLevel',
                                  'RelationshipSatisfaction','OverTime','Department',
                                  'EnvironmentSatisfaction','JobSatisfaction','WorkLifeBalance']])

for i, col in enumerate(data_df1.columns):
	sns.countplot(x=col, hue='Attrition',data=IBM_hrdata)	
	plt.figure(i)

sns.boxplot(IBM_hrdata['JobRole'], IBM_hrdata['JobSatisfaction'])
plt.xticks( rotation=90)
plt.show()
















