#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

firstname = input("Введите Имя --> ")
lastname = input("Введите Фамилию --> ")
inn = int(input("Введите номер ИНН --> "))
snils = int(input("Введите номер СНИЛС --> "))

print(f"Уважаемый(-ая) {firstname} {lastname}! Ваш номер ИНН {inn}, СНИЛС {snils}.")