number= int(input("Введите целое число от 1 до 12 (номер месяца):"))
seasons= {"winter": (1, 2, 12), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
for key in seasons.keys():
    if number in seasons[key]:
        print(key)
