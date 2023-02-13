def f(n):
    if n > 30:
        return n*n + 5*n + 4
    if n % 2 == 0:
        return f(n+1) + 3*f(n+4)
    return 2*f(n+2)+f(n+5)

cnt = 0
for n in range(1, 1001):
    if sum(int(d) for d in str(f(n))) == 27:
        cnt += 1
print(cnt)