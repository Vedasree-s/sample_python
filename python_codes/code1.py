# Program to add two even numbers

# Get first even number from user
num1 = int(input("Enter first even number: "))

# Validate that num1 is even
while num1 % 2 != 0:
    print("Please enter an even number!")
    num1 = int(input("Enter first even number: "))

print("U r giving an even number!")

# Get second even number from user
num2 = int(input("Enter second even number: "))

# Validate that num2 is even
while num2 % 2 != 0:
    print("Please enter an even number!")
    num2 = int(input("Enter second even number: "))

print("U r giving an even number!")

# Add the two even numbers
result = num1 + num2

# Display the result
print(f"{num1} + {num2} = {result}")
