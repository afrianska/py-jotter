# Making Numerical List

# Using the range() function
for value in range(1, 5):
    print(value)

print("-----")

# Using range() to make a list of numbers
numbers = list(range(1, 6))  # will create a list or array numbers
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2

squares.append(square)
print(squares)

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions
squares2 = [value**2 for value in range(1, 11)]
print(squares2)
