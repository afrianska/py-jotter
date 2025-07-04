# IF STATEMENTS
# Simple Example
cars = ["byd", "telsa", "fiat", "wuling"]

for car in cars:
    if car.lower() == "byd".lower():
        print(car.upper())
    elif car.lower() == "fiat".lower():
        print(car.lower())
    else:
        print(car.title())

print("\n-------")
# Conditional Test
# Checking for equality
fruit = "Apple"
print(fruit.lower() == "apple")

print("\n-------")
# Checking for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

print("\n-------")
# Numerical Comparisons
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

print("\n-------")
# Checking multiple condition
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

print("\n-------")
# Checking wehter a value is in a list
requested_toppings = ["mushrooms", "onions", "pineaple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)

print("\n-------")
# Checking whether a value is not in a list
banned_users = ["artemis", "athena", "hera"]
user = "aphrodite"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
