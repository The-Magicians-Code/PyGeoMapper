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
data = [geocode(object, max_locations=5)[0] for object in objects]
with open("res.json", "w") as file:
    json.dump(data, file, indent=4)

# print(data)

df = pd.json_normalize(data)