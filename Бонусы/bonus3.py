def is_reversible(number):
    reverse_number = int(str(number)[::-1])  # Обратное число
    sum_digits = number + reverse_number  # Сумма числа и его обратного числа
    digits = all(int(digit) % 2 != 0 for digit in str(sum_digits))  # Сумма только из нечетных цифр
    return digits


count = 0
limit = 1000000000

for number in range(1, limit):
    if number % 10 != 0 and is_reversible(number):  # Исключаем числа, оканчивающиеся на 0
        count += 1

print(f"Количество обратимых чисел меньше {limit}: {count}")
