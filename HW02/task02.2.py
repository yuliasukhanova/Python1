# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
# на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

my_list = []

elements = 5
x = 0

while x < elements:
    my_list.append(input("Введите элемент списка: "))
    x += 1

print(f"Сформирован список: {my_list}")

idx = 0

for idx in range(
        int(
            len(my_list) / 2
        )):
    my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
    idx += 2

print(f"После обмена индексами соседними значениями: {my_list}")
