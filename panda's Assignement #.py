# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 09:12:37 2019

@author: win10
"""
1.

import pandas as pd
mv = pd.read_csv('movies_metadata.csv',error_bad_lines=False,encoding='ISO-8859-1')
2.
mv['release_date']
res =mv[mv['release_date']>'1995-01-01']
3.
aa = mv.sort_values(["runtime"], axis =0 ,ascending= False)
4.
df1 = mv[(mv['revenue']>2000000)&(mv['budget']<1000000)]
6.
pop = mv.nlargest(15, ['popularity']) #6th question
7.
df2 = mv[(mv['tagline'].isnull())]
8.
df3 = mv[mv['original_language'] == 'en']