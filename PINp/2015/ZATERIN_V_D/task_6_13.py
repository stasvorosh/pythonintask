#Создайте игру, в которой компьютер загадывает название одного из двух
#спутников Марса, а игрок должен его угадать.

import random
sputnik = random.randint(1,2)
if sputnik == 1: sputnik="фобос"
elif sputnik ==2: sputnik="деймес"

print("Угадай спутник Марса: ")
otvet = input("\n ВВеди слово: ")
while(otvet != cvet):
    print("\nНеправильно. Попробуй еще раз")
    otvet = input("\nВведи слово: ")
 
print("Правильно! Это", sputnik,"спутник!")
input("Нажмите ENTER для продолжения")