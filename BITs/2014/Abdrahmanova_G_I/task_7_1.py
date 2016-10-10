#Задача 7. Вариант 1.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.
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
      if guessesTaken==1:
          print('Количество заработанных баллов: ', 100)
      if guessesTaken==2:
          print('Количество заработанных баллов: ', 50)
if guess!=musketry:
      print('Попытки кончились')
      print('Вы не набрали баллов')
input('Нажмите Enter')
#Abdrahmanova G. I.
#28.03.2016