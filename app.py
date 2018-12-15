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

    html.H2('second.html'),
    html.Iframe(id='map', srcDoc=open('second.html', 'r').read(),width="100%",height="300%")

    html.H3('three.html'),
    html.Iframe(id='map', srcDoc=open('three.html', 'r').read(),width="100%",height="300%")

    html.H4('four.html'),
    html.Iframe(id='map', srcDoc=open('four.html', 'r').read(),width="100%",height="300%")

    html.H5('five.html'),
    html.Iframe(id='map', srcDoc=open('five.html', 'r').read(),width="100%",height="300%")
])

if __name__ == '__main__':
    app.run_server(debug=True)