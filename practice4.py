def no_dups(s):
    cache = {}
    s = s.split()
    for i in s:
        cache[i] = 1
    x = cache
    return cache.items()



print(no_dups("hello hello hello"))

