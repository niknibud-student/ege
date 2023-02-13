def f(n):
    if n == 1:
        return 2
    return f(n-1) +5*n*n

print(f(39))