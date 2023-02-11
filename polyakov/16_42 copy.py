from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n-1) + 3 * g(n-1)

def g(n):
    if n == 1:
        return 1
    return f(n-1) - 2 * g(n-1)
 
s = f(50)
print(sum(int(d) for d in str(s)))