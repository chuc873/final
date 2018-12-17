import folium
from folium import plugins
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from xml.etree import ElementTree

%matplotlib inline

df=pd.read_csv('pop_data.csv')

m = folium.Map([6.5244,3.3792], zoom_start=1)

one=df.loc[df['Year'] == 2010]

firstmap = folium.Map([6.5244,3.3792], zoom_start=1)
one.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], 
                                                  row["Longitude"]]).add_to(m),
     axis=1)

for i in range(0,len(one)):
   folium.Circle(
      location=[one.iloc[i]['Latitude'], one.iloc[i]['Longitude']],
      popup=one.iloc[i]['Cities'],
      radius=one.iloc[i]['Population']*20000,
      color='black',
      fill=True,
      fill_color='black'
   ).add_to(firstmap)

firstmap.save(outfile= "one.html")

two=df.loc[df['Year'] == 2025]

secondmap = folium.Map([6.5244,3.3792], zoom_start=1)
two.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], 
                                                  row["Longitude"]]).add_to(m),
     axis=1)

for i in range(0,len(two)):
   folium.Circle(
      location=[two.iloc[i]['Latitude'], two.iloc[i]['Longitude']],
      popup=two.iloc[i]['Cities'],
      radius=two.iloc[i]['Population']*20000,
      color='black',
      fill=True,
      fill_color='black'
   ).add_to(secondmap)

secondmap.save(outfile= "two.html")

three=df.loc[df['Year'] == 2050]

thirdmap = folium.Map([6.5244,3.3792], zoom_start=1)
three.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], 
                                                  row["Longitude"]]).add_to(m),
     axis=1)

for i in range(0,len(three)):
   folium.Circle(
      location=[three.iloc[i]['Latitude'], three.iloc[i]['Longitude']],
      popup=three.iloc[i]['Cities'],
      radius=three.iloc[i]['Population']*20000,
      color='black',
      fill=True,
      fill_color='black'
   ).add_to(thirdmap)

thirdmap.save(outfile= "three.html")

four=df.loc[df['Year'] == 2075]

fourthmap = folium.Map([6.5244,3.3792], zoom_start=1)
four.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], 
                                                  row["Longitude"]]).add_to(m),
     axis=1)

for i in range(0,len(four)):
   folium.Circle(
      location=[four.iloc[i]['Latitude'], four.iloc[i]['Longitude']],
      popup=four.iloc[i]['Cities'],
      radius=four.iloc[i]['Population']*20000,
      color='black',
      fill=True,
      fill_color='black'
   ).add_to(fourthmap)

fourthmap.save(outfile= "four.html")

five=df.loc[df['Year'] == 2100]

fifthmap = folium.Map([6.5244,3.3792], zoom_start=1)
five.apply(lambda row:folium.CircleMarker(location=[row["Latitude"], 
                                                  row["Longitude"]]).add_to(m),
     axis=1)

for i in range(0,len(five)):
   folium.Circle(
      location=[five.iloc[i]['Latitude'], five.iloc[i]['Longitude']],
      popup=five.iloc[i]['Cities'],
      radius=five.iloc[i]['Population']*20000,
      color='black',
      fill=True,
      fill_color='black'
   ).add_to(fifthmap)