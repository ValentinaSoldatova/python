a = abs(int(input("Введите целое положительное число ")))
max_num = a % 10
while a >= 1:
    a = a % 10
    if a % 10 > max_num:
        max_num = a % 10
    if a > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max_num)
        break
