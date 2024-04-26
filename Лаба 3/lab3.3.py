# №24 Создайте словарь IgorCV = {"Имя": "Игорь", "Возраст": 25, "Желаемая зарплата": 85000, "Город":
# Казань"} из исходных списков ключей и значений.
# a. Изменить желаемую зарплату до 90000
# b. Проверить, есть ли ключ "Возраст" и если нет вывести в консоль «нет»
# c. Вывести все ключи в консоль, упорядочив по убыванию.
# d. Очистить словарь IgorCV.

keys = ['Имя', 'Возраст', 'Желаемая зарплата', 'Город']
values = ['Игорь', 25, 85000, 'Казань']

IgorCV = dict(zip(keys, values))
print(IgorCV)

# a.изменение зарплаты
IgorCV['Желаемая зарплата'] = 90000
print('Изменение желаемой зарплаты:', IgorCV)

# b.есть ли возраст
from collections import defaultdict


def fun():
    return "НЕТ"


IgorCVb = defaultdict(fun)
IgorCVb['Имя'] = 'Игорь'
# IgorCVb['Возраст'] = '25'
IgorCVb['Город'] = 'Казань'
meow = IgorCVb['Возраст']
print(meow)

# c.все ключи по убыванию
all_keys = list(IgorCV.keys())
all_keys.sort(reverse=True)
print('Все ключи:', all_keys)

# d.очистка словаря
IgorCV.clear()
print('Словарь очищен', IgorCV)
