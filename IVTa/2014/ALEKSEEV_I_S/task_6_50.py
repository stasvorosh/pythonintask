# Задача 6. Вариант 50.

#Создайте игру, в которой компьютер загадывает название одной из пятнадцати республик, 
#входящих в состав СССР, а игрок должен его угадать.

# Alekseev I.S.
# 15.05.2016

import random

print("Программа случайным образом загадывает название одной из пятнадцати республик, входящих в состав СССР, а игрок должен его угадать.")

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

answer = input('\nВведите название одной из пятнадцати республик: ')

if answer == repub :
    print('\nВы угадали!')
else :
    print('\nВы не угадали!!!')
    print('Правильный ответ: ', repub)

input("\n\nНажмите Enter для выхода.")
