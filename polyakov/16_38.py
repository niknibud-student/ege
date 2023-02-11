def f(n, m):
    if m == 0:
        d = 0
    else:
        d = n + f(n, m-1)
    return d

cnt = 0
for n in range(1, 100):
    for m in range(1, 100):
        if f(n, m) == 30:
            cnt += 1
print(cnt)