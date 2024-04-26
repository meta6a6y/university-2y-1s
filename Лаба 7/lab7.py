# 18. Создать единичную матрицу А(3×3) и матрицу В(3×2), заполненную числами 5.
# Объединить их в массив С(3×5)
import numpy as np
import scipy.optimize as opt

A = np.eye(3)
print('Единичная матрица:\n', A)

B = np.full((3, 2), 5)
print('\nМатрица из чисел 5:\n', B)

C = np.concatenate((A, B), axis=1)
print('\nОбъединение матриц в массив:\n', C)

# 4. Создать массив целых чисел размерностью 2×3×4 заполненный числами 2.
# Переразмерить его в 4×2×3

array = np.full((2, 3, 4), 2, dtype=int)
print('\nМассив из целых чисел:\n', array)
array2 = array.T
# array2 = array.reshape(4, 2, 3)   # или так
print('\nПерезармещенный массив:\n', array2)

# 15. Найти локальные минимумы функции f = x^2 – 5x + 4
# на различных отрезках: [-1, 1], [-3, 3], [-5, 5]


def f(x: float) -> float:       # f = x^2 – 5x + 4
    return x ** 2 - 5 * x + 4


# Отрезок [-1; 1]
res1 = opt.minimize_scalar(f, bounds=(-1, 1))
print("\nЛокальный минимум на отрезке [-1, 1]:", res1.x)

# Отрезок [-3, 3]
res2 = opt.minimize_scalar(f, bounds=(-3, 3))
print("Локальный минимум на отрезке [-3, 3]:", res2.x)

# Отрезок [-5, 5]
res3 = opt.minimize_scalar(f, bounds=(-5, 5))
print("Локальный минимум на отрезке [-5, 5]:", res3.x)
