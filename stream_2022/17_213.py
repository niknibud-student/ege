from statistics import mean
a = [int(x) for x in open('17-1.txt')]
# avg = sum(a) / len(a)
avg = mean(a)
cond = lambda x, y: x > avg and y > avg and abs(x+y)%100 == 31
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(a[i], a[i+1])]
print(len(ans), max(ans))