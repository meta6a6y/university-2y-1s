# №17 Задать 5 наборов по 6 случайных карт в виде сетов в формате «масть-номинал». Где «масть» =
# кодируется буквами П,Ч,Т,Б, «номинал» = 6,7,8,9,А,В,Д,К,Т.
# a. Определить, в каких наборах есть пиковая дама (ПД)
# b. Найти карты, которые не входят ни в один из наборов.
# c. Заменить во всех наборах карты с номиналом 6 на джокеров ("J")
# d. Определить, имеют ли общие карты наборы 1 и 2.

import random


def vse_cards():
    suits = {'П', 'Ч', 'Т', 'Б'}
    ranks = {'6', '7', '8', '9', 'А', 'В', 'Д', 'К', 'Т'}

    deck = {(suit + rank) for suit in suits for rank in ranks}
    return deck


deck = vse_cards()


# Функция для генерации случайной карты
def generate_card():
    suits = ('П', 'Ч', 'Т', 'Б')
    ranks = ('6', '7', '8', '9', 'А', 'В', 'Д', 'К', 'Т')
    mast = random.choice(suits)
    nom = random.choice(ranks)
    return mast + nom


# 5 наборов по 6 случайных карт
nabors = []
using_cards = set()
for _ in range(5):
    nabor = set()
    while len(nabor) < 6:
        card = generate_card()
        nabor.add(card)
        using_cards.add(card)
    nabors.append(nabor)
# print(len(all_cards))

# Вывод наборов карт
for i, nabor in enumerate(nabors, 1):
    print(f"Набор {i}: {nabor}")
print('\n')

# a.Пиковая дама
print("Поиски пиковой дамы.")
cards_not_found = ()
for i, nabor in enumerate(nabors, 1):
    if 'ПД' in nabor:
        print(f"В наборе {i} есть пиковая дама!")
    else:
        print(f"В наборе {i} нет пиковой дамы.")
print('\n')

# b.Не входят ни в один набор
b = vse_cards() ^ using_cards
# print(len(b))
print("Карты, которые не входят ни в один набор:", b)
print("\n")
# print(all_cards)
# print(len(vse_cards()))

# c.6 == J
count_of_six = 0
for i, nabor in enumerate(nabors, 1):
    for card in list(nabor):
        if '6' in card:
            nabor.discard(card)
            nabor.add("J")
            count_of_six += 1

    if count_of_six == 0:
        print(f'В наборе {i} нет шестерок')
    else:
        count_of_six = 0
print('\n')
# Вывод наборов карт
for i, nabor in enumerate(nabors, 1):
    print(f"Набор {i}: {nabor}")

# d.Общие карты 1 и 2
union_nabors = nabors[0] & nabors[1]
if union_nabors == set():
    print('\nОбщих карт нет.')
else:
    print(f'\nОбщие карты 1 и 2 набора: {union_nabors}')
