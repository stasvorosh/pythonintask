#Задача 9. Вариант 10.
#1-50. Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

#Кишуков Назир
#25.05.2016

import random
words = ("Нальчик", "Кабардино-Балкарская Республика", "Ирина", "Аслан")
word = random.choice(words)
proverka = word
letters = len(word)
letter = random.randrange(letters)
i = 5
print("Я загадал некоторые слова связанные со мной. В  нём ", letters, " букв(/-ы).")
print("У тебя есть 10 попыток угадать буквы в этом слове!")
guess = input("Введите букву: ")
while i > 0:
	if guess in word:
		print("Есть такая буква!")
	else: print("Тебе че в нос пернуть?!")
	i -= 1
	guess = input("Введите ещё одну букву: ")
guess = input("Назовешь слово сразу?!Эу?!: ")
if guess == word:
	print("Краусавчег! Это слово", word)
else:
	print("Вот ты лошпед!!")
input ("\nНажмите Enter для выхода.")
