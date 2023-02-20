a = [int(x) for x in open('17-1.txt')]
avg = sum(a) / len(a)
cond = lambda x, y, z: (x > avg) + (y > avg) + (z > avg) > 1
ans = [sum(a[i:1+3]) for i in range(len(a)-2) if cond(*a[i:i+3])]
print(len(ans), max(ans))