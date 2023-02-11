def f(n):
    if n <= 5:
        return n
    if n % 5 == 0:
        return n + f(n//5 + 1)
    return n + f(n+6)


for n in range(1, 200):
    try:
        if f(n) > 1000:
            print(n, f(n))
            break
    except:
        ...