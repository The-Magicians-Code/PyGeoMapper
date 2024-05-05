import pandas as pd
import json

with open("res.json", "r") as file:
    data = json.load(file)

df = pd.json_normalize(data)
print(df)