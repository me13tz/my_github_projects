# import simplegui
import random
import sys

secret_number = random.randrange(0, 100)
x = 7
n = 9

#helper functions to generate random numbers in two ranges
def range100():
    global secret_number
    secret_number = random.randrange(0, 100)
    return secret_number
def new_game100():
    global secret_number
    print ("\nNew Game. Guess the number, range is from 0 to 100 \nNumber of remaining guesses is 7")

def compare():
    guess100 = input("Enter your guess:  ")
    print()
    global x
    global n
    g = int(guess100)
    if g > 99 or g < 1:
        print("Your guess is out of range")
        x -= 1
        if x == 0:
            x = 7
            print("You are out of guesses, dude.")
            range100()
            new_game100()
            compare()
        else:
            print("Number of remaining guesses is " + str(x))
            print()
            compare()

    elif secret_number < g:
        print ("Lower")
        x -= 1
        if x == 0:
            x = 7
            print("You are out of guesses, man.")
            range100()
            new_game100()
            compare()
        print ("Number of remaining guesses is " + str(x))
        print()
        compare()
    elif secret_number > g:
        print("Higher")
        x -= 1
        if x == 0:
            x = 7
            print("You are out of guesses. Let's play again!")
            range100()
            new_game100()
            compare()
        else:
            print("Number of remaining guesses is " + str(x))
            print()
            compare()
    elif secret_number == g:
        print("Correct!")
        x = 7
        print()
        print()
        range100()
        new_game100()
        compare()

range100()
new_game100()
compare()

