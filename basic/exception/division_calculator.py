# Zero Division Error: devision by zero
# print(5 / 0) # will error

# Using exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

"""
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("Second number: ")
    if second_number == "q":
        break

    answer = int(first_number) / int(second_number)
    print(answer)
"""

# The else block
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't devide by 0")
    else:
        print(answer)
