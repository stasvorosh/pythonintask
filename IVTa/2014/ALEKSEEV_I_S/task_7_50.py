# Задача 7. Вариант 50.

#Разработайте систему начисления очков для задачи 6, в соответствии с которой 
#игрок получал бы большее количество баллов за меньшее количество попыток.

# Alekseev I.S.
# 15.05.2016

import random

print("Программа случайным образом загадывает название одной из республик СССР, а игрок должен его угадать.\nЧем меньше попыток вы используете, тем больше баллов заработаете.")

animal_numbers = random.randint(1,4)

repub_numbers = random.randint(1,15)

if repub_numbers == 1 :
    repub = 'РСФСР'
elif repub_numbers == 2 :
    repub = 'Украина'
elif repub_numbers == 3 :
    repub = 'Белоруссия'    
elif repub_numbers == 4 :
    repub = 'Узбекистан'
elif repub_numbers == 5 :
    repub = 'Таджикистан'
elif repub_numbers == 6 :
    repub = 'Казахстан'    
elif repub_numbers == 7 :
    repub = 'Грузия'
elif repub_numbers == 8 :
    repub = 'Азербайджан'    
elif repub_numbers == 9 :
    repub = 'Литва'
elif repub_numbers == 10 :
    repub = 'Молдавия'
elif repub_numbers == 11 :
    repub = 'Латвия'
elif repub_numbers == 12 :
    repub = 'Киргизия'
elif repub_numbers == 13 :
    repub = 'Армения'
elif repub_numbers == 14 :
    repub = 'Туркменистан'
elif repub_numbers == 15 :
    repub = 'Эстония'

trial = 3
bonus = 3000

while trial > 0 :
    answer = input('\nНазовите одно из животных, встреченных Колобком в лесу: ')
    if answer == repub :
        print('\nВы угадали!')
        print('Вам начислено', bonus, 'баллов.')
        break
    else :
        print('\nВы не угадали!!!')
        if trial > 1 :
            print('Попробуйте еще раз.')
        else :
            print('Правильный ответ: ', repub)
        
    trial -= 1
    bonus -= 1000

		
input("\n\nНажмите Enter для выхода.")
