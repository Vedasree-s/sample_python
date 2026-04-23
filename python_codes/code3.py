import random

# Sample list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Random choice from list
random_fruit = random.choice(fruits)
print(f"Random fruit: {random_fruit}")

# Random sample (multiple items)
random_sample = random.sample(fruits, 3)
print(f"Random sample: {random_sample}")

# Shuffle the list
random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# Random integer
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")