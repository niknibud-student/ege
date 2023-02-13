def f(n):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return (n//3)*f(n//3) + n
    return f(n-1) + n*n + 5

cnt = 0
for n in range(1, 1001):
    if all(d in '02468' for d in str(f(n))):
        cnt += 1
print(cnt)