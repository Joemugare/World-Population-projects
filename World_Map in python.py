#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd


# # Load data from the CSV file

# In[4]:


df = pd.read_csv('world-data-2023.csv')


# In[5]:


df


# # Drop rows with missing values in Latitude and Longitude columns

# In[24]:


country_data_cleaned = df.dropna(subset=['Latitude', 'Longitude'])


# # Create a map centered on the first city's location

# In[26]:


country_name = country_data_cleaned["Country"]
country_coords = list(zip(country_data_cleaned["Latitude"], country_data_cleaned["Longitude"]))


# # Create the Folium map

# In[27]:


map_countries = folium.Map(location=[0, 0], zoom_start=2)


# # Add markers for each city in the dataframe

# In[28]:


for name, coords in zip(country_name, country_coords):
    folium.Marker(location=coords, popup=name).add_to(map_countries)


# # Display the map

# In[29]:


map_countries


# In[ ]:




