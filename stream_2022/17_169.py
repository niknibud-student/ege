a = [int(x) for x in open('17-4.txt')]
cond = lambda x: x%3 == 0 and x%7 != 0 and x%17 != 0 and x%19 != 0 and x%27 != 0
ans = [x for x in a if cond(x)]
print(len(ans), max(ans))

