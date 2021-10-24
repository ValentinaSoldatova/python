from itertools import count
from math import factorial
def factgen():
    for el in count(1):
        yield factorial(el)
gen = factgen()
n = 0
for elem in gen:
    if n < 10:
        print(elem)
        n += 1
    else:
        break