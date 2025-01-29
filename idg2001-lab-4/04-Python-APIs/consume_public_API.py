import json
import requests


# Setup
LONGITUDE = '60.8'
LATITUDE = 10.7
API_LINK = f'https://www.7timer.info/bin/astro.php?lon={LONGITUDE}&lat={LATITUDE}&ac=0&unit=metric&output=json&tzshift=0'
# https://www.7timer.info/bin/astro.php?lon=60.8&lat=10.7&ac=0&unit=metric&output=json&tzshift=0


# Call API
response = requests.get(API_LINK)
print(response)
data = response.json()
pretty_data = json.dumps(data, indent=4)


# Print and store output in a file
print(pretty_data)
with open('data.json', 'w') as f:
    f.write(pretty_data)
