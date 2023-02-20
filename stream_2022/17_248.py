a = [int(x) for x in open('17-243.txt')]
mx = max(x for x in a if x % 119 == 0)
cond = lambda x, y: (x > mx or y > mx) and any(abs(z)%100 == 21 for z in (x, y))
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(a[i], a[i+1])]
print(len(ans), min(ans))