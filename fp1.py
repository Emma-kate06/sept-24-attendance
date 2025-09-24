import random
import time

# Greeting
print("Welcome to the PowerBall Lottery Number Generator!")

# Ask for the user's name and store it
varUserName = input("What is your name? ")

# Greet the user by their name
print(f"Hello, {varUserName}! Let's generate your lucky numbers.\n")
print("Generating your numbers now...")
print("...")
time.sleep(0.25)

# Generate the first five numbers (white balls, 1-69) and store them in variables
number1 = random.randint(1, 69)
number2 = random.randint(1, 69)
number3 = random.randint(1, 69)
number4 = random.randint(1, 69)
number5 = random.randint(1, 69)

# Print the first five numbers with a small delay between each
print(f"White balls: {number1}", end="")
time.sleep(0.25)
print(f"  {number2}", end="")
time.sleep(0.25)
print(f"  {number3}", end="")
time.sleep(0.25)
print(f"  {number4}", end="")
time.sleep(0.25)
print(f"  {number5}", end="")
time.sleep(0.25)

# Generate the sixth number (red ball, 1-26) and store it
red_ball = random.randint(1, 26)

# Print the final number in red with a larger space
# The ANSI escape codes "\033[91m" and "\033[0m" are used to change text color.
# 91m is the code for bright red, and 0m resets the color.
print(f"    \033[91mRed ball: {red_ball}\033[0m\n")

# Farewell message
print("Good luck with your ticket!")
