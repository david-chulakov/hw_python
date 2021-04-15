def max_digit(num):
    max = 0
    while num != 0:
        digit = num % 10

        if digit > max:
            max = digit

        num = num // 10
    return f"Наибольшая цифра в числе = {max}"

if __name__ == "__main__":
    number = int(input("Введите целое число: "))
    print(max_digit(number))