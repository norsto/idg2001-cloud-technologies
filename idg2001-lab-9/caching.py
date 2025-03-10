"""
__Part 1:__
Build the functions `get_rate(currency)` and `convert(currency1, currency2, amount)`. 
They should directly consume my API.
https://fastapi-production-03cc.up.railway.app/
"""

""" cache = {}

api = "https://fastapi-production-03cc.up.railway.app/"

def get_rate(currency):
    if currency in cache:
        print("Fetching from cache...")
        return cache[currency] 
    print("Putting value in storage...")
    result = currency 
    cache[currency] = result 
    return result

def convert(currency1, currency2, amount):
    currency1 = api 
    currency2 = api 
    amount = currency 
    return amount  """

import requests 

base_url = f"https://fastapi-production-03cc.up.railway.app/"

cache = {}

def get_rate(currency):
    url = base_url + "USD"
    response = request.get(url)
    data = response.json 