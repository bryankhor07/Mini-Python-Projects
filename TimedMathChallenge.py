import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

# This function is used to generate a math problem and returns the expression and the answer.
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

# Store the time when the user begins the quiz.
start_time = time.time()

# Generate 10 problems, get the user answer and increment wrong by 1 ifthe user didn't get the correct answer.
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
    if guess != str(answer):
        wrong += 1

# Store the time when the user ends the quiz
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
accuracy = ((TOTAL_PROBLEMS-wrong) / TOTAL_PROBLEMS) * 100
print("Your accuracy was " + str(accuracy) + "%")