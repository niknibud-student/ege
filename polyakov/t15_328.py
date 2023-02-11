from itertools import combinations
coords = combinations(range(200), r=3)

def f(x, y, z):
    return (220 != y + 2*x + z) or (a < 6*x) or (a < 2*z) == 1

for a in range(200):
    # if all(f(x, y, z) for x in range(150) for y in range(150) for z in range(150)):
    #     print(a)
    if all(f(x, y, z) for x, y, z in coords):
        print(a)