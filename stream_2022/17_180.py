a = [int(x) for x in open('17-4.txt')]
cond = lambda x: x%10 in (3, 5)
ans = [x for x in a if cond(x)]
print(len(ans), max(ans))