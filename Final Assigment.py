#!/usr/bin/env python
# coding: utf-8

# ## This Notebook is for all the activities done in IBM Data Science certification

# Before starting to code, insert a Markdown cell above in order to know what´s going on. For example:

# The sum by two numbers is given by:

# In[7]:


print(1+2)


# <a href=https://www.cognitiveclass.ai>Cognitive Class</a>

# | header | header | header |
# | ------ | ------ | ------ |
# | cell | cell | cell |
# | cell | cell | cell |
# | cell | cell | cell |

# <a href=https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>Markdown Cheatsheet</a>

# In[8]:


get_ipython().system('pip install openpyxl')
import pandas as pd
import seaborn as sns

url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-26.xlsx'
df_raw = pd.read_excel(url)

df_raw['Countries and territories'].unique()


# In[10]:


df = df_raw

df = df[df['Countries and territories']=='Mexico']

df = df.sort_values(['Year', 'Month' ,'Day'], ascending=[1, 1, 1])

df['ts'] = pd.to_datetime(df[['Year', 'Month' ,'Day']])


# In[12]:


chart = sns.lineplot(x='ts', y='Cases', data=df, hue='Countries and territories')
chart.set_xticklabels(df['ts'],rotation=45)


# In[ ]:




