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


def transform(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for letter in letters:
        word = word.replace(letter, "_")

    print(word)
    return word


def checkLetter(word, playerGuess, guess):
    # Check if guessed letter is in word,
    # then change underscore in playerGuess to letter
    # if not, then do not change playerGuess
    # return playerGuess

    dividedWord = list(word)
    dividedPlayerGuess = list(playerGuess)

    for i in range(len(dividedWord)):
        if (dividedWord[i] == guess):
            dividedPlayerGuess[i] = guess
            print(dividedPlayerGuess)

    playerGuess = ''.join(dividedPlayerGuess)

    return playerGuess
