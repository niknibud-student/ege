cnt = 0
for x in range(1, 1000):
    for y in range(1, 1000):
        f = (((x>6) and ((x+y)>=5)) or (y>=5)) == 0
        if f:
            cnt += 1
print(cnt)