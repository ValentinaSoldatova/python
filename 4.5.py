my_list = [el for el in range(100, 1001) if el % 2 ==0]
print(my_list)
from functools import reduce
def my_function(el_prev, el):
    return el_prev* el
print(reduce(my_function, my_list))