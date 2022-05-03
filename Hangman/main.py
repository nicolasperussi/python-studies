from Words import chooseRandomWord
import os
import random
import sys

os.system("cls")


def startGame():
    os.system("cls")

    isWordGuessed = False

    print('Select your theme:')
    print('Enter 1 to MOVIES')
    print('Enter 2 to FRUITS')
    theme = input()

    guesses = 8
    word = chooseRandomWord(int(theme) - 1)
    # playerGuess = 

    while (not isWordGuessed) and (guesses > 0):
        os.system("cls")

        print(playerGuess)
        guesses - 1


# create a 'guess' variable that is the same length as the word, change letters to underscores and keep spaces
# create a while statement to check if the guess is the same as the word everytime the players makes a guess
# at every guess, check if the there is any of the guessed letter in the word, then check position and change the underscore to the letter in that position


def main():
    print('Welcome to Hangman!')
    print('Enter 1 to play')
    print('Enter 2 to exit')

    option = input()

    if (option == '2'):
        sys.exit(0)
    elif (option == '1'):
        startGame()


main()
