# Решение через кэширование
from functools import lru_cache
from math import factorial

@lru_cache(None)
def f(n):
    if n >= 100: # 10000
        return factorial(n)
    if n % 2 == 0:
        return f(n+1) * f(n+2)
    return (n+2)/f(n+2)

for n in range(100, 0, -1): # 10000
    f(n)

print(f(10)/f(38))

