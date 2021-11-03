from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Необходимо ткани на сумму: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Очень абстрактно'


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Вещь очень абстрактна'


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(600)
costume = Costume(180)
print(coat.consumption)
print(costume.consumption())
print(coat.abstract())

