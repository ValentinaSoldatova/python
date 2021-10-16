my_ratings = [7, 5, 3, 3, 2]

while True:
    number = input('Введите новое значение рейтинга: ')

    try:
        number = abs(int(number))
    except ValueError as e:
        print('Ошибка ввода')
        continue

    if not my_ratings.count(number):

        if number > my_ratings[0]:
            my_ratings.insert(0, number)
        elif number < my_ratings[-1]:
            my_ratings.append(number)

        else:
            for k, v in enumerate(my_ratings):
                if number > v:
                    my_ratings.insert(k, number)
                    break
    else:
        new_index = my_ratings.index(number) + my_ratings.count(number)
        my_ratings.insert(new_index, number)

    print(my_ratings)
