# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа
# запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(var_1, var_2):
     try:
        n = var_1 / var_2
        return n
     except ZeroDivisionError:
         return "На ноль делить нельзя!"

print(f"Результат:", my_func(int(input("Введите делимое: ")), int(input("Введите делитель: "))))