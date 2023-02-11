from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
         return 2
    return n*(n-1) + f(n-1) + f(n-2)

for n in range(1, 2023):
    f(n)

print(f(2023) - f(2022) - f(2020) - f(2019))

'''
2023 * 2022 + <del>f(2022)</del> + f(2021) <def>- f(2022)</del> - f(2020) - f(2019)
2023 * 2022 + 2021 * 2020 + <del>f(2020) + f(2019) - f(2020) - f(2019)</del>
2023 * 2022 + 2021 * 2020 = 8172926
'''