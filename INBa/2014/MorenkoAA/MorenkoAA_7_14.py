# Задача 7, Вариант 14 
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Моренко А.А.
# 04.04.2016

import random
print ('Отгадайте загадку: Сидит дед во сто шуб одет')
def get_random_ded():
   deds = ("Дед","Капуста","Лук","Салат",
   "Дед в ста шубах")
   return random.choice(deds)
ded = get_random_ded()
user_ded = input('Введите ваш вариант: ')
Points = 100
while ded.lower() != user_ded.lower() and Points >1:
    Points -= 2
    print('У вас остлось', Points, 'Points', 'Попробуйте ещё раз')
    user_ded = input('Введите ваш вариант: ')
if Points > 1:
   print("Bы отгдали!"'Points остлось:', Points)
else:
    print('Баллы закончились, а вы не угадали :C ')
input ('Нажмите Enter для выхода')





