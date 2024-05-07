#!/usr/bin/env python3
# @Author: Tanel Treuberg
# @Github: https://github.com/The-Magicians-Code
# @Description: Process location data

from arcgis.geometry import Point, distance
from arcgis.geocoding import geocode
from arcgis.gis import GIS
from pathlib import Path
import pandas as pd

def process_and_prepare(filename: str, save: bool=True) -> pd.DataFrame:
    """
    Processes and prepares data from a file containing location objects.

    Parameters:
        filename (str): The path to the file containing location objects.
        save (bool, optional): Whether to save the processed data to a CSV file. Defaults to True.

    Returns:
        pd.DataFrame: A DataFrame containing processed location data.

    Example:
        # Process data from file "locations.txt"
        df = process_and_prepare("locations.txt")
    """
        
    fname = Path(filename).__str__()
    with open(fname, "r") as file:
        objects = [line.rstrip() for line in file.readlines()]

    # Create an anonymous GIS session
    gis = GIS()
    # Geocode the objects
    data = [geocode(object, max_locations=1)[0] for object in objects]

    # Veerenni being the root location and the first in the source file
    # Marking distance as 0 and setting the coordinates as root
    data[0]["distance"] = 0
    root = Point(data[0]["location"])

    # Calculate the distances from the rest of the points and add them to the dataframe
    for item in data[1:]:
        item.update(distance(4326, root, Point(item["location"]), geodesic=True))

    df = pd.json_normalize(data)
    df = df[["address", "score", "distance", "location.x", "location.y", "attributes.ExInfo"]]
    df["marker_size"] = 10

    if save:
        df.to_csv("../data/processed.csv")
    print(df)

    return df

if __name__ == "__main__":
    process_and_prepare("../data/source.txt")