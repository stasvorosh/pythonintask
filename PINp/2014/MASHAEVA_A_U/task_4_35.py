﻿# Задача 4 Вариант 35
# Напишите программу, которая выводит имя, под которым скрывается Тициано Вечеллио. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.
# Машаева Ангелина Юрьевна
# 19.03.2016

print("Тициано Вечеллио известен, как Тициан,который считается одним из величайших итальянских живописцев эпохи Возрождения.")
print("Место рождение:	Пьеве ди Кадоре, Фриули") 
a = 1485
b = 1576
v = b-a
print("Год рождения: " + str(a))
print("Год смерти: " + str(b))
print('Возраст: ' + str(v))
print("Область интересов:живописец ")
input("\n\nНажмите Enter для выхода.")