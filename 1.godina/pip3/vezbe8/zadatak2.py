import json
import os

file_path = os.path.join('vezbe8', 'contacts-data.json')
json_file = open(file_path, newline='')
json_data = json.loads(json_file.read())

provider_dict = {}

for obj in json_data:
    provider = obj['email'].split('@')[1]
    person = obj['name']
    provider_dict[provider] = provider_dict.get(provider, []) + [person]

json_file.close()

json_new = json.dumps(provider_dict, indent=4)
file_path = os.path.join('vezbe8', 'providers.json')
json_file = open(file_path, 'w')
json_file.write(json_new)
json_file.close()