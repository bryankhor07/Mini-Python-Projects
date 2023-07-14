import random

def get_choices():
    player_choice = input("Enter a choice: Rock, Paper, Scissors ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Paper":
            return "Paper covers rock! Computer wins!"
        else:
            return "Rock smashes scissors! You win!"
    elif player == "Paper":
        if computer == "Scissors":
            return "Scissors cuts paper! Computer wins!"
        else:
            return "Paper covers rock! You win!"
    elif player == "Scissors":
        if computer == "Rock":
            return "Rock smashes scissors! Computer wins!"
        else:
            return "Scissors cuts paper! You win!"

while True:   
    choices = get_choices()
    print(check_win(choices["player"], choices["computer"]))

    option = input("Do you want to play again? Y / N ")
    if option == "N":
        print("Good game! See you next time!")
        break