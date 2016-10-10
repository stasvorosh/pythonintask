# Задача 9. Вариант 23
# Создайте игру, в которой компьютер выбирает какое-либо слово,
# а игрок должен его отгадать. Компьютер сообщает игроку, сколько
# букв в слове, и дает пять попыток узнать, есть ли какая-либо буква
# в слове, причем программа может отвечать только "Да" и "Нет".
# Вслед за тем игрок должен попробовать отгадать слово.

#еще случайно разработал систему начисления очков
#так как немного перепутал задания 9 и 8

# Alekseev I.S.
# 14.05.2016

import random
 
word = ("агрессия","симпатия","недовольство","радость","печаль","апатия")
 
variant=""
 
computer=random.choice (word)
 
podskazka=5
points=10000
popitka=5
 
print("\nКомпьютер выбрал одно из 5-ти предложенных слов ",word," угадайте его") 
 
while popitka!=0 and variant != computer :
 
     
    if podskazka==5 :     
        
        if (input("\nВоспользуетесь подсказкой?\nДля согласия наберите 'да', для отказа нажмите Enter\n")) == "да" :
            print("\nДлина заданного слова = :",len(computer))
            podskazka=podskazka-1
            points=points-1000
            print("Осталось подказок :",podskazka)
            print("Осталось очков :",points)
            
    else :
        if podskazka <5 and podskazka >0:
            if (input("\nНужна ли Вам ещё подсказка?\n('Да' или Enter)")) == "да" :
                podskazka=podskazka-1
                points=points-1000
                print("Осталось подказок :",podskazka)
                print("Осталось очков :",points)
                letter=input("Назовите букву и я скажу - есть ли она в слове :")
                if letter in computer :
                    print("Эта буква присутствует в слове")
                else :
                    print ("буква отсутвует") 
 
    variant=input("\n Ваш вариант :")
 
    
    if variant==computer :
        print("Вы угадали!")
        print("Вы зарабoтали ",points,"очков.")
        print("И угадали слово с ",10-popitka,"попытки, использовав ",5-podskazka,"подсказки")
    else :
        popitka=popitka-1
        points=points-1000
        print("\nВы ошиблись")
        print("Осталось попыток :",popitka)
        print("Осталось очков :",points)

    if popitka==0:
        print("\nЗакончились попытки, вы заработали 0 очков")
print("Нажмите Интер для выхода")
