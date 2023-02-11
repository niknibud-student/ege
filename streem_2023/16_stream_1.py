from functools import lru_cache
import sys
sys.setrecursionlimit(100_000)

def f(n):
    if n <= 2:
        return 1
    return n*f(n-2)

print(f(5000)/f(4994))