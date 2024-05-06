from flask import Flask, render_template_string
import pandas as pd
import folium
import json

# with open("res.json", "r") as file:
#     data = json.load(file)

# # Convert the dictionary to a DataFrame
# df = pd.json_normalize(data)

app = Flask(__name__)

@app.route("/")
def map():
    # Create a map centered at an arbitrary location
    locations = {
        "Google HQ": {"x": -122.084, "y": 37.422},
        "Microsoft HQ": {"x": -122.13, "y": 47.64}
    }
    start_coords = (list(locations.values())[0]['y'], list(locations.values())[0]['x'])
    folium_map = folium.Map(location=start_coords, zoom_start=14)

    # Add points to the map
    for name, coordinates in locations.items():
        folium.Marker([coordinates['y'], coordinates['x']], popup=name).add_to(folium_map)

    # Render the map
    map_html = folium_map._repr_html_()

    # Use a basic inline template for the Flask app
    template = '''
        <html>
        <head>
            <title>My Map</title>
        </head>
        <body>
            {{map_html | safe}}
        </body>
        </html>
    '''

    return render_template_string(template, map_html=map_html)

if __name__ == "__main__":
    app.run(port=8061, host="0.0.0.0", debug=True)