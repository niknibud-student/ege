a = [int(x) for x in open('17-257.txt')]
mx = max(x for x in a if x % 2 != 0)
mn = min(x for x in a if x % 2 != 0)
cond = lambda x, y: (x+y)%2 == 0 and (x+y) > (mx+mn)
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(*a[i:i+2])]
print(len(ans), min(ans))