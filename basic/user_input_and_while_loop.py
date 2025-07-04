# User Input and while loop
# How the input() function works
"""
# Parrot
message = input("Tell me something, and I will reapeat it back to you: ")
print(message)

# Greeter
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Other Greeter
prompt = "If you can share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to accept Numerical input
# rollercoaster
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("n\You'll be able to ride when you're a little older.")
"""

# The Modulo Operator
"""
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
"""

# Even and Odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
