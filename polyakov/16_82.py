def f(n):
    if n <= 5:
        return n
    if n % 4 == 0:
        return n + f(n//2 - 1)
    return n + f(n+2)

for n in range(1, 20):
    try:
        print(n, f(n))
    except RecursionError:
        ...

