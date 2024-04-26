# Составить программу, которая по заданному числу (1 – 7) выводит название соответствующего ему дня
# недели на русском или английском языке.

def get_day_name(num_day, language):
    if language == '1':
        days = {
            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье'
        }
    else:
        days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }

    return days.get(num_day, 'Ошибка! Введите число 1-7')


num_day = int(input('Введите номер дня недели (1-7): '))
language = input('Выберите язык русский(1) или английский(0): ')

name_day = get_day_name(num_day, language)
print('Название дня недели:', name_day)
