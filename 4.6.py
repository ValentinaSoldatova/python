def my_func1():
    a = int(input('Введите начальное число: '))
    from itertools import islice
    from itertools import count

    for i in islice(count(a), 10):
        print(i)
my_func1()

def my_func2():
    list = [5, 305, 1002, 2018]

    from itertools import islice
    from itertools import cycle

    for el in islice(cycle(list), 15):
        print(el)
my_func2()