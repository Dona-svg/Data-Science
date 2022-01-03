#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
iris=pd.read_csv("iris.csv")
print("shape:",iris.shape)
print()


# In[5]:


print("First five rows")
print(iris.head())
print()
print("Last five rows")
print(iris.tail())
print()


# In[6]:


print("Size:",iris.size)
print()


# In[14]:


print("no of samples available for each type") 
print(iris["variety"].value_counts())
print()


# In[15]:


print(iris.describe())


# In[21]:


sns.pairplot(iris, hue="variety" ,kind="hist")
print(" ")
sns.pairplot(iris, hue="variety", kind="scatter")
print(" ")

sns.pairplot(iris, hue="variety",kind="kde")
print(" ")
sns.pairplot(iris, hue="variety",kind="reg")
print(" ")


# In[22]:


sns.displot( data =iris)


# In[23]:


sns.histplot(data=iris)


# In[24]:


sns.relplot(data=iris)


# In[ ]:




