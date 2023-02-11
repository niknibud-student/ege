# import sys
# sys.setrecursionlimit(10000000)
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 10000:
        return n - 10000
    return f(n+1) + f(n+2)

for n in range(10000, 0, -1):
    f(n)

f1 = f(12345)
f2 = f(10)
f3 = f(12)
f4 = f(11)
f5 = f(10101)
print(f1 * (f2 - f3)/f4 + f5)