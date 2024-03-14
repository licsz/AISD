import numpy as np
from matplotlib import pyplot as plt
n = int(input("Введите размер массива "))
k = int(input("Введите коэф. k "))
A = np.random.randint(-10, 11, size=(n, n))  # создание массива
F = A.copy()
print(A, "\n")
def conect_mat(mat, mat1, mat2, mat3, mat4):
    result = mat
    for i,i1 in zip(range(len(mat)//2), range(len(mat1))):
        for j,j1 in zip(range(len(mat)//2), range(len(mat1))):
            result[i][j] = mat1[i1][j1]
    for i,i1 in zip(range(len(mat)//2), range(len(mat2))):
        for j,j1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat2))):
            result[i][j] = mat2[i1][j1]
    for i,i1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat3))):
        for j,j1 in zip(range(len(mat)//2), range(len(mat3))):
            result[i][j] = mat3[i1][j1]
    for i,i1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat4))):
        for j,j1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat4))):
            result[i][j] = mat4[i1][j1]
    return result
def print_mat(mat,discription):
    plt.matshow(mat)
    plt.title(discription)
    plt.colorbar()
    plt.show()

size = len(A)//2
if len(A)%2 == 0:
    B = A[:size, :size]
    C = A[:size, size:]
    D = A[size:, :size]
    E = A[size:, size:]
else:
    B = A[:size, :size]
    C = A[:size, size+1:]
    D = A[size+1:, :size]
    E = A[size+1:, size+1:]

print_mat(A,"Матрица A:\n")
print_mat(B,"Матрица B:\n")
print_mat(C,"Матрица C:\n")
print_mat(D,"Матрица D:\n")
print_mat(E,"Матрица E:\n")
perimeter_e = np.concatenate((E[0, :], E[1:-1, -1], E[-1, ::-1], E[1:-1, 0][::-1])).tolist()

if sum(perimeter_e) > perimeter_e.count(0):
    (B, C) = (np.flip(C, axis=1), np.flip(B, axis=1))
else:
    (B, E) = (E, B)
F = conect_mat(F, B, C, D, E)
print(F, "\n")
print_mat(F,"Матрица F:\n")
diagonal_sum = np.trace(F) + np.trace(np.fliplr(F))
if np.linalg.det(A) > diagonal_sum:
    result = np.dot(A, np.transpose(A)) - k * F
    discription = "A*AT – K * F"
else:
    result = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F)) * k
    discription = "(A-1 +G-F-1)*K"

print_mat(result, discription)