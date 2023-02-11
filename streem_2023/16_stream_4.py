from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 2*f(n-1) + g(n-1) + 2*n

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    return f(n-1) + 2*g(n-1) - n

for n in range(2, 10000):
    f(n)
    g(n)

print(f(10000) - g(10000) + g(9999) - f(9999))

'''
Аналитическое решение
f(10000) = 2f(9999) + g(9999) + 20000
g(10000) = f(9999) + 2g(9999) - 10000
f(10000) - g(10000) = f(9999) - g(9999) + 30000
f(10000) - g(10000) + g(9999) - f(9999) = f(9999) - g(9999) + 30000 + g(9999) - f(9999) = 30000
'''