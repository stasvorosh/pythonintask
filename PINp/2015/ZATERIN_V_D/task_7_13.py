import random

print("Компьютер загадал марку одной из машин.\n")

car = ('chevralet','honda','mitsubishi','dodge','bmw','mercedes')
car = random.randint(0,5)
x = 0
i = 0
score = 0

#print (car[0]\n,car[1]\n,car[2]\n,car[3]\n,car[4]\n,car[5])

while(x != 6):
	print(auto[x])
	x += 1

answer = input("\nВведите название автомобиля: ")

while(answer != cars[car]):
    print("Неверно, попробуйте ещё раз.")
    answer = input("\n Введите название автомобиля: ")
    i += 1

if i == 0:
	score = 100
	
elif 0<i<6:
	score = 100 - i*2
	
else:
	score = 0

print("Верно, Вы победили!")
print("Число попыток: "+str(i))
print("Вы заработали "+str(score)+" баллов")

input("\nДля выхода нажмите Enter.")
