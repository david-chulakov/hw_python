cash_in = int(input("Введите выручку: "))
cash_out = int(input("Введите издержки: "))
if cash_in > cash_out:
    print(f"Ваша прибыль = {cash_in - cash_out} :)")
    print(f"Рентабельность = {round(cash_in / (cash_in - cash_out), 2)}")
    number = int(input("Введите кол-во сотрудников: "))
    print(f"Прибыль в расчете на одного сотрудника = {(cash_in - cash_out) / number}")
else:
    print(f"Ваш убыток = {cash_out - cash_in} :c ")
