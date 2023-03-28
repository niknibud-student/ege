def win(s1:int, s2: int, m: int) -> bool:
    if s1 + s2 >= 231:
        return m % 2 == 0
    if m == 0:
        return 0
    next_win = [win(s1+2, s2, m-1), win(s1, s2+2, m-1), win(s1*2, s2, m-1), win(s1, s2*2, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)

print(f'19) {max([s for s in range(1, 214) if win(17, s, 2)])}') # all -> any
print(f'20) {[s for s in range(1, 214) if not win(17, s, 1) and win(17, s, 3)]}')
print(f'21) {min([s for s in range(1, 214) if not win(17, s, 2) and win(17, s, 4)])}')

# 19) 211
# 20) 53, 105
# 21) 96