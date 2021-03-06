#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
# Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
# Должна получиться фраза на русском языке, например: как два байта переслать.

# Ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Подсказки:
#   В каждом элементе списка защифровано одно слово.
#   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
#   Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

#  Получите строки используя один срез, а не два.
#  Вместо secret_message[3][a:b][::-1] нужно сделать
#  secret_message[3][c:d:e] --
#  - не понял как делать...':e' - это ведь шаг..?,а мне нужно перевернуть полученное слово...
#  Если использовать способ: [7:13:-1] , где с помощью -1 сделать срез в обратном порядке,то у меня ничего не выходит.
#  В инете чет такую связку тоже не нашел...Вы на уроке пообещали с этим разобраться...)
#  Спасибо. Я понял. Не верно расставлял индексы
# [::-1]-синтаксис среза переворота строки.
# Для оформления длинных строк удобно пользоваться скобками:
not_secret = (
        secret_message[0][3] + ' '
        + secret_message[1][9:13] + ' '
        + secret_message[2][5:15:2] + ' '
        + secret_message[3][12:6:-1] + ' '
        + secret_message[4][20:15:-1]
)

print(not_secret.capitalize())


