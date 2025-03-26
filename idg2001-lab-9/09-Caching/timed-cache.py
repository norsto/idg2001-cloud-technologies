# python3 -m pip install requests
import requests
import time


base_url = "https://fastapi-production-03cc.up.railway.app"


cache = {}  # endpoint: (results, time_added)


def access_cache(endpoint):
    time_added = time.time()

    # Remove old values
    for key, value in cache.items():
        results, old_time_added = value
        duration = time_added - old_time_added
        if duration > 2:
            del cache[key]

    # If exists.
    if endpoint in cache:
        print('From cache')
        print(cache)
        return cache[endpoint][0]

    # If not exists.
    print('From API')
    results = get_from_API(endpoint)
    cache[endpoint] = (results, time_added)
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
    endpoint = f'/rate/{currency}'
    result = access_cache(endpoint)
    return result


def convert_cache(currency1, currency2, amount):
    '''Request the currency convertion function.'''
    endpoint = f'/convert/{currency1},{currency2},{amount}'
    result = access_cache(endpoint)
    return result


if __name__ == '__main__':
    # Test cache, wait for cached value to expire, test cache again.
    print(rate_cache('NOK'))
    print(rate_cache('NOK'))

    time.sleep(3)

    print(rate_cache('NOK'))
    print(rate_cache('NOK'))
