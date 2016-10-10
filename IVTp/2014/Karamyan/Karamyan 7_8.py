# Задача 7, Вариант 8

# Разработайте систему начисления очков для задачи 6, в соответствии
# с которой игрок получал бы большее количество баллов за меньшее
# количество попыток.

# Карамян Н.Г.
# 23.05.2016

import random

name = random.randrange(2)

if (name) == 0:
    name = "Пейдж"
elif (name) == 1:
    name = "Брин"

trial = 3
bonus = 1000

print ("Я загадал имя одного из сооснователей Гугл. Угадай, кого!\n")
print (name)

while trial > 0 :
        answer = input ("Ваш ответ: ")
        if answer.lower() == name.lower():
                print('\nЙес!!!')
                print ('Вам начислено', bonus, 'баллов.')
                break

        else:
                print ("Ноуп :(")
                trial -= 1
                bonus -= 100
                if trial > 1:
                        print ('У Вас осталось', bonus, 'баллов.')
                        print ('Попробуйте еще раз.')
                        
                else:
                        print("Правильный ответ: " , name)

input ("Жмак")
