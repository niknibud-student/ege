a = [int(x) for x in open('17-4.txt')]
# условие стрима
cond = lambda x: (x%16 in (11, 13)) and x%7 == 0 and all(x%y!=0 for y in (6, 13, 19))
# условие по сборнику Полякова
# cond = lambda x: x%16 == 11 and x%7 == 0 and all(x%y!=0 for y in (6, 13, 19))
ans = [x for x in a if cond(x)]
print(sum(ans), len(ans))
# ответ на стриме 159607 27
# ответ по сборнику Полякова 74452 12