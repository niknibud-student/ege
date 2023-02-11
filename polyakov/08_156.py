even = '02468'
odd = '13579'
cnt = 0
m = '5'
for i in odd:
    for j in even:
        for k in odd:
            for l in even:
                s = i + j + k + l + m
                if (s.count('0') <= 1) and (s.count('1') <= 1) and (s.count('2') <= 1) and (s.count('3') <= 1) and (s.count('4') <= 1) and (s.count('5') <= 1) and (s.count('6') <= 1) and (s.count('7') <= 1) and (s.count('8') <= 1) and (s.count('9') <= 1):
                    cnt += 1
m = '0'
for i in even:
    for j in odd:
        for k in even:
            for l in odd:
                s = i + j + k + l + m
                if (s.count('0') <= 1) and (s.count('1') <= 1) and (s.count('2') <= 1) and (s.count('3') <= 1) and (s.count('4') <= 1) and (s.count('5') <= 1) and (s.count('6') <= 1) and (s.count('7') <= 1) and (s.count('8') <= 1) and (s.count('9') <= 1):
                    cnt += 1

print(cnt)
