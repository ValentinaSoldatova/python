import random
list1 = random.sample(range(1, 1000), 10)
print(list1)
list2 = []
for el in range(len(list1) - 1):
    if list1[el] < list1[el+1]:
        list2.append(list1[el+1])
print(list2)