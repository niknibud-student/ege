from itertools import product

bit_chain = [''.join(i) for i in product('01', repeat=8)]
a = set()
p = {i for i in bit_chain if i[:2] == '11'}
q = {i for i in bit_chain if i[-1] == '0'}


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not A) <= (P or (not Q))

for x in bit_chain:
    if f(x) == 0:
        a.add(x)
print(len(a))


# Верный ответ: 96. Полученный аналитическим способом решения