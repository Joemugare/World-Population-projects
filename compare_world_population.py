#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt


# In[14]:


df =pd.read_csv('world-data-2023.csv')


# # Display the CSv file contents

# In[20]:


df


# # Get the populations of the specified countries

# In[15]:


def compare_population_pie(df, country1, country2):
    
    country1_population = df.loc[df['Country'] == country1, 'Population'].str.replace(',', '').astype(float).values[0]
    country2_population = df.loc[df['Country'] == country2, 'Population'].str.replace(',', '').astype(float).values[0]

    # Create a pie chart to compare the populations of the specified countries
    plt.figure(figsize=(8, 6))
    labels = [country1, country2]
    sizes = [country1_population, country2_population]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f'Population Comparison: {country1} vs. {country2}')
    plt.show()






# # Assuming you have already loaded the data into the DataFrame 'df'

# In[16]:


#Let's compare the populations of two different countries using a pie chart
compare_population_pie(df, 'Uganda', 'Kenya')


# # Let's compare the populations of other different countries using a pie chart

# In[17]:


compare_population_pie(df, 'China', 'Zambia')


# In[18]:


compare_population_pie(df, 'China', 'Nigeria')


# In[19]:


compare_population_pie(df, 'India', 'United States')


# In[ ]:




