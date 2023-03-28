def win(s1, s2, m):
    if s1 == s2:
        return m % 2 == 0
    if m == 0:
        return 0
    if s1 < s2:
        next_win = [win(s1+1, s2, m-1), win(s1+3, s2, m-1)]
    else:
        next_win = [win(s1, s2+1, m-1), win(s1, s2+3, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)

print(f'19) {[s for s in range(1, 24) if not win(13, s, 0) and win(13, s, 2)]}') # для 21 all -> any и вывод 19 сравнить 21
print(f'20) {[s for s in range(1, 24) if not win(13, s, 1) and win(13, s, 3)]}')
print(f'21) {[s for s in range(1, 24) if not win(13, s, 2) and win(13, s, 4)]}')

# 19) [9, 11, 15, 17] - 9
# 20) [6, 8, 18, 20] - 6, 8
# 21) [5, 7, 19, 21] - 7, 19, т.к. при 5 у Вани нет стратегии для выигрыша своим первым ходом