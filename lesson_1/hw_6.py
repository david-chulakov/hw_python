def func(a, b):
    counter = 1
    print(f"{counter}-й день: {a} км")
    while b > a:
        a = a + a * 0.1
        counter += 1
        print(f"{counter}-й день: {round(a, 2)} км")
    return print(f"На {counter}-й день спортсмен достиг результата - не менее {round(a, 2)} км ")

if __name__ == '__main__':
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    print(func(a, b))