#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv(r'C:\Users\BHOOMI\Downloads\weatherHistory.csv')


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.shape


# In[7]:


df


# In[8]:


df.index


# In[9]:


df.columns


# In[159]:


df.value_counts()


# In[157]:


df.dtypes


# In[158]:


df.count()


# In[160]:


df.info()


# In[161]:


df.head(10)


# # find all the unique wine speed values in the data

# In[162]:


df['Wind Speed (km/h)'].nunique()


# In[163]:


df.nunique()


# In[12]:


df['Precip Type'].unique()


# # find the number of times when the weather is exaclty clear

# In[165]:


df.head(2)


# In[166]:


df.Summary.value_counts()


# In[167]:


df[df.Summary  == 'Clear']


# In[168]:


df.groupby("Summary").get_group('Clear')


# # find the number of times whenthe wind speed was exactly 4km/hr

# In[169]:


df.head(2)


# In[170]:


df[df['Wind Speed (km/h)'] == 4]


# In[171]:


df


# In[172]:


df[df['Wind Speed (km/h)'] == 4]


# # find null values

# In[173]:


df.isnull().sum()


# In[174]:


df[df['Precip Type'].isnull()]


# In[175]:


df.notnull().head()


# In[176]:


df.shape


# In[177]:


df.isnull().sum()


# In[178]:


df.dropna(how = 'any').shape


# In[179]:


df.dropna(how = 'all').shape


# In[180]:


df.columns


# In[181]:


df.dropna(subset =['Precip Type'],how='all').shape


# In[182]:


df.dropna()


# In[183]:


df.notnull().sum()


# # rename the column weather of dataframe to weather condition

# In[193]:


df.rename(columns = {'Pressure (millibars)'  : 'Pressure'}, inplace = True)


# In[194]:


df.head()


# # what is the mean visibility

# In[191]:


df.Visibility_km.mean()


# In[ ]:





# # what is the standard deviation of pressure in this data

# In[195]:


df.Pressure.std()


# # what is the variance of relative humidity in this data

# In[196]:


df['Humidity'].var()


# # find all instance when snow was recorded

# In[ ]:





# In[197]:


df['Weather'].value_counts()


# In[ ]:





# In[199]:


df[df['Weather'] == 'snow']


# # # # find all instances when wind speed is above 24 and visibility is 25

# In[201]:


df.head(2)


# In[204]:


df[(df['Wind Speed (km/h)'] > 24) & (df['Visibility_km'] == 25)]


# # what isthemean value of each column against each weather condition

# In[205]:


df.groupby('Weather').mean()


# # what is the minimum value of each column against each wheather condition

# In[206]:


df.groupby('Weather').min()


# In[207]:


df.groupby('Weather').max()


# # show all the records where weather condition is fog

# In[217]:


df[df['Weather'] == 'rain']


# In[212]:


df.tail(10)


# # find all instances when wheather is clear or visibility is above 40

# In[219]:


df[(df['Weather'] =='Clear') | (df['Visibility_km'] > 10)].tail(50)


# # find all instances when:

# In[220]:


df[(df['Weather'] =='Clear') & (df['Humidity'] >0.50)| (df['Visibility_km'] >10)]


# In[ ]:




