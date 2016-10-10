#Задача №8, Вариант 21
#1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#Rotkin A.M.
## 27.05.16
import random
slova = ("Вселенная","Щеки","Милота","Няшность","Солнышко")
slovo = random.choice(slova)
correct = slovo
podskazka = ""
jumble = ""
count = 20
while slovo:
    position = random.randrange(len(slovo))
    jumble += slovo[position]
    slovo = slovo[:position]+slovo[(position+1):]
print ("Игра началась...")
print ("Представленная анаграмма", jumble)
turn = " "
while turn != correct and turn != "":
    turn = input("Начальное слово:")
    if turn == "подсказка":
        podskazka = (correct[:position+1])
        print (podskazka)
        count -=1
        print (count)
        position +=1
    elif turn == correct:
        count -=1
        print("WIN!, Your score:", count)
    elif turn != correct:
        count -=1
        print ("Попробуй снова:")
input ("put enter to exit")
