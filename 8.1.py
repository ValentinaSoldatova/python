from datetime import date

class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Формат даты не верный!'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return (data)
        except ValueError:
            return 'Формат даты не верный!'


print(Data.valid('27-09-1983'))
print(Data.type('27-09'))
