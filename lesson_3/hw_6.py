def upper_word(word: str) -> str:
    """ Функция делает первую букву заглавной для 1 слова

    word: str
    """
    return word[0].upper() + word[1:]


def upper_text(text: str) -> str:
    """ Функция делает первую букву заглавной для всех слов

    text: str
    """
    text = text.split()
    result = ''
    for word in text:
        result = result + upper_word(word) + ' '
    return result


if __name__ == "__main__":
    print(upper_word(input("Введите слово в нижнем регистре ")))
    print(upper_text(input("Введите слова через пробел в нижнем регистре ")))