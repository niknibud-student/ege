a = [int(x) for x in open('17-7.txt')]
cond = lambda x: sum(map(int, str(x)))%3 == 0
ans = [x for x in a if cond(x)]
print(len(ans), max(ans))