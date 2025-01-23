# (Initially) an empty dictionary called cache
cache = {}

# Returns the square of x
def f(x):
    return x ** 2

# Checks if the result for x is already stored in the cache
def cached_f(x):
    if x in cache:
    # If x has alreeady been calculated before (it'll be in the cache), --
    # the function will return the stored value instead of recalculating it
        return cache[x]  
    # Else, if not in cache--
    else:
        # Calculates result/the x
        result = f(x)  
        # Stores result in cache
        cache[x] = result  
        # Returns the result
        return result


print(cache)        # Initially empty: {}

print(cached_f(3))  # First call, calculates 3**2 = 9, stores the answer in cache
print(cache)        # Now: {3: 9}

print(cached_f(3))  # Second call, retrieves from cache (no recalculation)

print(cached_f(4))  # First time for 4, calculates 4**2 = 16
print(cache)        # Now: {3: 9, 4: 16}