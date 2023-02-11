def f(n):
    if n > 25:
        return 2 * n**3 + 1
    return f(n+2) + 2*f(n+3)

cnt = 0
for n in range(1, 1001):
    if f(n) % 11 == 0:
        cnt += 1 

print(cnt)