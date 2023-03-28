def win(s: int, m: int) -> bool:
    """Определяет наличие стратегии при заданном количестве камней и номере хода

    Args:
        s (int): количество камней
        m (int): номер хода (Нечетные - Петя, Четные - Ваня)

    Returns:
        bool: есть или нет стратегии
    """
    if s >= 25:
        return m % 2 == 0
    if m == 0:
        return 0
    next_win = [win(s+2, m-1), win(s*2, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)

# for s in range(1, 25):
#     if win(s, 2):
#         print(19, s)
#         break

print(f'19) {min([s for s in range(1, 25) if win(s, 2)])}')  # мин S Ваня выиграет 1-м ходом (m=2)
print(f'20) {len([s for s in range(1, 25) if not win(s, 1) and win(s, 3)])}')  # Количество значений S при (not m=1 and m=3), ходы Пети
print(f'21) {[s for s in range(1, 25) if not win(s, 2) and win(s, 4)]}')  # 2 значения S, есть выигрышная стратегия Ваня при (not m=2 and m=4)