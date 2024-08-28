import json
import os

dictionary = {
    "name": "Pera",
    "age": 22,
    "cars": [
        "Jugo",
        "Kec"
    ],
    "parent": {
        "name": "Mika",
        "age": 5000
    }
}

json_object = json.dumps(dictionary, indent=4)
file_path = os.path.join('vezbe8', 'primer.json')
json_file = open(file_path, 'w')
json_file.write(json_object)
json_file.close()