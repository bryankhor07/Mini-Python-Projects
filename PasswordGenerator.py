import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd  += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        elif special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def main():
    min_length = int(input("How long do you want your password to be?"))
    has_numbers = input("Do you want to include numbers in your password? (Y/N)") == "Y"
    has_special = input("Do you want to include special characters in your password? (Y/N)") == "Y"


    print("Here's your generated password: " + generate_password(min_length, has_numbers, has_special))

main()