# Caching

I've used the following free and open API to get data.

> https://open.er-api.com/v6/latest/USD

Since we don't want to be banned, I have copied the data and added my own FastAPI in Railway. It will not be updated, so don't expect it to actually be correct. Here is my copy.

> https://fastapi-production-03cc.up.railway.app/


## My API description
My API has the following endpoints.

| Endpoint                                     | Description                                                 |
| -------------------------------------------- | ----------------------------------------------------------- |
| `/`                                          | The same info as in this table.                             |
| `/all`                                       | Shows the entire data set.                                  |
| `/rate/{currency: str}`                      | Gets the currency-to-USD ratio. E.g., `/rate/NOK`: 10.55... |
| `/convert/{c1: str},{c2: str},{amount: int}` | Converts amount from currency1 to currency2.                |

Try the API endpoints in the browser to check. For example, the following two links check the NOK rate (1) and how many GBP 100 NOK is (2).

1. > https://fastapi-production-03cc.up.railway.app/rate/NOK
2. > https://fastapi-production-03cc.up.railway.app/convert/NOK,GBP,100

Check the following GitHub repo for the API source code:

> https://github.com/catsymptote/FastAPI-currency-exchange


## The task
__Part 1:__
Build the functions `get_rate(currency)` and `convert(currency1, currency2, amount)`. They should directly consume my API.

__Part 2:__
Build an additional function `rate_cache` which takes a cache for the `get_rate` function. Its functionality should be something like the following.

1. When get_rate is called, check the cache.
    - If the cache has a match, return the match.
    - If not, update the cache from the API.

Update the `get_rate` function to use the `rate_cache`.

__Part 3:__
Build a similar function `convert_cache`. Same functionality, but it now has to work with multiple input parameters.

__Part 4:__
Make the caches expire after a 3 min. I.e., when it is more than 3 minutes since the cache value was updated, delete it, so it will have to be pulled again.


## My solutions
The following table describes which solutions include which functionality.

Name | Parts | Description
---|---|---
no-cache.py | 1 | Consumes/uses my API directly.
cache.py | 1-3 | Stores all received values in a cache, and uses this (forever).
timed-cache.py | 1-4 | Same as cache.py, but removes values when outdated (old).


## Potential upgrades
Here is a list of potential upgrades you can add to your code. Many of these are kind of large, so consider whether to work on your assignments instead. (But also, these will possibly be relevant for assignment 2, so not a waste of time.)

- Make this into a FastAPI - with the same endpoints, and push this to Railway.

- Assuming your did the last, add an endpoint `/reset` to reset the cache.

- Add another time to your cache: last_accessed. This should be reset on every access for this specific endpoint. It should have its own timer.

- Add a max_size for the cache. When the cache becomes bigger than this size, remove the oldest element from the cache.


## Additional resources
For other free and open (authentication-less) APIs, see the following list. Feel free to use any of those instead.

> https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/

Feel free to use them, but try not to spam them too much.
