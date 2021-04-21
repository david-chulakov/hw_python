def what_the_season(month_num):
    seasons = {
        'зима': [1, 2, 12],
        'весна': [3, 4, 5],
        'лето': [6, 7, 8],
        'осень': [9, 10, 11]
    }

    for key in seasons:
        if month_num in seasons[key]:
            answer = key

    return answer

if __name__ == '__main__':
    month_num = int(input('Введите номер месяца '))
    print(what_the_season(month_num))

