def f(x):
    return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))

for a in range(1, 1000):
    if all(f(x) for x in range(100_000)):
        print(a)
        break