﻿#Задача 10. Вариант 27.
#Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.
print ("""
		    Добро пожаловать в "Генератор персонажей"    				
	   Вы можете распределить 30 очков между 4 характеристиками:    
	Сила,Здоровье,Мудрость и Ловкость. Вы можете как брать из общего
	                 числа пунктов,так и возвращать.    
					 
	                             Удачи!                               
 """)
STR=0
HP=0
INT=0
AGL=0
point=30
amount=0
print("Напишите ту характеристику, которую хотите изменить.")
while True:
       if STR<0 or HP<0 or INT<0 or AGL<0 or point>30:
              print("Ошибка")
              break
       elif point==0:
              print("Вы распределили очки таким образом:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL)
              break
       print("Ваши очки:\nСила:",STR,"\nЗдоровье:",HP,"\nМудрость:",INT,"\nЛовкость:",AGL,"\nНераспределенные очки:",point)
       user_input=input("")
       if user_input=="Сила" :
              amount=int(input("Сколько хотите прибавить(убавить)?\n"))
              if amount <= point :
                            STR+=amount
                            point-=amount
              else :
                     print('Слишком много')
       elif user_input=="Здоровье":
              amount=int(input("Сколько хотите прибавить(убавить)?\n"))
              if amount <= point :
                            HP+=amount
                            point-=amount
              else :
                     print("Слишком много")
       elif user_input=="Мудрость" :
              amount=int(input("Сколько хотите прибавить(убавить)?\n"))
              if amount <= point :
                            INT+=amount
                            point-=amount
              else :
                     print("Слишком много")
       elif user_input=="Ловкость":
              amount=int(input("Сколько хотите прибавить(убавить)?\n"))
              if amount <= point :
                            AGL+=amount
                            point-=amount
              else :
                     print("Слишком много")
input("Нажмите Enter")
#Chernov M. S.
#28.05.2016