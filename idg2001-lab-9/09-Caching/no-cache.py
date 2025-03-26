# python3 -m pip install requests
import requests


# Location of the API endpoints.
base_url = "https://fastapi-production-03cc.up.railway.app"


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


# Run only if this is the main file, not if this file is imported.
if __name__ == '__main__':
    print(convert('NOK', 'GBP', 100))
