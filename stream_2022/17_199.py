a = [int(x) for x in open('17-199.txt')]
f2 = lambda x: 10 <= x <= 99 and x % 2 == 0
cond = lambda x, y, z: (not f2(x)) and f2(y) and (not f2(z))
ans = [(a[i]+a[i+1]+a[i+2]) for i in range(len(a)-2) if cond(*a[i:i+3])]
print(len(ans), max(ans))