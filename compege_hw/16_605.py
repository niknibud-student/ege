def f(n):
    sm = n*n
    if n > 1:
        sm += 2*n + 1 + f(n-2) + f(n//3)
    return sm

print(f(100))
