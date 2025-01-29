def f(x):
    return x**2

cache = {}

def cached_f(x):
    global cache
    if x in cache:
        print('Used cache :D')
        return cache[x]

    print('Did not use cache :c')
    y = f(x)
    cache[x] = y
    return y


print(cached_f(3))  # No cache
print(cached_f(3))  # Cache
print(cached_f(3))  # Cache
print(cached_f(4))  # No cache
print(cached_f(4))  # Cache
