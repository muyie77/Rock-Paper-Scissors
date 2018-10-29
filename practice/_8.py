while True:
    choices = ["rock", "paper", "scissors"]
    yes_or_no = ['y', 'n', 'Y', 'N']
    play_again = None

    while True:
        player1 = input("Player1: ")
        if player1 in choices:
            break
        else:
            print("Invalid!")

    while True:
        player2 = input("Player2: ")
        if player2 in choices:
            break
        else:
            print("Invalid!")

    if player1 == player2:
        print("Draw")
    elif player1 == choices[0]:
        if player2 == choices[1]:
            print("Player2 won")
        else:
            print("Player1 won")
    elif player1 == choices[1]:
        if player2 == choices[2]:
            print("Player2 won")
        else:
            print("Player1 won")
    elif player1 == choices[2]:
        if player2 == choices[0]:
            print("Player2 won")
        else:
            print("Player1 won")

    while play_again not in yes_or_no:
        play_again = input("Would you like to play again? y/n")
        if play_again not in yes_or_no:
            print("Invalid!")

    if play_again == yes_or_no[0] or play_again == yes_or_no[2]:
        pass
    else:
        break
