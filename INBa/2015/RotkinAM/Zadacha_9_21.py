#Задача №9
#1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.
#Rotkin A.M.
## 28.05.16
import random
slova = ("Вселенная","Щеки","Милота","Няшность","Солнышко")
slovo = random.choice(slova)
count = 5
vvod = " "
lastslovo = " "
print (" В данном слове", len(slovo), "букв(-ы)")
while count > 0:
    vvod = input("У вас есть 5 попыток. Введите букву:")
    if vvod in slovo:
        print ("Yes")
        count -=1
    else:
        print ("No")
        count -=1
if count <= 0 :
    lastslovo = input("У вас есть возможность угадать слово целиком, go:")
    if lastslovo == slovo:
        print ("WIN!!!")
    else:
        print("Lowara")
input ("put enter to exit")
