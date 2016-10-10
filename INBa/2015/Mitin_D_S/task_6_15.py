# Задача 6. Вариант 15.
# Создайте игру, в которой компьютер загадывает название одного из двенадцати городов, входящих в Золотое кольцо России, 
#а игрок должен его угадать.

# Mitin D.S.
# 30.03.2016, 21:20.
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
    otvet = input("\nВведите город: ")

print("Правильно! Это город", choice,"!")
input("Нажмите ENTER для продолжения")
