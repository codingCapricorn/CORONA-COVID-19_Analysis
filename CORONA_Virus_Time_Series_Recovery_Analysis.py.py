# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

#CORONA VIRUS TIME SERIES RECOVERY ANALYSIS USING MACHINE LEARNING 

Dataset ::: Recovered CoViD-19 cases from 1/22/20 TO 6/13/20

File Name :: (csse_covid_19_time_series)
time_series_covid19_recovered_global.csv

URL :: https://github.com/CSSEGISandData/COVID-19

Dataset is taken from John Hopkins University Github .... https://github.com/CSSEGISandData
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
# %matplotlib inline

df=pd.read_csv('/content/time_series_covid19_recovered_global.csv')

df.head()

df.info()

df.dtypes

df.shape

df.describe()

df.columns

for j in range(1,148):
       print(df.iloc[:, j].unique())

## finding all columns that have nan:

droping_list_all=[]
for j in range(0,7):
    if not df.iloc[:, j].notnull().all():
        droping_list_all.append(j)        
        #print(df.iloc[:,j].unique())
droping_list_all

df.isnull().sum()

df.describe()

df.Lat.plot(title='LATTITUDE',color='r') 
plt.tight_layout()
plt.show()   

df.Long.plot(title='LONGITUDE',color='g') 
plt.tight_layout()
plt.show()   

df.Lat.plot(color='r', legend=True)
df.Long.plot(color='g', legend=True) 
plt.tight_layout()
plt.title("Lat vs Long")
plt.show()

df['1/22/20'].plot(color='g', legend=True)
df['1/23/20'].plot(color='g', legend=True)
df['1/24/20'].plot(color='g', legend=True)
df['1/25/20'].plot(color='g', legend=True)
df['1/26/20'].plot(color='g', legend=True)
df['1/27/20'].plot(color='g', legend=True)
df['1/28/20'].plot(color='g', legend=True)
df['1/29/20'].plot(color='g', legend=True)
df['1/30/20'].plot(color='g', legend=True)
df['1/31/20'].plot(color='g', legend=True)
plt.xticks(rotation=60)
plt.ylabel('No of patients')
plt.title('JANUARY month Recovery')
plt.show()

df['1/22/20'].plot(color='y', legend=True)
df['2/22/20'].plot(color='g', legend=True)
df['3/22/20'].plot(color='b', legend=True)
df['4/22/20'].plot(color='r', legend=True)
df['5/22/20'].plot(color='y', legend=True)
#plt.show()
plt.xticks(rotation=60)
plt.ylabel('No Of Patients')
plt.title('Recovered on x/22/20')
plt.show()

df['1/22/20'].plot(color='g', legend=True)
df['6/13/20'].plot(color='r', legend=True)
plt.title("Difference Betw Patients recovered on 1/22 and 6/13")
plt.show()

df['2/15/20'].plot(kind='hist',color='g', legend=True)
df['3/15/20'].plot(kind='hist',color='g', legend=True)
df['4/15/20'].plot(kind='hist',color='g', legend=True)
df['5/15/20'].plot(kind='hist',color='g', legend=True)
plt.xticks(rotation=60)
plt.xlabel('No Of Patients')
plt.title('Recovered on various dates')
plt.show()

data_returns = df
sns.jointplot(x='Lat', y='Long', data=data_returns)  
plt.title("Corona Effect All Over Globe")
plt.show()

data_returns = df
sns.jointplot(x='4/13/20', y='6/13/20', data=data_returns)  

plt.show()

plt.matshow(df.corr(method='pearson'),vmax=1,vmin=-1,cmap='PRGn')
plt.title('Recovery', size=15)
plt.colorbar()
plt.show()

df['Country/Region'].value_counts().sort_values()

y=df['Province/State'].value_counts()
plt.pie(y,labels=y.index,autopct="%0.2f%%",shadow=True)
plt.show()

y=df['Province/State'].value_counts()
y

y=df['Country/Region'].value_counts()
plt.pie(y,labels=y.index,autopct="%0.2f%%",shadow=True)
plt.show()

y=df['Country/Region'].value_counts()
y

y=df['1/22/20'].value_counts()
plt.pie(y,labels=y.index,autopct="%0.2f%%",shadow=True)
plt.show()

y=df['2/13/20'].value_counts()
plt.pie(y,labels=y.index,autopct="%0.2f%%",shadow=True)
plt.show()

p=df.pivot_table(index='Country/Region',columns='5/10/20')
p

sns.heatmap(p,linewidths=5,linecolor='blue',cmap='Accent_r')
plt.show()

df[:10].plot.bar(x='Country/Region',y=['1/22/20','2/22/20','3/22/20','4/22/20','5/22/20','6/13/20'])

df[:10].plot.bar(x='Province/State',y=['1/22/20','2/22/20','3/22/20','4/22/20','5/22/20','6/13/20'])

df[:10].plot.bar(x='Country/Region',y=['5/22/20','6/13/20'])

df[:10].plot.bar(x='Province/State',y=['5/22/20','6/13/20'])

df['Province/State'].isnull().sum()

chart_df = df.drop(['Province/State','Lat', 'Long'],axis=1)
chart_df.head()

chart_df.shape

chart_df.columns

chart_df['Country/Region'].value_counts()

chart_df.head(10)

chart_df = chart_df.groupby('Country/Region').agg(np.sum)
chart_df = chart_df.reset_index()
chart_df.head(10)

chart_df.shape

chart_df.to_csv('bar_chart_race.csv')

