from functools import lru_cache
import sys
sys.setrecursionlimit(1_000_000)

def f(n):
    if n > 100_000:
        return n
    return f(n+1) + 5*n + 2


print(f(3) - f(7))