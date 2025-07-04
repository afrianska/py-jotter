# Nesting
# A list of Dictionaries
alien_0 = {
    "color": "green",
    "points": 5,
}
alien_1 = {
    "color": "yellow",
    "points": 10,
}
alien_2 = {
    "color": "red",
    "points": 15,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n-----")
# Another example
# Make an ampty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

print("\n")
# With condition
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

print("\n")
# With condition
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15


for alien in aliens[:5]:
    print(alien)
print("...")

print("\n-----")
# A list i a Dictionay
# Store information about a pizza being ordered.
pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

print("\n------")
# Other example with favorite languages
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phill": ["pythong", "haskell"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

print("\n-----")
# A Dictionary in a dictionady
users = {
    "zhanglulu": {"first": "zhang", "last": "lu", "location": "Chongqing"},
    "jacobvim": {"first": "jacob", "last": "vimuser", "location": "amsterdam"},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
