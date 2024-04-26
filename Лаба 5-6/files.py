import itertools


def count_valid_grids():
    count = 0
    digits = range(10)  # Возможные цифры от 0 до 9
    total_combinations = 10 ** 16  # Общее количество комбинаций

    for i, grid in enumerate(itertools.product(digits, repeat=16)):
        if i % (total_combinations // 10) == 0:
            progress = (i / total_combinations) * 100
            print(f"Прогресс: {progress:.0f}%")

        grid = [grid[i:i + 4] for i in range(0, 16, 4)]  # Преобразование списока в сетку 4x4

        # Проверка условия суммы для каждой строки, столбца и диагонали
        if all(sum(row) == 12 for row in grid) and \
           all(sum(col) == 12 for col in zip(*grid)) and \
           sum(grid[i][i] for i in range(4)) == 12 and \
           sum(grid[i][3-i] for i in range(4)) == 12:
            count += 1

    return count


# Вызываем функцию и выводим результат
result = count_valid_grids()
print(f"Количество способов заполнить сетку: {result}")
