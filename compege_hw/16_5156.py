import sys
sys.setrecursionlimit(100_000)

def f(n):
    if n <= 3:
        return n
    if n % 2 != 0:
        return 2*n + f(n-2)
    return n*n + f(n-1)

print(f(10000)-f(9995))