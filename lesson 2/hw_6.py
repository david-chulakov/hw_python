
def create_analytics(list_products):
    for tup in list_products:
        for i in range(len(tup)):
            tup[1]


if __name__ == "__main__":
    list_products = []
    counter = int(input("Введите кол-во товаров "))
    number = 1
    while counter != 0:
        name = input("Введите название ")
        price = int(input("Введите цену "))
        count = int(input("Введите количество "))
        measure = input("Введите единицу измерения ")
        create_tuple(number, name, count, measure)
        number += 1
        counter -= 1
        list_products.append((number, {'название': name, 'цена': price, 'количество': count, 'ед.': measure}))

