from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return f(n-2) + n - 2
    return f(n+2) + n + 2

cnt = 0
for n in range(1, 10000):
    try:
        if len(str(f(n))) == 5:
            cnt += 1
    except:
        ...
print(cnt)