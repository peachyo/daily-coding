def staircase(n, X):
    cache = [0 for _ in range(n+1)]
    cache[0] = 1

    for i in range(1, n+1):
        cache[i] += sum(cache[i-step] for step in X if i - step >= 0)

    return cache[n]

