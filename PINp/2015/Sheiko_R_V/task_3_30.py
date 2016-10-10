# Задача 1. Вариант 30.
'''
Напишите программу, которая выводит имя "Илья Арнольдович Файзильберг",
и запрашивает его псевдоним. Программа должна сцеплять две эти строки
и выводить полученную строку, разделяя имя и псевдоним с помощью тире.
'''
# SHEIKO R.V
# 10.03.2016

from sys import stdout as c
from time import sleep

name = 'Илья Арнольдович Файнзильберг'
question = 'Какой псевдоним носил советский писатель ' + name + '?'

sleep(1.0)

def printer(text):
    for char in text:
        c.write(char)
        c.flush()
        pause = 0.03
        sleep(pause)

printer(question)
c.write('\n'*2)
answer = input('Ваш ответ: ')
c.write('\n'*2)
printer('Правильно: ' + name + ' - ' + answer)
c.write('\n'*2)

input('ok')
