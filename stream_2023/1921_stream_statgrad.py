def win(s, m):
    if s >= 41:
        return m % 2 == 0
    if m == 0:
        return 0
    next_win = [win(s+1, m-1), win(s+2, m-1)]
    if s <= 25:
        next_win += [win(s*2, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)

print(f'19) {[s for s in range(1, 40) if not win(s, 2) and win(s, 4)]}')
print(f'20) {[s for s in range(1, 40) if not win(s, 4) and win(s, 6)]}')
print(f'21) {[s for s in range(1, 40) if not win(s, 1) and win(s, 3)]}')
print(f'21*) {[s for s in range(1, 40) if not win(s, 0) and win(s, 2)]}')


# 19) [35]
# 20) [17, 32]
# 21) [10, 18, 19, 36, 37] ответ 19, из него можно попасть в 20 (+1) и 38 (*2)
# 21*) [20, 38]