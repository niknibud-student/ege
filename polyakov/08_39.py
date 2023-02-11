a = 'ABCDX'
cnt = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                s = i + j + k + l
                if s.count('X') == 1:
                    cnt += 1
print(cnt)