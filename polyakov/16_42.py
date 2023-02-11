dct_f = {}
dct_g = {}
def f(n):
    if n not in dct_f:
        if n == 1:
            dct_f[n] = 1
        else:
            dct_f[n] = f(n-1) + 3 * g(n-1)
    return dct_f[n]

def g(n):
    if n not in dct_g:
        if n == 1:
            dct_g[n] = 1
        else:
            dct_g[n] = f(n-1) - 2 * g(n-1)
    return dct_g[n]

s = f(50)
print(sum(int(d) for d in str(s)))