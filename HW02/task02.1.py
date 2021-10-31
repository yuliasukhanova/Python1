# 1 Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = []

my_list.extend([1, 2, 3, 4.56, 'string', '', b'bytes', bytearray(b'barray'), {'daytime': 'evening'}, {1, 2, 1, 3}, None, True])

for item in my_list:
    item_type = type(item)

    print(f"{item} is type({item_type})")
