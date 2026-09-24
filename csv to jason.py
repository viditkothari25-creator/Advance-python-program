

import csv
import json

with open("input.csv", "r") as file:
    data = csv.DictReader(file)
    
    data = list(data)

with open("output.json", "w") as file:
    json.dump(data, file)

print("CSV file converted to JSON successfully!")



















