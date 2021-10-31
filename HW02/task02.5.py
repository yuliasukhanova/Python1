#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
#чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

item = int(input("Введите новый элемент рейтинга: "))

my_list = [7, 5, 3, 3, 2]

count = my_list.count(item)

for element in my_list:
    if count > 0:
        n = my_list.index(item)
        my_list.insert(n+count, item)
        break
    else:
        if item > element:
            n = my_list.index(element)
            my_list.insert(n, item)
            break
        elif item < my_list[len(my_list) - 1]:
            my_list.append(item)
print(my_list)