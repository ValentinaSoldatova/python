class Error:
    def __init__(self, *args):
        self.my_list = []

    def mylist(self):
        while True:
            try:
                val = int(input('Просьба ввести значения: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Введенные данные не числовые!")
            else:
                    print(try_except.mylist())

try_except = Error(1)
print(try_except.mylist())