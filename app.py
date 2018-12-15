import dash
import dash_core_components as dcc
import dash_html_components as html

import folium
from folium import plugins
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from xml.etree import ElementTree

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('first.html'),
    html.Iframe(id='map', srcDoc=open('first.html', 'r').read(),width="100%",height="300%")
])

if __name__ == '__main__':
    app.run_server(debug=True)