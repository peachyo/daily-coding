def coin_ways(n, cache={0: 1}):
    if n in cache:
        return cache[n]

    if n < 0:
        return 0

    cache[n] = coin_ways(n - 1) + coin_ways(n - 5)
    return cache[n]


def coin_ways2(n):
    cache = {0: 1}
    for i in range(1, n + 1):
        cache[i] = cache.get(i - 1, 0) + cache(i - 5, 0)
    return cache
