def my_sum ():
    sum_res = 0
    num = False
    while num == False:
        number = input('Введите строку чисел через пробел ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                num = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Текущая сумма равна  {sum_res}')
    print(f'Финальная сумма равна  {sum_res}')


my_sum()
