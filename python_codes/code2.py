# Sample code demonstrating F-strings in Python

name = "Alice"
age = 30
city = "New York"

# Basic F-string usage
print(f"Hello, my name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")

# F-string with expressions
print(f"In 5 years, I will be {age + 5} years old.")

# F-string with formatting
price = 19.99
print(f"The price is ${price:.2f}")

# F-string with f-string inside
message = f"Hello {name}, you are {age} years old!"
print(message)

# F-string with dictionaries
person = {"name": "Bob", "age": 25}
print(f"Person: {person['name']}, Age: {person['age']}")