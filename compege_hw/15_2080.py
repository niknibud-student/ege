def f(x, y):
    return (x*x - 10*x + 16 > 0) or (y*y - 10*y + 21 > 0) or (x*y < 2*a)

for a in range(100):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break