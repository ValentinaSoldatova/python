class ZeroDivisionError(Exception):
    def __str__(self):
        return f'На ноль делить нельзя!'
class Del:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dell(self):
        if self.b == 0:
            raise ZeroDivisionError
        else:
            return self.a/self.b
d = Del(8, 0)
try:
    print(d.dell())
except ZeroDivisionError as exeption:
    print("На ноль делить нельзя!")