from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n/2 + f(n-1)
    return n + f(n-2)

for n in range(2, 10000):
    f(n)


print(f(10000)-f(9993))
'''
f(10000) = 10000/2 + f(9999)
f(9999) = 9999 + f(9997)
f(9997) = 9997 + f(9995)
f(9995) = 9995 + f(9993)
5000 + 9999 + 9997 + 9995 = 34991

'''
