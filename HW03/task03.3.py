# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    summ = max(arg_1, arg_2, arg_3) + max(min(arg_1, arg_2), min(arg_1, arg_3), min(arg_2, arg_3))
    return summ

print(my_func(3, 5, 10))
