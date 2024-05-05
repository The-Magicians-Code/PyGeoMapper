from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import json

with open("res.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data)

px.set_mapbox_access_token(open(".mapbox_token").read())

# df = px.data.carshare()
print(df)
fig = px.scatter_mapbox(df, lat="location.y", lon="location.x", color="score", hover_name="attributes.ExInfo",
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=9)

app = Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(port=8061, host="0.0.0.0", debug=True)