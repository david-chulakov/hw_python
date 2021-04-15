def calculate(a):
    return a + a * 11 + a * 111

if __name__ == '__main__':
    n = int(input("Введите n: "))
    print(calculate(n))