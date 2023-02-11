import sys
import math
sys.setrecursionlimit(10_000)


def f(n):
    if n >= 5000:
        return math.factorial(n)
    return 2*f(n+1)//(n+1)

print(1000*f(7)/f(4))