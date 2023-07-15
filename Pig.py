import random

# Player class
class Player:
    # Constructor
    def __init__(self, name, total_score, turn_score) -> None:
        self.name = name
        self.total_score = total_score
        self.turn_score = turn_score

    def turn(self):
        roll = roll_die()

        if roll == 1:
            self.turn_score = 0
            print("Oh no, you rolled a 1")
            print(f"Your total score is {self.total_score}")
            return True
        else:
            print(f'You rolled a {roll}')
            self.turn_score += roll
            print(f"Current turn score: {self.turn_score}\n")

    def check_score(self):
        if self.turn_score + self.total_score >= 100:
            return True

# Returns a random integer between 1 and 6
def roll_die():
    die = [1,2,3,4,5,6]
    return random.choice(die)

# Main function
def main():
    print("Welcome to Pig the Dice Game!\n")
    print("The rules are simple:")
    print("1. The game is played with a single six-sided die.")
    print("2. There are 2 players. Players take turns rolling the die.")
    print("3. On a player's turn, they repeatedly roll the die until either:")
    print("3.1 They roll a 1, losing all points for that turn.")
    print("3.2 They hold their turn score, adding it to their total score.")
    print("4. If the player rolls a 1, they lose all points for that turn and their turn ends.")
    print("5. If the player holds, their turn ends and it switches to the other player.")
    print("6. The first player to reach 100 total points wins the game.")
    print("7. Points are accumulated turn-by-turn until a player reaches 100.\n")

    player1_name = input("Input your name player 1: ")
    player2_name = input("Input your name player 2: ")

    player1 = Player(player1_name, 0, 0)
    player2 = Player(player2_name, 0, 0)

    current_player = player1

    while True:
        option = input(f"\nWould you like to roll the dice, {current_player.name}? Yes or No ")
        # Input validation
        while option != "Yes" or option != "No":
            option = input(f"\nWould you like to roll the dice, {current_player.name}? Yes or No ")
            if option == "Yes" or option == "No":
                break
        
        # If the player says yes, call the turn() function
        # If the turn() function returns True, that means the player rolled a 1. Switch player.
        # Also, check if the player score reaches 100. If True, then game over.
        if option == "Yes":
            if current_player.turn():
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1
            if current_player.check_score():
                print(f"Congratulations {current_player.name}! You win!")
                break
        # If the player says no, add their turn_score to their total score, display their total score and reset their turn score.
        # Switch player
        elif option == "No":
            if current_player == player1:
                player1.total_score += player1.turn_score
                print(f"Your total score is {player1.total_score}\n")
                player1.turn_score = 0
                current_player = player2
            else:
                player2.total_score += player2.turn_score
                print(f"Your total score is {player2.total_score}")
                player2.turn_score = 0
                current_player = player1
main()
