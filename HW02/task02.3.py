# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

list = [["зима", ["12", "1", "2"]],
        ["весна", ["3", "4", "5"]],
        ["лето", ["6", "7", "8"]],
        ["осень", ["9", "10", "11"]]]

dict = {'зима': ['12', '1', '2'],
        'весна': ['3', '4', '5'],
        'лето': ['6', '7', '8'],
        'осень': ['9', '10', '11']}

number = input("Введите порядковый номер месяца: ")

for season, month in list:
    if number in month:
        print(f"{number} месяц это {season}")

for season, months in dict.items():
    if number in months:
        print(f"{number} месяц это {season}")
