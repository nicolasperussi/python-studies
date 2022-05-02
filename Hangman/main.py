import random
import sys

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
]

WORD_LIST = [movie_list, fruits_list]

def startGame():
  wordListChosen = random.choice(WORD_LIST)
  word = random.choice(wordListChosen)

  # create a 'guess' variable that is the same length as the word, change letters to underscores and keep spaces
  # create a while statement to check if the guess is the same as the word everytime the players makes a guess
  # at every guess, check if the there is any of the guessed letter in the word, then check position and change the underscore to the letter in that position 

def main():
    print('=================================')
    print('Welcome to Hangman!')
    print('Enter 1 to play')
    print('Enter 2 to exit')
    print('=================================')

    option = input()

    if (option == '2'):
        sys.exit(0)
    elif (option == '1'):
        startGame()


main()
