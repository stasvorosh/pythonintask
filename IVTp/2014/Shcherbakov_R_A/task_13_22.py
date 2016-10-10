# Задача 13. Вариант 22.
# Разработайте собственную стратегию ходов компьютера для игры "Крестики-
# нолики" (Задача 12). Перепишите функцию computer_move() в соответствии с этой
# стратегией.

# Щербаков Р.А.
# 22.05.2016

import random

print("""
Добро пожаловать на игру крестики нолики 
чтобы сделать ход введите число от 0 до 8
Моя стратегия предназначена для новичков
	 
	          0 | 1 | 2
	          ---------
	          3 | 4 | 5
	          ---------
	          6 | 7 | 8""")
doska=["-","-","-","-","-","-","-","-","-"]
bol=True
wins=False
schet=0
t1="X"
t2="O"
def disp(doska):
     print("\n\t"+doska[0]+" | "+doska[1]+" | "+doska[2]+"\n\t---------"+
	 "\n\t"+doska[3]+" | "+doska[4]+" | "+doska[5]+"\n\t---------"+
	 "\n\t"+doska[6]+" | "+doska[7]+" | "+doska[8]+"\n\t---------")
def win(doska):
     twin=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
     for row in twin:
	     if doska[row[0]]==doska[row[1]]==doska[row[2]]!="-":
		     return True

while True:
     vibor=input("\nХотите ходить первым? [y/n]: ")
     if(vibor=="n"):
          bol=False
          t1="O"
          t2="X"
          break
     elif(vibor=="y"):
          break
while wins!=True:
     if(schet==9):
         break
     if(bol):
         n1=input("\nВаш ход: ")
         if(doska[int(n1)]=="-"):
             doska[int(n1)]=t1
             disp(doska)
             bol=False
             wins=win(doska)
             schet+=1
         else:
	         print("Занято")
     else:
         n2=random.randint(0,8)
         if(doska[int(n2)]=="-"):
             doska[int(n2)]=t2
             disp(doska)
             bol=True
             wins=win(doska)
             schet+=1
if(wins and bol):
     print("Вы проиграли")
elif(wins and not bol):
     print("Вы победили")
else:
     print("Ничья")
input("Ok")