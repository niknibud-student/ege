import math

a = set()
p = set(range(2, 21, 2))
q = set(range(3, 31, 3))
r = set(range(12, 61, 12))

def f(x):
    return (x not in a) <= (((x in p) and (x in q)) <= (x in r))

for x in range(1, 1000):
    if f(x) == 0:
        a.add(x)
    
print(math.prod(a))