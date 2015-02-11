#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Вхідні дані: рядок, що складається з відкриваючих та закриваючих круглих дужок - аргумент командного рядка. Для передачі в якості рядка послідовність береться в подвійні лапки.

Результат роботи: рядок "YES", якщо вхідний рядок містить правильну дужкову послідовність; або рядок "NO", якщо послідовність є неправильною. Дужкова послідовність вважається правильною, якщо всі дужки можна розбити попарно "відкриваюча"-"закриваюча", при чому в кожній парі закриваюча дужка слідує після відкриваючої.

Пояснення для математиків:
 "" (порожній рядок) - правильна дужкова послідовність (ПДП)
 "(ПДП)" - також ПДП
 "ПДППДП" (дві ПДП записані поряд) - також ПДП

Наприклад
 Вхідні дані: ")("
 Результат: NO
 Вхідні дані: "(()(()"
 Результат: NO
 Вхідні дані: "(()(()()))"
 Результат: YES
 Вхідні дані: "())()(()())(()"
 Результат: NO
 """
