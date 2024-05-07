#!/usr/bin/env python3
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Display location data on an interactive web map

from dash import Dash, dcc, html
from base64 import b64encode
from process import process_and_prepare
import plotly.express as px
import pandas as pd
import io

try:
    df = pd.read_csv("../data/processed.csv")
except:
    print("File not existent! Proceeding with data processing, it will take time")
    df = process_and_prepare("../data/source.txt", False)

# Create a scatter map
fig = px.scatter_mapbox(df, lat="location.y", lon="location.x", color="distance", hover_name="attributes.ExInfo",
    color_continuous_scale=px.colors.cyclical.IceFire, zoom=8.8, height=800, width=800, size="marker_size", size_max=15,
    hover_data={
        "marker_size": False
    },
    labels={
        "location.x": "x",
        "location.y": "y"
    }, 
    center={
        "lat": df["location.y"].mean(),
        "lon": df["location.x"].mean()
    })

# Add map style
fig.update_layout(mapbox_style="open-street-map")

# Create an html object and encode it
buffer = io.StringIO()
fig.write_html(buffer)
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

# Create a Dash server
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H2("Interactive map"),
    dcc.Graph(figure=fig),
    html.A(
        html.Button("Download interactive map"),
        id="download",
        href=f"data:text/html;base64,{encoded}",
        download="map.html"
    )
])

# Run the app
if __name__ == '__main__':
    app.run(port=8061, host="0.0.0.0", debug=True)
