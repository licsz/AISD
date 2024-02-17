#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
#распознает, преобразует и выводит на экран лексемы по определенному правилу. Лексемы разделены пробелами. Преобразование делать
#по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
#Регулярные выражения использовать нельзя.
#Вариант 27.
#Шеснадцатиричные нечетные числа, не превышающие 409610 и содержащие более К цифр.
#Вывести числа и их количество. Минимальное число вывести прописью.

def convert_hex_to_dec(number):
    digits = '0123456789abcdef'
    result = 0
    position = 1
    for i in number[::-1]:
        result += position * digits.find(i)
        position *= 16
    return result


k = int(input("Введите число К = "))
file = open('text.txt', 'r')
a = ""
mas = []
mas_dict = {}


for i in file:
    a +=i
mas = a.split(' ')
for i in mas:
    mas_dict[i] = mas_dict.get(i, 0)+1

mas_dict_result = {}



for i in mas_dict.keys():
    if len(i) > k:
        temp_dec = convert_hex_to_dec(i)
        if temp_dec % 2 == 1 and temp_dec <= 4096:
            mas_dict_result[i] = mas_dict.get(i)

del mas_dict
dec_mas = {}
for i in mas_dict_result.keys():
    dec_mas[convert_hex_to_dec(i)] = i

print("число | кол-во")
min = dec_mas.get(min(dec_mas.keys()))
for i in mas_dict_result:
    print(i+" | " + str(mas_dict_result.get(i)))

print('минимальное число = '+min)
