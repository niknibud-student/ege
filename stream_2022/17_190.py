a = [int(x) for x in open('17-7.txt')]
cond = lambda x: x%8 == 7 and x//8%8 != 2
# cond = lambda x: oct(x)[-1] == '7' and oct(x)[-2] == '2'
# cond = lambda x: x%8 == 7 and x%64 == int('27', 8)
ans = [x for x in a if cond(x)]
print(len(ans), max(ans))