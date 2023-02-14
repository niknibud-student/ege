a = set()
p = set(range(3, 13, 3))
q = set(range(1, 7))

def f(x):
    return not((x not in a) and (x in p)) or (x not in q)


for x in range(100):
    if f(x) == 0:
        a.add(x)

print(len(a))