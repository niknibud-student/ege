def f(n):
    if n < 3:
        return n
    if n % 2 == 0:
        return (n + f(n-2))//5
    return (2*n + f(n-1) + f(n-2))//4

print(f(50))