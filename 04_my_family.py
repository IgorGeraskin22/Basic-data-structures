#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Игорь', 'Юля', 'Алексей', 'Даша', 'Илья']

# список списков приблизителного роста членов вашей семьи
# my_family_height = []
# ['имя', рост],
my_family_height = [['Игорь', 175], ['Юля', 165], ['Алексей', 190], ['Даша', 155], ['Илья', 180]]
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
h = (my_family_height[0][1])
print('Рост отца -', h, 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
# Операторы лучше переносить на новую строку. Так код становится более читаемым.
height_families = (
        my_family_height[0][1]
        + my_family_height[1][1]
        + my_family_height[2][1]
        + my_family_height[3][1]
        + my_family_height[4][1]
)

print('Общий рост моей семьи -', height_families, 'см')

# зачет!