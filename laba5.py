#27 F(1) = 1; F(2) = 2; F(n) = (-1)n*(F(n-1)- F(n-2) /(2n)!) при n > 2.
import math
import time
import matplotlib.pyplot as plt

def print_mat(mat,discription): #Вывод матрицы c Наименованием
    plt.matshow(mat)
    plt.title(discription)
    plt.colorbar()
    plt.show()
def F_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return (-1) ** (n * (F_recursive(n-1) - F_recursive(n-2)) / math.factorial(2*n))

def F_iterative(n):
    temp_1 = 0
    temp_2 = 0
    for i in range(1, n+1):
        if i == 1:
            temp_1 = 1
        elif i == 2:
            temp_2 = 2
        elif i % 2 == 1 and i != 1:
            temp_1 = (-1) ** (n * (temp_2 - temp_1) / math.factorial(2*i))
        elif i % 2 == 0 and i != 2:
            temp_2 = (-1) ** (n * (temp_1 - temp_2) / (math.factorial(2*i)))
    if n % 2 == 1:
        return temp_1
    else:
        return temp_2

data1 = []
data2 = []
execution_time_recursive = 0
execution_time_iterative = 0
time_reaction = float(input("Введите макс время реакции "))
iteration = 0
count_sim = 0
while max(execution_time_recursive, execution_time_iterative) < time_reaction:
    iteration += 1
    start_time = time.time()
    result = F_recursive(iteration)
    end_time = time.time()
    execution_time_recursive = end_time - start_time
    data1.append((iteration, execution_time_recursive))
    print("Тест рекурсия ", "Результат выполнения: ", result, " Время выполения: ", execution_time_recursive)

    start_time = time.time()
    result = F_iterative(iteration)
    end_time = time.time()
    execution_time_iterative = end_time - start_time
    data2.append((iteration, execution_time_iterative))
    print("Тест итерационно ", "Результат выполнения: ", result, " Время выполения: ", execution_time_iterative)
    if execution_time_recursive == execution_time_iterative:
        count_sim += 1
x1, y1 = zip(*data1)
x2, y2 = zip(*data2)
print_mat([x1,y1], "Тест рекурсия")
print_mat([x2,y2], "Тест итерационно")

# построение графика
plt.plot(x1, y1, label='Тест рекурсия')
plt.plot(x2, y2, label='Тест итерационно')

# добавление легенды
plt.legend()
# добавление заголовка и меток осей
plt.title('График зависимости')
plt.xlabel('Ось X, кол-во итераций')
plt.ylabel('Ось Y, Время выполения')
# вывод графика на экран
plt.show()

print("Количество итераций с одинаковым результатом по времени: ", count_sim)