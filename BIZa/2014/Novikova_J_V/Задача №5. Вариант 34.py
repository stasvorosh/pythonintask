#Задача №5. Вариант 34. 
#Напишите программу, которая бы при запуске случайным образом отображала 
имя одного из пяти генеральных секретарей ЦК КПСС. 


#Novikova J. V. 
#26.04.2016 

import random 
print("Генеральный секретарь ЦК КПСС") 
Sekretar1=("Иосиф Виссарионович Сталин") 
Sekretar2=("Леонид Ильич Брежнев") 
Sekretar3=("Юрий Владимирович Андропов") 
Sekretar4=("Константин Устинович Черненко"") 
Sekretar5=(Михаил Сергеевич Горбачёв")

country=random.randint(1,3) 
if people==1: 
print (Sekretar1) 
if people==2: 
print(Sekretar2) 
elif people==3: 
print(Sekretar3) 

input('Нажмите Enter для выхода')