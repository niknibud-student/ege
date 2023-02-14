def f(x, y):
    return (x*y > a) and (x > y) and (x < 8)

for a in range(100):
    if all(f(x, y) == 0 for x in range(1000) for y in range(1000)):
        print(a)
        break