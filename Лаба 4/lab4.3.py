# Вычислить значение суммы F1 и F2 для диапазона аргументов х.
# Шаг по х принять 0.1 для обычных функций и 0,05π если диапазон х задан в долях π.
# Примечание. Учитывать вероятность возникновения ошибок при вычислениях.

import math
import decimal


def F1(x, z, y, l):
    if y ** 2 < -1 or y ** 2 > 1:
        print('Ограничение арккосинуса')
        return
    if (z ** 2 + x * y) ** 2 == 0:
        print("Деление на ноль")
        return

    result = decimal.Decimal(l ** (2 * x ** 2 - y) + (3 * math.cos(y ** 2)) / ((z ** 2 + x * y) ** 2))
    return result


def F2(x, z, y):
    if (3 * z + math.cos(x ** 2)) == 0:
        print("Деление на ноль")
        return

    result = decimal.Decimal(math.tan((abs(x - y) ** 2) / (3 * z + math.cos(x ** 2))))
    return result


start = 6
end = 9
i = 0.1

X = start
# Y = 7
Y = 0.5
L = 2
Z = 8

# пришлось использовать decimal, так как ответ был за пределами точности диапазона float
decimal.getcontext().prec = 100
while X <= end:
    result_1 = F1(x=X, y=Y, z=Z, l=L)
    result_2 = F2(x=X, z=Z, y=Y)

    if result_1 is None or result_2 is None:
        X += i
        continue

    sum_result = result_1 + result_2
    print(f"x = {X:.1f}, F1 = {result_1:.2f}, F2 = {result_2:.5f}, Сумма = {sum_result:.2f}")
    X += i
