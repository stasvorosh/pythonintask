# Задача 7. Вариант 15.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее 
# количество баллов за меньшее количество попыток.

# Mitin D.S.
# 11.04.2016, 14:21
ochki=500000
import random
choice = random.randint(1,12)
if choice == 1:
    choice="Переславль-Залесский"
elif choice == 2: 
    choice="Ростов Великий"
elif choice == 3: 
	choice="Углич"
elif choice == 4: 
	choice="Ярославль"
elif choice == 5: 
	choice="Кострома"
elif choice == 6: 
	choice="Плёс"
elif choice == 7: 
	choice="Суздаль"
elif choice == 8: 
	choice="Владимир"
elif choice == 9: 
	choice="Александров"
elif choice == 10: 
	choice="Сергиев Посад"
elif choice == 11: 
	choice="Тутаев"
elif choice == 12: 
	choice="Юрьев-Польский"
print("Угадайте город Золотого кольца: ")
otvet = input("\nВведите город: ")
while(otvet != choice):
    print("\nНеправильно. Попробуй еще раз")
    ochki=ochki-5000
    otvet = input("\nВведите город: ")

print("Правильно! Это город",choice,"!")
if ochki>0: 
    print("Вы набрали ",ochki," очков! Поздравляем!")
elif ochki<=0:
    print("У вас 0 очков. Вы проиграли. Попробуйте еще.")
input("Нажмите ENTER для продолжения")
