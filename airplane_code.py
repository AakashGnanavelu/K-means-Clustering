# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:00:09 2021

@author: Aakash
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from sklearn.cluster import	KMeans

X = np.random.uniform(0,1,100)
Y = np.random.uniform(0,1,100)
df_xy = pd.DataFrame(columns=["X","Y"])
df_xy.X = X
df_xy.Y = Y

df_xy.plot(x="X", y="Y",kind="scatter")

model1 = KMeans(n_clusters=4).fit(df_xy)

df_xy.plot(x="X", y = "Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)

data = pd.read_excel(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Full Data Science\K- Means Clustering\Assginment\air_data.xlsx')
data.describe()

data = data.drop('ID#',axis = 1)

def norm_func(i):
    x = (i-i.min())	/ (i.max() - i.min())
    return (x)

data_norm = norm_func(data.loc[:, :])

TWSS = []
k = list(range(2,10))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(data_norm)
    TWSS.append(kmeans.inertia_)
    
TWSS

plt.plot(k,TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

model = KMeans(n_clusters=3)
model.fit(data_norm)

model.labels_ 
mb = pd.Series(model.labels_) 
data['cluster'] = mb

data.head()
data_norm.head()

tab = data.iloc[:, :].groupby(data.cluster).mean()

data.to_csv("k-means clustering airplanes output.csv",encoding="utf-8")

import os
os.getcwd()
