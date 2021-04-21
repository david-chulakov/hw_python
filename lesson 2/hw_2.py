def list_change(array):
    for i in range(len(array) - 1):
        if i % 2 == 1:
            continue
        array[i], array[i+1] = array[i+1], array[i]
    return array

if __name__ == "__main__":
    some_list = input("Вводите элементы через пробел ").split()
    print(f'Измененный список {list_change(some_list)}')