# Изменена на стриме
def f2(x):
    cnt = 0
    while x > 0:
        if x % 3 == 2:
            cnt += 1
        x //= 3
    return cnt == 3

def f0(x):
    cnt = 0
    while x > 0:
        if x % 7 == 0:
            cnt += 1
        x //= 7
    return cnt == 0

a = [int(x) for x in open('17-4.txt')]
cond = lambda x: f2(x) and f0(x)
ans = [x for x in a if cond(x)]
print(len(ans), min(ans))

