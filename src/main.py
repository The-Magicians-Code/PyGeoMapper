from arcgis.geometry import Point, distance
from arcgis.geocoding import geocode
from arcgis.gis import GIS
from pathlib import Path
import pandas as pd
import json

fname = Path("source.csv").__str__()
with open(fname, "r") as file:
    objects = [line.rstrip() for line in file.readlines()]

# Create an anonymous GIS session
gis = GIS()
# Geocode the objects
# Out_fields malfunctioning?
data = [geocode(object, max_locations=1)[0] for object in objects]

# Veerenni being the zero point
data[0]["distance"] = 0
root = Point(data[0]["location"])

for item in data[1:]:
    item.update(distance(4326, root, Point(item["location"]), geodesic=True))

with open("res.json", "w") as file:
    json.dump(data, file, indent=4)

# print(data)

df = pd.json_normalize(data)
df = df[["address", "score", "distance", "location.x", "location.y", "attributes.ExInfo"]]
print(df)