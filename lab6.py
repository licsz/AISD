#Вариант 27. У юноши P пиджаков, B брюк, R рубашек, G галстуков. Составьте все возможные костюмы из этих предметов.
# Усложнить: Если вес одежды больше 4 у.е. то пиджак не нужен

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



list1 = {"штаны - 'бухта'": 2, "черные джинсы": 3, ",бриджи": 1, "Штаны - спорт": 1.5, "Брюки неглаженные": 2, "Штаны спец.одежды": 3, "Штаны зимнего комбинезона": 4}
list2 = {"рубашка белая класическая": 1.8, "футболка - airborn": 1, "майка - 'алкоголичка'":0.7, "Рубашка фирменная 'STIHL'":2, "Рубашка с короткими рукавами": 1.3, "футболка с воротником":1.5,
         "кофта серая": 2}
list3 = {None: 0, "Пиджак 'Мажор'": 2, "Ветровка": 1.5, "Куртка осенняя длинная": 3.1}
list4 = {None: 0, "cиний":0.1, "красный в клетку":0.1,"длинный и синий":0.3}

start_time = time.perf_counter()
result = []
for l1 in list1.keys():
    for l2 in list2.keys():
        for l3 in list3.keys():
            for l4 in list4.keys():
                result.append(Outfit(l1,l2,l3,l4))
end_time = time.perf_counter()
result_time1 = end_time - start_time

it = 0
for i in result:
    it+=1
    print(it, " ",i)
del result

print("______________________________________________________________")
print("______________________________________________________________")
start_time = time.perf_counter()
combinations = product(list1.keys(), list2.keys(), list3.keys(), list4.keys())
results = [Outfit(*combo) for combo in combinations]
end_time = time.perf_counter()
result_time2 = end_time - start_time

it = 0
for i in results:
    it+=1
    print(it, " ",i)
result = []

print("______________________________________________________________")
print("______________________________________________________________")


start_time = time.perf_counter()
result = []
for key1, value1 in list1.items():
    for key2, value2 in list2.items():
        for key4, value4 in list4.items():
            if value1+value2+value4 <= 4:
                for key3 in list3.keys():
                    result.append(Outfit(key1, key2, key3, key4))
            else:
                    result.append(Outfit(key1, key2, None, key4))

end_time = time.perf_counter()
result_time3 = end_time - start_time
it = 0
for i in result:
    it+=1
    print(it, " ",i)
result = []

print("______________________________________________________________")
print("______________________________________________________________")

print(result_time1)
print(result_time2)
print(result_time3)
