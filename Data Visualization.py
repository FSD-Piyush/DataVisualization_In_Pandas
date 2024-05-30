#!/usr/bin/env python
# coding: utf-8

# # Pandas Visualization

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv(r"C:\Users\PIYUSH\Downloads\Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[43]:


df.plot()


# In[8]:


df.plot(kind = 'line')


# In[9]:


df.plot(kind = 'line', subplots = True)


# In[11]:


df.plot(kind = 'line', title = 'Ice Cream Ratings')


# In[12]:


df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[15]:


df.plot(kind='bar')


# In[16]:


df.plot(kind='bar', stacked = True)


# In[17]:


df['Flavor Rating'].plot(kind='bar', stacked = True)


# In[18]:


df.plot.barh(stacked = True)


# In[20]:


df.plot.barh()


# In[27]:


df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'Red')


# In[29]:


df.plot.hist()


# In[31]:


df.plot.hist(bins = 100)


# In[32]:


df.plot.hist(bins = 10)


# In[33]:


df.plot.hist(bins = 20)


# In[34]:


df.boxplot()


# In[35]:


df.plot.area()


# In[36]:


df.plot.area(figsize = (10,5))


# In[38]:


df.plot.pie(y='Flavor Rating')


# In[40]:


df.plot.pie(y='Flavor Rating', figsize = (10,10))


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




