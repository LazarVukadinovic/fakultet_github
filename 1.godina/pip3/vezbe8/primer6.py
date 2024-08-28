import json
import os

file_path = os.path.join('vezbe8', 'primer.json')
json_file = open(file_path, newline='')

json_data = json.loads(json_file.read())

print(json_data['name'])
print(json_data['parent']['name'])

json_file.close()