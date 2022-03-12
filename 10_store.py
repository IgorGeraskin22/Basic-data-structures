#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

# lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


# 1.Задание. Один раз распечать сколько всего столов и их общая стоимость.
# Решение:
# Вычислим общую стоимость стола по цене 510 рублей в количестве 22 штуки
table_code = goods['Стол']
table_item = store[table_code][0]
table_quantity = table_item['quantity']
table_price = table_item['price']
table_cost = table_quantity * table_price
# Вычислим общую стоимость стола по цене 520 рублей в количестве 32 штуки
table_code = goods['Стол']
table_item = store[table_code][1]
table_quantity2 = table_item['quantity']
table_price2 = table_item['price']
table_cost2 = table_quantity2 * table_price2
# Вычислим общее количество столов всех видов.
total_table_quantity = table_quantity + table_quantity2
# Вычислим общую стоимость столов
total_table_cost = table_cost + table_cost2
print('Стол -', total_table_quantity, 'шт, стоимость', total_table_cost, 'руб')

# 2.Задание. Один раз распечать сколько всего диванов и их общая стоимость.
# Решение:
# Вычислим общую стоимость дивана по цене 1200 рублей в количестве 2 штуки.
sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_cost = sofa_quantity * sofa_price
# Вычислим общую стоимость стола по цене 1150 рублей в количестве 1 штука.
sofa_code = goods['Диван']
sofa_item = store[sofa_code][1]
sofa_quantity2 = sofa_item['quantity']
sofa_price2 = sofa_item['price']
sofa_cost2 = sofa_quantity2 * sofa_price2
# Вычислим общее количество диванов всех видов.
total_sofa_quantity = sofa_quantity + sofa_quantity2

# Вычислим общую стоимость диванов
total_sofa_cost = sofa_cost + sofa_cost2
print('Диван -', total_sofa_quantity, 'шт, стоимость', total_sofa_cost, 'руб')

# 3.Задание. Один раз распечать сколько всего стулов и их общая стоимость
# Решение:
# Вычислим общую стоимость стулов по цене 100 рублей в количестве 50 штук.
stool_code = goods['Стул']
stool_item = store[stool_code][0]
stool_quantity = stool_item['quantity']
stool_price = stool_item['price']
stool_cost = stool_quantity * stool_price
# print(stool_cost)

# Вычислим общую стоимость стула по цене 95 рублей в количестве 12 штук.
stool_code = goods['Стул']
stool_item = store[stool_code][1]
stool_quantity2 = stool_item['quantity']
stool_price2 = stool_item['price']
stool_cost2 = stool_quantity2 * stool_price2
# print(stool_cost2)

# Вычислим общую стоимость стула по цене 97 рублей в количестве 43 штуки.
stool_code = goods['Стул']
stool_item = store[stool_code][2]
stool_quantity3 = stool_item['quantity']
stool_price3 = stool_item['price']
stool_cost3 = stool_quantity3 * stool_price3
# Вычислим общее количество стулов всех видов.
total_stool_quantity = stool_quantity + stool_quantity2 + stool_quantity3
# Вычислим общую стоимость столов
total_stool_cost = stool_cost + stool_cost2 + stool_cost3
print('Стул -', total_stool_quantity, 'шт, стоимость', total_stool_cost, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

# зачет!
