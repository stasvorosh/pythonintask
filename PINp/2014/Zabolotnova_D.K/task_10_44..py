﻿#Задача 10. Вариант 44.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо
#буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

#Заболотнова Д.К.
#25.05.2016


POINT = 30 
ochki = 30  
person = {"Сила":"0","Здоровье":"0","удрость":"0","Ловкость":"0"} 
points = 0 # Переменная для назначения пунктов
choice = None # Переменная выбора меню
while choice != 0: # Цикл работы, пока не будет нажат "0"
    print("""
0 - Выход
1 - Добавить пункты к характеристике
2 - Уменьшить пункты характеристики
3 - Просмотр характеристик
""")
    choice = int(input("Choose option: "))
    if choice == 1:
        print("Пожалуйста, введите характеристику для добавления пунктов. Для изменения доступны", len(person), "характеристики:")
        for item in person:
            print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов для данной характеристики. У вас", ochki, "свободных пунктов")
            points = int(input("\n:"))
            while points > ochki or points < 0: # Проверяем возможность начисления введенного количества пунктов, а также не введено ли отрицательное значение
                print("Вы не можете назначить такое количество пунктов", "Доступно", ochki, "свободных пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было добавлено к", char)
        ochki -= points # Изменяем количество доступных к начислению пунктов
    elif choice == 2:
        print("Пожалуйста, введите имя характеристики для снятия пунктов.", "Доступно изменение для: ")
        for item in person:
            if int(person[item]) > 0: # Не показываем характеристику, если она равна 
                print(item)
        char = str(input("\n:"))
        char = char.title()
        while char not in person:
             print("Нет такой характеристики, проверьте введенные данные: ")
             char = str(input("\n:"))
             char = char.title()
        else:
            print("\nВведите количество пунктов для характеристики. Доступно", person[char], "пунктов:")
            points = int(input("\n:"))
            while points > int(person[char]) or points < 0: # Проверяем возможность снятия такого количества пунктов, а также не введено ли отрицательное значение
                print("Невозможно удалить такое количество пунктов. Доступно", person[char], "пунктов")
                points = int(input("\n:"))
        person[char] = points
        print(points, "пунктов было удалено")
        ochki += points # Возвращаем освободившиеся пункты в доступные
    elif choice == 3:
        print("\nХарактеристики героя")
        for item in person:
            print(item, "\t\t", person[item])
        
    elif choice == 0:
        print("Пока!")
    else:
        print("В меню нет такого пункта")
