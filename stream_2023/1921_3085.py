def win(s1:int, s2: int, m: int) -> bool:
    if s1 + s2 <= 20:
        return m % 2 == 0
    if m == 0:
        return 0
    next_win = [win(s1-1, s2, m-1), win(s1, s2-1, m-1), win((s1+1)//2, s2, m-1), win(s1, (s2+1)//2, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)


print(f'19) {[s for s in range(11, 1000) if win(10, s, 2)]}')
print(f'20) {[s for s in range(11, 1000) if not win(10, s, 1) and win(10, s, 3)]}')
print(f'21) {[s for s in range(11, 1000) if not win(10, s, 2) and win(10, s, 4)]}')