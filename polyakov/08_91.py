a = 'КАЛИЙ'
a1 = 'КАЛИ'
cnt = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i + j + k + l + m
                    if (not 'ИА' in s) and (s.count('К') == 1) and (s.count('А') == 1) and (s.count('Л') == 1) and (s.count('И') == 1) and (s.count('Й') == 1):
                        cnt += 1
print(cnt)
