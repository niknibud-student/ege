from itertools import combinations

Ox = [x/4 for x in range(15*4, 52*4)]
m = []

def f(x):
    b = 18 <= x <= 52
    c = 16 <= x <= 41
    a = a1 <= x <= a2
    return (b <= a) and ((not c) or a)

for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)

print(min(m))