from itertools import combinations, product

lst = [int(''.join(x)) for x in list(product('0123456789', repeat=5)) if int(''.join(x)) % 5 == 0 and x[0] != '0']

print(len(lst))