from arcgis.geocoding import geocode
from arcgis.gis import GIS
from pathlib import Path
import pandas as pd
# import pipreqs.pipreqs as pr

# pr.main()

fname = Path("source.csv").__str__()
with open(fname, "r") as file:
    objects = [line.rstrip() for line in file.readlines()]

print(objects)

# Create an anonymous GIS session
gis = GIS()
# Geocode the objects
coded = {object: geocode(object)[0] for object in objects}

df = pd.DataFrame(coded)
print(df)
