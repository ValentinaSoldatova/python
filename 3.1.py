def division(*args):

    try:
        a = int(input("Введите делимое "))
        b = int(input("Введите делитель "))
        res = a / b
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Ошибка. На ноль делить нельзя"

    return res



print(f'res  {division()}')