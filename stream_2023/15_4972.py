from itertools import combinations

def f(x):
    p = 25 <= x <= 50
    q = 54 <= x <= 75
    a = a1 <= x <= a2
    return q <= ((p == q) or ((not p) <= a))

Ox = [i/4 for i in range(24*4, 76*4)]  # числовая школа
m = []  # Длины отрезков

for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        m.append(a2-a1)

print(min(m))

