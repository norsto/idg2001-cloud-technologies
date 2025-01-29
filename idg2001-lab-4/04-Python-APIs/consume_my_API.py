import json
import requests


API_LINK = 'http://127.0.0.1:8000/items'


response = requests.get(API_LINK)
print(response)
data = response.json()

with open('our_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
