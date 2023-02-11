# Решение через увеличение границы рекурсии
import sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 10000:
        return n
    if n % 4 == 0:
        return n//4 + f(n//4 + 2)
    return 1 + f(n+2)

print(f(174) - f(3))

'''
Аналитическое решение:
f(174) = 1 + f(176)
f(176) = 44 + f(46)
f(46) = 1 + f(48)
f(48) = 12 + f(14)
f(14) = 1 + f(16)
f(16) = 4 + f(6)
f(6) = 1 + f(8)
f(8) = 2 + f(4)
f(4) = 1 + f(3)
f(174) = 1 + 44 + 1 + 12 + 1 + 4 + 1 + 2 + 1 + f(3)
1 + 44 + 1 + 12 + 1 + 4 + 1 + 2 + 1 + f(3) - f(3)
1 + 44 + 1 + 12 + 1 + 4 + 1 + 2 + 1 = 67
'''

# Решение через кэширование
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n % 4 == 0:
         return n//4 + f(n//4 + 2)
    return 1 + f(n+2)

for n in range(10000, 1, -1):
    if n % 4 != 0 and n % 2 != 0:
        f(n)
for n in range(10000, 1, -1):
    f(n)

print(f(174) - f(3))