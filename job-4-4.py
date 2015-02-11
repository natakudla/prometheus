#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Завдання передбачає пошук "щасливих" квитків. "Щасливим" називається такий тролейбусний квиток, в якому сума перших трьох цифр дорівнює сумі останніх трьох. Наприклад 030111 (0+3+0 = 1+1+1), 902326 (9+0+2 = 3+2+6), 001100 (0+0+1 = 1+0+0).

Вхідні дані: два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного рядка.

Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до a2 включно. Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, як це і відбувається при нумерації квитків.

Наприклад
 Вхідні дані: 0 1000
 Результат: 1
 Пояснення: номер 000000
 Вхідні дані: 1001 1122
 Результат: 3
 Пояснення: номери 001001, 001010, 001100
 Вхідні дані: 222222 222333
 Результат: 7
 Пояснення: номери 222222, 222231, 222240, 222303, 222312, 222321, 222330
 """
