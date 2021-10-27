from sys import argv

script_name, productivity,  rate, prize = argv
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", productivity)
print("Ставка в часах: ", rate)
print("Премия: ", prize)
print("Зарплата равна: ", int(productivity) * int(rate) + int(prize))

