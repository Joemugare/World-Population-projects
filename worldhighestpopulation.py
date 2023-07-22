#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# # Load the data from 'world-data-2023.csv' into the DataFrame df

# In[2]:


df = pd.read_csv('world-data-2023.csv')


# In[4]:


df


# # Clean up the column names by removing unwanted characters and spaces

# In[3]:


df.columns = df.columns.str.replace('["\n()]', '', regex=True)


# In[5]:


df


# # Convert the 'Population' column to a numeric data type

# In[6]:


df['Population'] = pd.to_numeric(df['Population'].str.replace(',', ''), errors='coerce')


# In[11]:


df


# # Convert the 'Population' column to a numerical data type (e.g., int)

# In[8]:


df['Population'] = pd.to_numeric(df['Population'], errors='coerce')


# In[9]:


df['Population']


# # Drop rows with missing or invalid population values

# In[12]:


df = df.dropna(subset=['Population'])


# In[14]:


df


# # Sort the data by population in descending order and select the top 10 countries

# In[15]:


top_10_countries = df.nlargest(10, 'Population')


# In[16]:


top_10_countries


# # Create a bar chart for the top 10 countries by population

# In[17]:


plt.figure(figsize=(10, 6))
plt.bar(top_10_countries['Country'], top_10_countries['Population'])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Top 10 Countries by Population')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# # Create a bar chart to compare the populations of China and India

# In[18]:


china_population = top_10_countries.loc[top_10_countries['Country'] == 'China', 'Population'].values[0]
india_population = top_10_countries.loc[top_10_countries['Country'] == 'India', 'Population'].values[0]

plt.figure(figsize=(8, 6))
plt.bar(['China', 'India'], [china_population, india_population])
plt.xlabel('Country')
plt.ylabel('Population')
plt.title('Population Comparison: China vs. India')
plt.show()


# In[ ]:




