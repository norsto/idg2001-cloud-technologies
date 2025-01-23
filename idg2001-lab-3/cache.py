"""
print(f)
print("hello?")
print("it is working")
"""

cache = {}

def f(x):
    return x ** 2

def cached_f(x):
#    global cache
#    if x in cache:
    return cache[x]  # Return cached result
#    else:
#        result = f(x)  # Calculate result
#        cache[x] = result  # Store result in cache
#        return result


print(cached_f(3))
print(cached_f(3))
print(cached_f(3))
