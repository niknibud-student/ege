# Аналитическое решение. Анализируем формулу
def f(n):
    if n <= 10 and n % 2 == 0:
        return -1
    if n <= 10 and n % 2 != 0:
        return 1
    return f(n-1) + 3*f(n-3) + 2

print(f(20))