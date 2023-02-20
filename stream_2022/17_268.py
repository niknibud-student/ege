a = [int(x) for x in open('17-243.txt')]
t_sum = sum(int(d) for x in a if x % 49 == 0 for d in str(x))
cond = lambda x, y: (x > t_sum and (not y > t_sum) and y%10 == 7) or ((not x > t_sum) and y > t_sum and x%10 == 7)
ans = [(a[i]+a[i+1]) for i in range(len(a)-1) if cond(*a[i:i+2])]
print(len(ans), min(ans))