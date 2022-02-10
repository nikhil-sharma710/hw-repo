import json

with open("sites.json", "r") as f:
    sites_data = json.read(f)

print(sites_data)
starting_lat = 16.0
starting_long = 82.0


