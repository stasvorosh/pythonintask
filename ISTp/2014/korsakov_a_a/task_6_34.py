# Задача 6. Вариант 34
# Создайте игру, в которой компьютер загадывает имя одного из трех
# племянников Скруджа МакДака, а игрок должен его угадать.

# Korsakov A.A.
# 13.04.2016

print ('Программа случайным образом загадывает имя одного из трёх племянников Скруджа МакДака, а игрок должен его угадать')
import random
Slovo_Polzovatelya = input('\n Назовите имя одного из племянников Скруджа МакДака:')
Billy = 'Билли'
Villy = 'Вилли'
Dilly = 'Дилли'
n = random.randint(1,3)
if n == 1: word = Billy
elif n == 2: word = Villy
else: word = Dilly
while word.lower()!= Slovo_Polzovatelya.lower():
    Slovo_Polzovatelya = input('Вы не угадали, попробуйте ещё раз!\n:')
print('Ура, поздравляем, вы угадали!') 

input ('\n\n Нажмите Enter для выхода')
