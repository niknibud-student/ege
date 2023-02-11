'''
Функции для решения заданий №8

'''

def convert(place: int, letters: str, len_word: int) -> str:
    '''Функция определяет слово, стоящеее на определеном месте'''
    sys = len(letters)  # Определяем систему счисления
    num = place - 1
    n_sys = []
    while num > 0:
        n_sys.insert(0, num % sys)
        num //= sys
    n_sys = [0] * (len_word - len(n_sys)) + n_sys
    return ''.join([letters[x] for x in n_sys])




if __name__ == '__main__':
    place = int(input('Позиция слова: '))
    letters = input('Буквы слов: ')
    len_word = int(input('Длина слов: '))
    print(convert(place, letters, len_word))
