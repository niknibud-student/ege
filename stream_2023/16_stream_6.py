from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 0:
         return 0
    if n % 2 != 0:
         return 1 + f(n//2)
    return f(n//2)


for n in range(1, 20):
    print(n, bin(n)[2:], f(n))

'''
Идейное решение, исходя из основной задачи
'''
cnt = 0
for i in range(50):
     for j in range(i+1, 50):
          for k in range(j+1, 50):
               a = 2**i + 2**j + 2**k
               if a <= 1_000_000_000:
                    cnt += 1
print(cnt)

'''
Аналитическое решение
Длина двоичной записи числа 1_000_000_000 - 30 знаков
тогда на любые 3 места можно поставить 1,
т.е. 30*29*28 / 3! = 4060
'''