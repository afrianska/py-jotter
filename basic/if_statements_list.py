# Using if statements with List
# Checing for special items
requested_toppings = ["mushrooms", "green peppers", "extra chees"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

print("\n-------")
# Checking that a list is not empty
requested_drinks = []

if requested_drinks:
    for requested_drink in requested_drinks:
        print(f"Adding {requested_drink}.")
        print("\nFinished making your drink!")
else:
    print("Are you sure you are not thristy?")


print("\n-------")
# Using multiple list
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
