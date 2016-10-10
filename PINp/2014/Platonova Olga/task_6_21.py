# Задача 6. Вариант 21.
#Создайте игру, в которой компьютер загадывает название одной из семи основных физических единиц, согласно Международной системы единиц , а игрок должен его угадать.

# Platonova O. A.
# 29.05.2016
import random

metric=random.randint(0,6)
if metric==0:
  answer="килограмм"
elif metric==1:
    answer="метр"
elif metric==2:
    answer="кельвин"
elif metric==3:
    answer="секунда"
elif metric==4:
    answer="ампер"
elif metric==5:
    answer="моль"
elif metric==6:
    answer="кандела"

print("Программа случайным образом загадала название одной из семи основных физических единиц. Игрок должен отгадать.")
myanswer=input("Назовите одну из семи основных физических единиц: ")
if answer==myanswer:
    print("Вы угадали!")
else:
    print("Вы не угадали!")
print("Првильный ответ:",answer)

input("\nНажмите Enter для выхода.")