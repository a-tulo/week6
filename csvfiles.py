
# to open a file in python csv
import csv
with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(row[0])

# to open a json file
import json

with open("data.json") as json_file:
  data = json.load(json_file)

print(data)

# writing to a json file
import json

json_data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_file = open("output.json", "w")
json.dump(json_data, json_file, indent = 4)

json_file.close()