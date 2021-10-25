#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Enter number: ")
number2 = int(number+number)
number3 = int(number+number+number)
amount = int(number) + number2 + number3

print(f"{number} + {number2} + {number3} = {amount}")
