a = set(range(1, 60))
p = set(range(2, 21, 2))
q = set(range(5, 51, 5))

def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))

for x in range(1, 100):
    if f(x) == 0:
        a.remove(x)
print(len(a))