# Задача 5. Вариант 21.
#Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати восьми стран, входящих в Европейский союз.

# Platonova O. A.
# 29.05.2016
import random

evro=random.randint(0,27)
if evro==0:
    print("Австрия")
elif evro==1:
    print("Бельгия")
elif evro==2:
    print("Болгария")
elif evro==3:
    print("Венгрия")
elif evro==4:
    print("Великобритания")
elif evro==5:
    print("Греция")
elif evro==6:
    print("Германия")
elif evro==7:
    print("Дания")
elif evro==8:
    print("Италия")
elif evro==9:
    print("Ирландия")
elif evro==10:
    print("Испания")
elif evro==11:
    print("Республика Кипр")
elif evro==12:
    print("Люксембург")
elif evro==13:
    print("Бельгия")
elif evro==14:
    print("Латвия")
elif evro==15:
    print("Литва")
elif evro==16:
    print("Мальта")
elif evro==17:
    print("Нидерланды")
elif evro==18:
    print("Португалия")
elif evro==19:
    print("Польша")
elif evro==20:
    print("Румыния")
elif evro==21:
    print("Словения")
elif evro==22:
    print("Словакия")
elif evro==23:
    print("Франция")
elif evro==24:
    print("Финляндия")
elif evro==25:
    print("Хорватия")
elif evro==26:
    print("Чехия")
elif evro==27:
    print("Швеция")


input("\nНажмите Enter для выхода.")