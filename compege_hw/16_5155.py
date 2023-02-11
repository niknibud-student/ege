from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n*n + f(n-1)

for n in range(1, 1001):
    f(n)

print(f(1000) - f(997))