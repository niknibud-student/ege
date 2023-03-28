def win(s1:int, s2: int, m: int) -> bool:
    """Определяет наличие стратегии при заданном количестве камней в двух кучах и номере хода

    Args:
        s1 (int): количество камней в первой куче
        s2 (int): количество камней в второй куче
        m (int): номер хода (Нечетные - Петя, Четные - Ваня)

    Returns:
        bool: есть или нет стратегии
    """
    if s1 + s2 >= 45:
        return m % 2 == 0
    if m == 0:
        return 0
    next_win = [win(s1+1, s2, m-1), win(s1, s2+1, m-1), win(s1*3, s2, m-1), win(s1, s2*3, m-1)]
    return any(next_win) if (m-1) % 2 == 0 else all(next_win)


print(f'19) {[s for s in range(1, 41) if win(4, s, 2)]}')  # Неудачный ход Пети - min значение 5 all->any
print(f'20) {[s for s in range(1, 41) if not win(4, s, 1) and win(4, s, 3)]}')
print(f'21) {[s for s in range(1, 41) if not win(4, s, 2) and win(4, s, 4)]}')