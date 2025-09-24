# Import the random module to generate random numbers
import random
# Import the time module to add delays (for extra practice)
import time

# Greeting and getting the user's name
print("Welcome to the PowerBall Number Generator!")
varUserName = input("What is your name? ")

# Greeting the user by their name
print(f"Hello, {varUserName}! Here are your lucky numbers:")

# Generating the five white ball numbers
ball1 = random.randint(1, 69)
time.sleep(1) # Optional delay
ball2 = random.randint(1, 69)
time.sleep(1) # Optional delay
ball3 = random.randint(1, 69)
time.sleep(1) # Optional delay
ball4 = random.randint(1, 69)
time.sleep(1) # Optional delay
ball5 = random.randint(1, 69)
time.sleep(1) # Optional delay

# Generating the one red Powerball number
powerball = random.randint(1, 26)

# Printing the numbers with the specified spacing
print(f"{ball1}  {ball2}  {ball3}  {ball4}  {ball5}    {powerball}")

# Farewell message
print(f"\nGood luck, {varUserName}!")