a = set()
p = set(range(1, 12, 2))
q = set(range(3, 13, 3))

def f(x): 
    return ((x in p) <= (x not in q)) or (x in a)

for x in range(100):
    if f(x) == 0:
        a.add(x)
    
print(sum(a))
