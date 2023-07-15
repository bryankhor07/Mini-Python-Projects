import random

def get_choices():
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    player_choice = input("Enter a choice: Rock, Paper, Scissors, Lizard, Spock ")

    # Validate the user's input each round to make sure they enter a valid choice
    while player_choice not in options:
        print(f"{player_choice} is not a valid option. Pick again.")
        player_choice = input("Enter a choice: Rock, Paper, Scissors, Lizard, Spock ")
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer, computer_name, emojis):
    player_emoji = emojis[player]
    computer_emoji = emojis[computer]
    print(f"You chose {player}{player_emoji}, {computer_name} chose {computer}{computer_emoji}")
    if player == computer:
        return "It's a tie!"
    elif player == "Rock":
        if computer == "Scissors":
            return f"Rock crushes {computer} You win!"
        elif computer == "Lizard":
            return f"Rock crushes {computer}! You win!"
        elif computer == "Paper":
            return f"Paper covers {player}! {computer_name} wins!"
        elif computer == "Spock":
            return f"Spock vaporizes {player}! {computer_name} wins!"
    elif player == "Paper":
        if computer == "Rock":
            return f"Paper covers {computer}! You win!!"
        elif computer == "Spock":
            return f"Paper disproves {computer}! You win!"
        elif computer == "Lizard":
            return f"Lizard eats {player}! {computer_name} wins!"
        elif computer == "Scissors":
            return f"Scissors cuts {player}! {computer_name} wins!"
    elif player == "Scissors":
        if computer == "Paper":
            return f"Scissors cuts {computer}! You win!"
        elif computer == "Lizard":
            return f"Scissors decapitates {computer}! You win!"
        elif computer == "Rock":
            return f"Rock crushes {player}! {computer_name} wins!"
        elif computer == "Spock":
            return f"Spock smashes {player}! {computer_name} wins!"
    elif player == "Lizard":
        if computer == "Spock":
            return f"Lizard poisons {computer}! You win!"
        elif computer == "Paper":
            return f"Lizard eats {computer}! You win!"
        elif computer == "Rock":
            return f"Rock crushes {player}! {computer_name} wins!"
        elif computer == "Scissors":
            return f"Scissors decapitates {player}! {computer_name} wins!"
    elif player == "Spock":
        if computer == "Rock":
            return f"Spock vaporizes {computer}! You win!"
        elif computer == "Scissors":
            return f"Spock smashes {computer}! You win!"
        elif computer == "Paper":
            return f"Paper disproves {player}! {computer_name} wins!"
        elif computer == "Lizard":
            return f"Lizard poisons {player}! {computer_name} wins!"


def main():       
    username = input("What's your name? ")
    computer_names = ["Betty", "Derek", "Veronica", "Xavier", "Penny", "Cody"]
    computer = random.choice(computer_names)
    player_score = 0
    computer_score = 0

    emojis = {"Rock": "✊️", "Paper": "✋️", "Scissors": "✌️", "Lizard": "🦎", "Spock": "🖖"}

    print(f"Welcome {username}! Today you will be playing against {computer}.")
    rounds = int(input("How many rounds do you want to play? "))

    for i in range(rounds): 
        print(f"\nRound {i+1}:")
        choices = get_choices()
        result = check_win(choices["player"], choices["computer"], computer, emojis)
        if "You" in result:
            player_score += 1
        elif computer in result:
            computer_score += 1

        print(result)
        print(f"Score: {username} {player_score}, {computer} {computer_score}")
        if i == rounds - 1:
            if player_score == computer_score:
                print("Oh no, it's a tie!")
            elif player_score > computer_score:
                print(f"Congratulations {username}! You won the game!")
            else:
                print("You lost! Try again next time!")

main()