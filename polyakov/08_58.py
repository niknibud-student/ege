a = 'ПИРОГ'
a1 = 'ПИРГ'
cnt = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                s = i + j + k + l
                if (s.count('Е') <= 2) and (not 'ИО' in s) and (not 'ОО' in s):
                    cnt += 1
print(cnt)
