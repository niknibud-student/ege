a = 'ЛЕТО'
cnt = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i + j + k + l + m
                    if s.count('Е') > 0: #  'E' in s
                        cnt += 1
print(cnt)
