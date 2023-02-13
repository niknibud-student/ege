def f(n):
    if n <= 3:
        return n
    if n % 3 == 0:
        return n**3 + f(n-1)
    if n % 3 == 1:
        return 4 + f(n//3)
    return n*n + f(n-2)

print(f(100))