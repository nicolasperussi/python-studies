import time
from Words import chooseRandomWord, transform, checkLetter
import os
import sys


def clearConsole():
    print('')
    os.system("cls")


def loseGame():
    clearConsole()
    print('You lost!')
    time.sleep(5)
    sys.exit(0)

def startGame():
    clearConsole()

    isWordGuessed = False

    print('Select your theme:')
    print('Enter 1 to MOVIES')
    print('Enter 2 to FRUITS')
    theme = input()

    wordToGuess = chooseRandomWord(int(theme) - 1)
    playerGuess = transform(wordToGuess)
    guesses = len(wordToGuess)

    clearConsole()

    while (isWordGuessed is not True) and (guesses > 0):
        clearConsole()
        print('You have {} guesses left'.format(guesses))
        print('Your word is:')
        print(playerGuess)

        print('')
        print('Choose 1 to guess a letter')
        print('Choose 2 to guess the word')
        choice = int(input())

        if choice == 1:
            clearConsole()
            print('Your word is:')
            print(playerGuess)
            print('')
            print('Please enter a letter:')
            letterGuess = input()

            playerGuess = checkLetter(wordToGuess, playerGuess, letterGuess)
        else:
            clearConsole()
            print('Your word is:')
            print(playerGuess)
            print('')
            print('Please enter your guess:')
            wordGuess = input()

            # Create a method to the player guess the whole word


        # Make sure after all the letters are correct, he takes a guess at the word
        # And make sure he can guess the word after the number of guesses gets down to zero

        guesses = guesses - 1

    if (guesses <= 0) and isWordGuessed is False:
        loseGame()


# create a while statement to check if the guess is the same as the word everytime the players makes a guess



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
