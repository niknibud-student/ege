def f(n):
    s = 0 
    s += n+1
    if n > 1:
        s += n+5 + f(n-1) + f(n-2)
    return s

print(f(30))