from itertools import combinations

Ox = [i/4 for i in range(16*4, 80*4)]
m = []

def f(x):
    d = 17 <= x <= 58
    c = 29 <= x <= 80
    a = a1 <= x <= a2
    return d <= (((not c) and (not a)) <= (not d))

for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)

print(min(m))