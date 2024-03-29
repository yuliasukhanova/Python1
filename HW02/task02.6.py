# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
myList = []
n = 1
dict = {}

while True:
    dict = {'name': input("Введите имя: "), 'price': input("Введите стоимость: "),
            'amount': input("Введите количество: "), 'unit': input("Введите единицы измерения: ")}

    myList.append((n, dict))
    n += 1

    q = input('Еще один товар? (y/n)): ')
    if q == 'y':
        break

for item in myList:
    print(item)

names = []
prices = []
amounts = []
units = []
for idx, el in myList:
    names.append(el['name'])
    prices.append(el['price'])
    amounts.append(el['amount'])
    units.append(el['unit'])

print(f"name: {names}, price: {prices}, amount: {amounts}, unit: {units}")
