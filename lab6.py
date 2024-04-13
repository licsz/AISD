#Вариант 27. У юноши P пиджаков, B брюк, R рубашек, G галстуков. Составьте все возможные костюмы из этих предметов.


import time
from itertools import product
class Outfit:
    pants = None
    shirt = None
    jacket = None
    tie = None

    def __init__(self, pants, shirt, jacket = None, tie = None):
        self.pants = pants
        self.shirt = shirt
        self.jacket = jacket
        self.tie = tie

    def __str__(self):
        return f"Outfit: pants - {self.pants},shirt - {self.shirt}, jacket - {self.jacket}, tie - {self.tie}"



list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4]
list3 = [None, 1, 2, 3]
list4 = [None, 1, 2, 3, 4, 5]

start_time = time.perf_counter()
result = []
for l1 in list1:
    for l2 in list2:
        for l3 in list3:
            for l4 in list4:
                result.append(Outfit(l1,l2,l3,l4))
end_time = time.perf_counter()
result_time1 = end_time - start_time

for i in result:
    print(i)
del result

print("______________________________________________________________")
print("______________________________________________________________")
result =[]
start_time = time.perf_counter()
combinations = product(list1, list2, list3, list4)
results = [Outfit(*combo) for combo in combinations]
end_time = time.perf_counter()
result_time2 = end_time - start_time

for i in results:
    print(i)
result = []


print(result_time1)
print(result_time2)
