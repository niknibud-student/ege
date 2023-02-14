def f(x, y):
    return (x > 39) or (y > 26) or (2*x + 4*y < a)

for a in range(1000):
    if all(f(x, y) for x in range(10000) for y in range(10000)):
        print(a)
        break