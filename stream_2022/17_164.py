# Изменная на стриме на поиск минимальной суммы
a = [int(x) for x in open('17-3.txt')]
cond = lambda x, y, z: x*y*z%7 == 0 and abs(x+y+z)%10 == 5
ans = [(a[i]+a[i+1]+a[i+2]) for i in range(len(a)-2) if cond(*a[i:i+3])]
print(len(ans), min(ans))
# Ответ на стриме: 153 -25085