from itertools import combinations

Ox = [x/4 for x in range(16*4, 84*4)]
m = []

def f(x):
    p = 17 <= x <= 54
    q = 37 <= x <= 83
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)

print(min(m))
