text = input("Введите слова")
words = text.split()
numerator = 1
for word in words:
    if len(word) > 10:
        print(f'{numerator}. {word[:10]}')
    else:
        print(f'{numerator}. {word}')
    numerator += 1
