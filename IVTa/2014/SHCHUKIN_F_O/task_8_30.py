# Задача 8. Вариант 30
'''
Доработайте игру "Анаграммы" (см. М.Доусон
Программируем на Python. Гл.4) так, чтобы к
каждому слову полагалась подсказка. Игрок должен
получать право на подсказку в том случае, если
у него нет никаких предположений. Разработайте
систему начисления очков, по которой бы игроки,
отгадавшие слово без подсказки, получали больше
тех, кто запросил подсказку.
'''
# Shchuckin F. O.
# 03.04.2016

from random import shuffle, choice

def score_print(score):
  print ('У вас', score, 'очков')

words_and_info = (
('Кошка',   'мяукает'),
('Собака',  'гавкает'),
('Кит',     'самое большое'),
('Медведь', 'ест рыбу и мед'),
('Леопард', 'самое быстрое'),
('Носорог', 'с рогом на лбу'),
('Жираф',   'очень высокое'),
('Пантера', 'черная кошка'),
('Ягуар',   'как алкогольный напиток')
)

choiced = choice(words_and_info)
word = list(choiced[0].lower())
shuffle(word)
word = ''.join(word)

score = 10

print('Отгадай животное -', word)
print('Наберите "подсказка", чтобы получить совет')
score_print(score)

while True:
  gues = input('> ').lower()

  if gues.lower() == 'подсказка':
    print('подскaзка: Это животное', choiced[1])
    score -= 5
    score_print(score)
    continue

  elif gues.lower() == choiced[0].lower():
    print('Правильно -', choiced[0])
    score_print(score)
    break

  score -= 1
  score_print(score)

input('Нажмите ENTER...')

