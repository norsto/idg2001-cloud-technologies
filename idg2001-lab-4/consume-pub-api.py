import requests

long = ""
lat = ""
url = f"https://www.7timer.info/bin/astro.php?lon={long}&lat={lat}.1&ac=0&unit=metric&output=json&tzshift=0"

x = requests.get(url)
print(x)