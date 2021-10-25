#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

proceeds = float(input("Сумма выручки: "))
costs = float(input("Сумма издержек:"))

if proceeds >= costs:

    print(f"В исследуемом периоде предприятие безубыточно.")

    profitability = proceeds / costs

    print(f"Рентабельность {profitability:.2f} рубля(-ей)")

    workers = int(input("Введите численность сотрудников: "))
    profit = proceeds - costs

    print(f"Прибыль в расчете на одного сторудника составила {profit / workers:.2f} рубля(-ей)")
else:
    print("Предприятие убыточно")