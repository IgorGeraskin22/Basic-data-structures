#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# Решение:
zoo.insert(1, 'bear')  # Вставляем "bear" на первую позицию так как лев на нулевой позиции, а кенгуру
# сдвигается на 2 позицию.
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# Решение:
zoo.extend(birds)  # Расширяем список "zoo"
print(zoo)

# уберите слона
#  и выведите список на консоль
# Решение:
zoo.remove('elephant')  # Удаляем из списка: "elephant"(слон).
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# Решение:
# Определим клетку где сидит лев (lion)
#  Положение животных в клетке нужно вычислить.
#  Животные в списках нумеруются с 0. Животные в клетке нумеруются с 1
#  Метод index возвращает позицию животного в списке. Вам нужно получить из него
#  номер клетки.

#  Не совсем понял. Вы пишите: -"Метод index возвращает позицию животного в списке. Вам нужно получить из него
#  номер клетки"
#  Мне индексу льва(а он является в списке - 0) просто присвоить "1"? .
#  Что в этом списке считать клеткой?
#  Правильно ли я вас понял..так?
# Да, всё верно.

print('Лев находится в клетке  №', (zoo.index('lion') + 1))

print('Жаворонок находится в клетке  №', (zoo.index('lark') + 1))

# зачет!
