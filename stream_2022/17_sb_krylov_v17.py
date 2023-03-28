a = [int(x) for x in open('17var18.txt')]
cond = lambda x, y: (x*x + y*y) % 2 != 0 and x*x + y*y < 80
ans = [(a[i], a[i+1]) for i in range(len(a)-1) if cond(*a[i:i+2])]
mx = max(ans, key=sum)
print(len(ans), ans)