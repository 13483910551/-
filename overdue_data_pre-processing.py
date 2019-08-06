
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib as mpt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing  import OneHotEncoder,LabelEncoder
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


f=open('C:Desktop/data.csv')
data=pd.read_csv(f)


# In[3]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
#y_train=data.status
#data.drop(['status'],axis=1,inplace=True)
data.head(10)


# In[4]:


#去掉重复的
data_cols=data.columns.values.tolist()
for col in data_cols:
    if data[col].value_counts().count()==1 :
        data.drop(col,axis=1,inplace=True)
data.drop(['id_name','trade_no','student_feature','Unnamed: 0'],axis=1,inplace=True)
           


# In[5]:


reg_preference_for_trad_mapping={
    '一线城市':1,
    '二线城市':2,
    '三线城市':3,
    '境外':4,
    '其他城市':5
}
data.reg_preference_for_trad=data.reg_preference_for_trad.map(reg_preference_for_trad_mapping)
data.reg_preference_for_trad.fillna(stats.mode(data.reg_preference_for_trad)[0][0],inplace=True)
data.reg_preference_for_trad.astype('int64')


# In[9]:


data.latest_query_time=pd.to_datetime(data.latest_query_time)
data['latest_query_time_year']=data.latest_query_time.dt.year
data['latest_query_time_month']=data.latest_query_time.dt.month
data['latest_query_time_day']=data.latest_query_time.dt.day
data.loans_latest_time=pd.to_datetime(data.loans_latest_time)
data['loans_latest_time_year']=data.loans_latest_time.dt.year
data['loans_latest_time_month']=data.loans_latest_time.dt.month
data['loans_latest_time_day']=data.loans_latest_time.dt.day
data.drop(['latest_query_time','loans_latest_time'],axis=1,inplace=True)


# In[10]:


data_cols=data.columns.values.tolist()
li=[]
for col in data_cols:
    if data[col].dtype=='object'and  data[col].isnull().any()==True:
        li.append(col)
    if data[col].isnull().any()==True:
        data[col].fillna(data[col].mode,inplace=True)     


# In[11]:


data_cols2=data.columns.values.tolist()
li2=[]
for col in data_cols2:
    if data[col].dtype=='int64'and data[col].isnull().any()==True:
        li2.append(col)
    if data[col].isnull().any()==True:
        data[col].fillna(data[col].mode,inplace=True)


# In[12]:


data_cols3=data.columns.values.tolist()
li3=[]
for col in data_cols3:
    if data[col].dtype=='float'and data[col].isnull().any()==True:
        li3.append(col)
    if data[col].isnull().any()==True:
        data[col].fillna(data[col].mode,inplace=True)


# In[13]:


data.info()


# In[14]:


data.isnull().sum().sort_values()

