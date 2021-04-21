my_list = [7, 5, 3, 2, 0]
print(f'Изначальный массив {my_list}')
while True:
    number = int(input("Введите следующее число "))
    for i in range(len(my_list)):
        if my_list[i] > number:
            continue
        else:
            my_list.insert(i, number)
            break
    print(f'Пользователь ввел число {number}. Результат {my_list}')
