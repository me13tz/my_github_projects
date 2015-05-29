
import random
import math


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print()
        print("Need you to learn how to spell. Let's try again :)")
        new_game()



def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Need you to learn how to spell. Let's try again :)")
        new_game()

def new_game():
    print('\nrock\npaper\nscissors\nlizard\nSpock')
    print()
    player_choice = input("Choose your weapon: ")
    print()
    print ("The player\'s choice is " + player_choice) ###we got the player's choice

    comp_number = random.randrange(0,5) #pick a random integer between 0 and 4
    number = comp_number
    comp_choice = number_to_name(number)#assign function call to result
    print("The computer\'s choice is " + comp_choice)  ###we got the pooter's choice
    name = player_choice
    name_to_number(name)
    player_number = name_to_number(name)
    x = player_number
    y = comp_number
    z = (x - y) % 5
    rpsls(z)


#
def rpsls(z):
    if z == 1:
        print(" ")
        print("Player wins!")
        new_game()
    elif z == 2:
        print(" ")
        print("Player wins!")
        new_game()
    elif z == 3:
        print(" ")
        print("Computer wins!")
        new_game()
    elif z == 4:
        print(" ")
        print("Computer wins!")
        new_game()
    else:
        print(" ")
        print("It\'s a tie!")
        new_game()

new_game()




