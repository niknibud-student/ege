a = [int(x) for x in open('17-5.txt')]
cond = lambda x, y: abs(x)%10 == 7 or abs(y)%10 == 7
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(a[i], a[i+1])]
print(len(ans), max(ans))