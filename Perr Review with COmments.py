# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Hunter Stines
# Creation Date: 05-12-2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors).  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    #ERROR: Incorrect logic, returning the wrong variable name "caves" instead of "cave"
    return caves

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    #ERROR: Typing error, comment indicates that it needs to sleep for 2 seconds however it is actually sleeping for 3 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        #ERROR: Incorrect syntax, print statements require Parenthesis around the string
        print 'Gobbles you down in one bite!'

#ERROR: Main Driver code should be put in a main() function
#ERROR: Design flaw, declaring global variables outside of a function is not good practice
playAgain = 'yes'
#ERROR: Incorrect syntax, while comparing two variables you need to use == instead of = 
while playAgain = 'yes' or playAgain = 'y':
    displayIntro()
    #ERROR: Incorrect function name call, you need to use the function name "chooseCave" instead of "choosecave" as python is case sensitive
    caveNumber = choosecave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
    if playAgain == "no":
        #ERROR: Typing error, you need to use the string "Thanks for playing" instead of "Thanks for planing!"
        print("Thanks for planing")
    #ERROR: Logic flaw, if the user answers anything except yes or no, the program should continue to run and ask the user to answer between yes or no. The logic of the while loop should be
    # while playAgain != 'no' or playAgain != 'n': similar to the choseCave Function.