#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Розробити класс CombStr для представлення рядка символів.

Забезпечити наступні методи класу:
конструктор, який приймає 1 аргумент -- рядок string.
метод count_substrings(length), який приймає 1 аргумент -- невід'ємне ціле число length, 
та повертає ціле число -- кількість всіх різних підрядків довжиною length, 
що містяться в рядку string.

Тести із некоректними даними не проводяться. 

Послідовність символів substring вважається підрядком рядка string, 
якщо її можна отримати зі string шляхом відкидання символів з початку та/або з кінця рядка. 
Наприклад 'asd' є підрядком 'asdfg', а 'fgh' -- ні. Вважати, що порожніх підрядків не буває, 
тому для length=0 повертати 0.

Приклад послідовності дій для тестування класу:
 s0 = CombStr('qqqqqqweqqq%')
 print s0.count_substrings(0) # 0
 print s0.count_substrings(1) # 4
 print s0.count_substrings(2) # 5
 print s0.count_substrings(5) # 7
 print s0.count_substrings(15) # 0
"""
class CombStr(object):
	
	