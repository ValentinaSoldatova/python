class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.d = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма d1 и d2 равна:')
        return f'd = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение d1 и d2 равно:')
        return f'd = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'd = {self.a} + {self.b} * i'


d_1 = ComplexNumber(5, 4)
d_2 = ComplexNumber(-6, 8)
print(d_1)
print(d_1 + d_2)
print(d_1 * d_2)
