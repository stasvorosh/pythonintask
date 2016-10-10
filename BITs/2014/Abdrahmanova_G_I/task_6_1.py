#Задача 6. Вариант 1.
#Создайте игру, в которой компьютер загадывает имя одного из трех мушкетеров - товарищей д'Артаньяна, а игрок должен его угадать.
import random
guessesTaken=0
print('Компьютер загадал имя одного из трех мушкетеров - товарищей д`Артаньяна. \nТвоя цель отгадать имя загаданного мушкетера.')
musketry=random.choice(["Атос", "Партос", "Арамис"])
while guessesTaken < 2:
      print('Загаданное имя мушкетера: ')
      guess=input()
      guessesTaken=guessesTaken+1
      if guess!=musketry:
          print('Неверно!')
      if guess==musketry:
          break
if guess==musketry:
      print('Верно! Число использованных попыток: ', guessesTaken)
if guess!=musketry:
      print('Попытки кончились')
input('Нажмите Enter')
#Abdrahmanova G. I.
#28.03.2016