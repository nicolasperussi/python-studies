from Words import chooseRandomWord, transform, checkLetter
import os
import sys


def clearConsole():
    os.system("cls")


def startGame():
    clearConsole()

    isWordGuessed = False

    print('Select your theme:')
    print('Enter 1 to MOVIES')
    print('Enter 2 to FRUITS')
    theme = input()

    guesses = 8
    wordToGuess = chooseRandomWord(int(theme) - 1)
    playerGuess = transform(wordToGuess)

    clearConsole()

    while (not isWordGuessed) and (guesses > 0):

        print('Your word is:')
        print(playerGuess)

        print('')
        print('Choose 1 to guess a letter')
        print('Choose 2 to guess the word')
        choice = input()

        if choice == 1:
            clearConsole()
            print('Your word is:')
            print(playerGuess)
            print('')
            print('Please enter a letter:')
            letterGuess = input()

            playerGuess = checkLetter(wordToGuess, playerGuess, letterGuess)

            # let him make another guess
        else:
            # let him guess the word
            clearConsole()
            print('Your word is:')
            print(playerGuess)
            print('')
            print('Please enter your guess:')
            wordGuess = input()

        guesses = guesses - 1


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
