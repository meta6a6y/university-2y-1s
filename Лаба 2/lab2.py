# Варианты: 24 8 25 7
# №1 Переводить значение давления, заданного в паскалях (Па), атмосферах (атм.) или мм. ртутного
# столба друг в друга. 1 атм = 101 325 Па = 760 мм. рт. ст.

normal_mm = 760
normal_atm = 1
normal_pa = 101325

pressure_mm0 = 760
pressure_atm0 = (pressure_mm0 * normal_atm) / normal_mm
pressure_pa0 = (pressure_mm0 * normal_pa) / normal_mm
print('Задано в мм. ртутного столба. ({})'.format(pressure_mm0))
print('В Паскалях: {}'.format(pressure_pa0))
print('В Атмосферах: {}'.format(pressure_atm0))

pressure_pa1 = 101326
pressure_mm1 = (pressure_pa1 * normal_mm) / normal_pa
pressure_atm1 = (pressure_pa1 * normal_atm) / normal_pa
print('\nЗадано в Паскалях. ({})'.format(pressure_pa1))
print('В мм. ртутного столба: {}'.format(pressure_mm1))
print('В Атмосферах: {}'.format(pressure_atm1))

pressure_atm2 = 1
pressure_mm2 = (pressure_atm2 * normal_mm) / normal_atm
pressure_pa2 = (pressure_atm2 * normal_pa) / normal_atm
print('\nЗадано в Атмосферах. ({})'.format(pressure_atm2))
print('В мм. ртутного столба: {}'.format(pressure_mm2))
print('В Паскалях: {}'.format(pressure_pa2))

# №2 Задайте две произвольные строки разной длины. Проверьте, имеется ли первая строка во второй.
# Попробуйте заменить имеющийся фрагмент второй строки первой.

fist_line = 'Moscow'
second_line = 'Moscow is a capital of Russia'

if fist_line in second_line:
    second_line = second_line.replace(fist_line, 'Moscow')
    print('\nСтрока после замены:', second_line)
else:
    print('\nПервая строка не содержится во второй.')

# №3 Задайте произвольную строковую переменную s. Соберите из неё в новую строковую
# переменную, используя срезы строки (результаты для строки «Революция!» приведены ниже в
# скобках). Срезы строки без изменений должны работать для любых строк, а не только для
# тестовой (за исключением случаев, когда индексы указаны явно)! Проверить это на примере строки
# «Эту фразу нужно обработать при помощи срезов строки».
# Примечание. Не использовать одиночные символы типа s[1], s[-7] и т.п. Только срезы!
# Символы 1 3 5 4 3 2 (еоюлов)

test = 'Эту фразу нужно обработать при помощи срезов строки'
result = test[0::2]
result = result[0:12]
print('\nТестовая строка:', result)

s = "Революция!"
new_s = s[1:7:2] + s[4::-1]  # или s[4:1:-1] (еоюлов)
new_s = new_s[0:6]
print('\nРеволюция!', new_s)

# №4 Отформатировать строку: "http://somesite.com/request?key1&key2&key3", где вместо key1, key2, key3
# должны быть выведены значения соответствующих целочисленных переменных, каждая из которых
# занимает 5 разрядов. Т.е. если в них содержатся числа 1, 2, 3, то должно быть выведено:
# "http://somesite.com/request?00001&00002&00003"

key1 = 345
key2 = 22
key3 = 6
string = f"http://somesite.com/request?{key1:05d}&{key2:05d}&{key3:05d}"
print('\n' + string)