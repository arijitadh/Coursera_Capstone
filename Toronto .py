#!/usr/bin/env python
# coding: utf-8

# In[25]:


get_ipython().system('conda install -c conda-forge folium=0.10.1 --yes ')


# In[26]:


import numpy as np # library to handle data in a vectorized mannerjavascript:void(0);

import pandas as pd # library for data analsysis

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

from pandas import read_html
print('Libraries imported.')


# In[27]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
dframe_list = pd.io.html.read_html(url)


# In[28]:


dframe = dframe_list[0]
dframe


# In[29]:


dframe.shape


# In[30]:


dframe.dropna(inplace = True)


# In[31]:


dframe['Postal code'].value_counts().to_frame


# In[32]:


dframe


# In[33]:


dframe['Neighborhood'] = dframe['Neighborhood'].str.replace('/',',')


# In[34]:


dframe


# In[35]:


dframe.shape


# In[37]:



import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_ef41cdf2bf8249b297b176d686d8cbcd = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='Sc2e5tSltx1aOVg-zLmrXRgARWcKFD82XDSImy8P0M1X',
    ibm_auth_endpoint="https://iam.ng.bluemix.net/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3-api.us-geo.objectstorage.service.networklayer.com')

body = client_ef41cdf2bf8249b297b176d686d8cbcd.get_object(Bucket='project1-donotdelete-pr-ehqzo7uscmawdx',Key='Geospatial_Coordinates.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

df_data_1 = pd.read_csv(body)
df_data_1.head()


# In[40]:


df_data_1.rename(columns = {'Postal Code':'Postal code'}, inplace = True)


# In[42]:


data = pd.merge(dframe, df_data_1)


# In[43]:


data.head()


# In[44]:


data2 = data.iloc[0:5,:]
data2


# In[48]:


address = 'Toronto, ON'

geolocator = Nominatim(user_agent="tn_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))


# In[67]:


# create map of New York using latitude and longitude values
map_Toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(data['Latitude'], data['Longitude'], data['Borough'], data['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup= 'neighborhood',
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_Toronto)  
    
map_Toronto


# In[ ]:




