a = [int(x) for x in open('17-3.txt')]
cond = lambda x, y: (x+y)%3 == 0 and (x+y)%6 != 0 and abs(x*y)%10 == 8
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(a[i], a[i+1])]
print(len(ans), max(ans))