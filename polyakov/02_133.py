print('x y z')
k = 0, 1
for x in k:
    for y in k:
        for z in k:            
            # print(x, y, z, w)
            if (not(x) and y and z) or (not(x) and not(z)):
                print(x, y, z)
