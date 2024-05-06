from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import json

with open("res.json", "r") as file:
    data = json.load(file)

# Convert the dictionary to a DataFrame
df = pd.json_normalize(data)

# Create a scatter mapbox
fig = px.scatter_mapbox(df, lat="location.y", lon="location.x", color="distance", hover_name="attributes.ExInfo",
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=9)

fig.update_layout(mapbox_style="open-street-map")

# Create a Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(port=8061, host="0.0.0.0", debug=True)
