def win(s: int, m: int) -> bool:
    """Определяет наличие стратегии при заданном количестве камней и номере хода

    Args:
        s (int): количество камней
        m (int): номер хода (Нечетные - Петя, Четные - Ваня)

    Returns:
        bool: есть или нет стратегии
    """
    if 45 <= s <= 112:
        return m % 2 == 0
    if s > 112:
        return m % 2 != 0
    if m == 0:
        return 0
    next_win = [win(s+2, m-1), win(s*3, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)


print(f'19) {[s for s in range(1, 45) if win(s, 2)]}')  
print(f'20) {[s for s in range(1, 45) if not win(s, 1) and win(s, 3)]}')
print(f'21) {[s for s in range(1, 45) if not win(s, 2) and win(s, 4)]}')