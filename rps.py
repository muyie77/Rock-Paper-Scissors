from random import randint
from sys import exit

# Function Declarations
# Player
def player():
    while True:
        choice = int(input("> "))
        if choice == 1:
            print("You have chosen Rock.")
            break
        elif choice == 2:
            print("You have chosen Paper.")
            break
        elif choice == 3:
            print("You have chosen Scissors.")
            break
        else:
            print("Invalid choice! Choose again.")
    return choice

# Computer
def computer():
    choice = randint(1, 3)

    if choice == 1:
        print("Computer have chosen Rock.\n")
    elif choice == 2:
        print("Computer have chosen Paper.\n")
    else:
        print("Computer have chosen Scissors.\n")
    return choice

# Comparing choice
def compare():
    win = 0
    lose = 0
    draw = 0

    while True:
        print("--------------")
        print("| 1. Rock    |\n| 2. Paper   |\n| 3. Scissors|")
        print("--------------")

        user = player()
        ai = computer()

        if user == 1: # User chose Rock
            if ai == 1: # Computer chose Rock
                print("Draw!\n")
                draw += 1
            elif ai == 2: # Computer chose Paper
                print("You lose!\n")
                lose += 1
            else: # Computer chose Scissors
                print("You win!\n")
                win += 1
        elif user == 2: # User chose Paper
            if ai == 1: # Computer chose Rock
                print("You win!\n")
                win += 1
            elif ai == 2: # Computer chose Paper
                print("Draw!\n")
                draw += 1
            else: # Computer chose Scissors
                print("You lose!\n")
                lose += 1
        else: # User chose Scissors
            if ai == 1: # Computer chose Rock
                print("You lose!\n")
                lose += 1
            elif ai == 2: # Computer chose Paper
                print("You win!\n")
                win += 1
            else: # Computer chose Scissors
                print("Draw!\n")
                draw += 1

        print(f"Win: {win}\tLose: {lose}\tDraw: {draw}")
        print("Do you want to play again? y/n")

        while True:
            ch = input("> ")
            if ch == 'y' or ch == 'Y':
                print("")
                """Play again"""
                break
            elif ch == 'n' or ch == 'N':
                exit(0)
            else:
                print("Invalid choice!\n")

compare()
