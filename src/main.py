from arcgis.geocoding import geocode
from arcgis.gis import GIS
from pathlib import Path
# import pandas as pd
# import pipreqs.pipreqs as pr
import json

# pr.main()

fname = Path("source.csv").__str__()
with open(fname, "r") as file:
    objects = [line.rstrip() for line in file.readlines()]

# Create an anonymous GIS session
gis = GIS()
# Geocode the objects
coded = [geocode(object)[0] for object in objects]
with open("res.json", "w") as file:
    json.dump(coded, file, indent=4)

# print(coded)