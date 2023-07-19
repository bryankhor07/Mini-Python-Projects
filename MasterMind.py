import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# Generate a random color code
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        # User input
        guess = input("Guess: ").upper().split(" ")

        # Check if the user input the valid code length.
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        # Check if the color that the user guessed is valid.
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Initialize the color in the color_counts dictionary if it doesn't exist.
    # Increment the color count everytime it encounters that specific color.
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # The zip function is going to take my two arguments and combine them into tuples
    for guess_color, real_color in zip(guess, real_code):
        # If the guess_color is equal to the real_color, then increment correct_pos by 1 and 
        # decrement the color count in the dictionary by 1
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # This loop will check if the user guessed the correct color but it is in the incorrect position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

# Run the game
def game():
    print(f"Welcome to MasterMind! You have {TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)
    print()

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        # If the correct positions equals to the code length, then the user guessed the code and break out the loop.
        if correct_pos == CODE_LENGTH:
            print(f"\nYou guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        # Print this if the user ran out of tries and reveal the code to the user.
        print("\nYou ran out of tries, the code was:", *code)

game()