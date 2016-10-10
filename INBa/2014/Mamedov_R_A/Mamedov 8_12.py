# Задача 8, вариант 12

# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков,
# по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Мамедов Р.А.
# 10.05.2016


import random
print('Анаграммы (Word Jumble)')
print('Компьютер выбрипает какое-либо и хаотически переставляет его буквы.Задача игрока -восстановить искодные слова')
print('За каждую подсказку, программа списывает 5 баллов')
COUNT_INSIDE = 3

WORDS = ('питон','анаграмма', 'простая', 'сложная', 'ответ', 'подстаканник')

def shufle(word) :
    shufle_word = word
    n = len(word)
    shufle_word = ''
    for i in range(0,n) :
       shufle_word += word[n-i-1] 
    return shufle_word

def init_insides(word) :
    insides = []
    for i in range(0, COUNT_INSIDE) :
        insides.append('Подсказка ' + str(i+1))
    return insides

correct = random.choice(WORDS)
jumble = shufle(correct)

ball = 15
penalty = 5 
count_penalty = 0

insides = init_insides(correct)

print('Вот анаграмма, угадай:'  ,jumble)

user_word = ''
while correct != user_word and count_penalty < COUNT_INSIDE :
    user_word = input('Введите ваш вариант: ')
    if correct != user_word :
        print('Не правильно')
        inside = input('Подсказку дать? (да/нет)')
        if inside.lower() == 'да' :
            print ('Подсказка', insides[count_penalty])
            count_penalty += 1
            print ('С вас списали', penalty,'баллов!')
            ball -= penalty

if correct == user_word :        
    print('Вы выиграли!!! У вас' , ball,  'баллов')
else :
	print('Вы проиграли!!! Правильный ответ: ', correct)
input ('Нажмите Enter для выхода')



