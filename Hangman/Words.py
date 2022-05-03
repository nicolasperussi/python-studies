import random

movie_list = [
    'Star Wars',
    'Star Trek',
    'Indiana Jones',
    'Avengers Endgame',
    'Harry Potter',
]

fruits_list = [
    'Apple',
    'Banana',
    'Peach',
    'Passionfruit',
    'Pineapple',
    'Pear',
    'Orange',
    'Mango'
]

WORD_LIST = [movie_list, fruits_list]


def chooseRandomWord(theme):
    word = random.choice(WORD_LIST[theme])
    return word
