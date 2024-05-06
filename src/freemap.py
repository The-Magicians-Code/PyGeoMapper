from dash import Dash, dcc, html
from base64 import b64encode
import plotly.express as px
import pandas as pd
import json
import io

with open("res.json", "r") as file:
    data = json.load(file)

# Convert the dictionary to a DataFrame
df = pd.json_normalize(data)

# Create a scatter mapbox
fig = px.scatter_mapbox(df, lat="location.y", lon="location.x", color="distance", hover_name="attributes.ExInfo",
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=9)

buffer = io.StringIO()

fig.update_layout(mapbox_style="open-street-map")
# fig.write_html("map.html")

# Create an html object and encode it
fig.write_html(buffer)
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

# Create a Dash app
app = Dash(__name__)

# Define the layout
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
