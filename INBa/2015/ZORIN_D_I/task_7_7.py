# Задача 7. Вариант 7.
# Создайте игру, в которой компьютер загадывает имя одного из двух сооснователей компании Google, а игрок должен его угадать.

# Zorin D.I.
# 01.05.2016
ball=10
import random
a = random.randint(1,2)
if a == 1:
  w="Сергей Брин"
elif a ==2:
  w="Ларри Пейдж"
print("Основатель компании google: ")
otvet = input("\nВведите имя: ")
while(otvet != w):
 ball=ball-1
 if (ball > 0):
    print("\nНеправильно. Попробуй еще раз")
 otvet = input("\nВведите имя: ")
 if (ball < 0):
    ball = 0
 elif ball==0:
    print("Вы проиграли!!! Попробуй в другой раз.")
print("Правильно!", w,"!") 
print("Вы набрали ",ball," очков!")
print("Game over! \nCпасибо за игру!")
input("Нажмите ENTER для продолжения")

