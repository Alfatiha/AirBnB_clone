import random

# Get the user's name
name = input("What is your name? ")

# Generate 10 random numbers
random_numbers = []
for i in range(10):
  random_numbers.append(random.randint(1, 100))

# Print the user's name and the random numbers
print(f"Hello, {name}! Here are 10 random numbers:")
print(random_numbers)
