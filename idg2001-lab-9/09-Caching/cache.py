'''
Lines where the "# timed" is added, are locations where we add or modify
something for the timed funcion to work.

Included multiple unnecessary prints, which should be removed when finished.
'''

# python3 -m pip install requests
import requests


base_url = "https://fastapi-production-03cc.up.railway.app"


cache = {}  # endpoint: results


def access_cache(endpoint):
    # timed

    # If exists.
    if endpoint in cache:
        print('From cache')
        print(cache)
        return cache[endpoint]  # timed

    # If not exists.
    results = get_from_API(endpoint)
    cache[endpoint] = results  # timed
    print('From API')
    print(cache)
    return results


def get_from_API(endpoint):
    '''Request endpoint and return results as a dict.'''
    url = base_url + endpoint
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()  # Convert the response to JSON
        return results
    else:
        print(f"Request failed with status code {response.status_code}, at url: {url}")

# print(get_from_API('/rate/NOK'))
# print(get_from_API('/convert/NOK,GBP,100'))


def get_rate(currency):
    '''Request the currency rate (using the get_from_API function).'''
    endpoint = f'/rate/{currency}'
    result = get_from_API(endpoint)
    return result

# print(get_rate('NOK'))


def convert(currency1, currency2, amount):
    '''Request the currency convertion function.'''
    endpoint = f'/convert/{currency1},{currency2},{amount}'
    result = get_from_API(endpoint)
    return result

# print(convert('NOK', 'GBP', 100))


def rate_cache(currency):
    '''Same as get_rate(), but uses the cache as well.'''
    endpoint = f'/rate/{currency}'
    result = access_cache(endpoint)
    return result

# print(rate_cache('NOK'))
# print(rate_cache('NOK'))


def convert_cache(currency1, currency2, amount):
    '''Same as convert(), but uses the cache as well.'''
    endpoint = f'/convert/{currency1},{currency2},{amount}'
    result = get_from_API(endpoint)
    return result

# print(convert_cache('NOK', 'GBP', 100))
# print(convert_cache('NOK', 'GBP', 100))


if __name__ == '__main__':
    print(rate_cache('NOK'))
    print(rate_cache('NOK'))
