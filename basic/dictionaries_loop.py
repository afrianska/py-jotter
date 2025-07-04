# Looping through a dictionary
# Looping through all key value pairs
user_0 = {"username": "efermi", "first": "enrico", "last": "fermi"}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("-----")
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n-----")
# Looping through all they keys in a dictinioray
favorite_languages_0 = {
    "kelly": "javascript",
    "lily": "c",
    "andy": "rust",
    "emma": "python",
}
for name in favorite_languages.keys():
    print(name.title())

print("\n")
# More complex example
friends = ["andy", "lily"]
for name in favorite_languages_0.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages_0[name].title()
        print(f"\t{name.title()}, I see you love {language}")

print("\n")
if "erin" not in favorite_languages_0.keys():
    print("Erin, please take your poll!")

print("\n-----")
# Looping through a dictionay's keys in a particular order
favorite_languages_1 = {
    "artemis": "javascript",
    "hera": "rust",
    "zeus": "python",
    "aprodhite": "golang",
}

for name in sorted(favorite_languages_1.keys()):
    print(f"{name.title()}, thank you for taking me poll.")

print("\n-----")
# Looping through all values in a dictionary
# Use dictionary above
print("The following languages have been mentioned:")
for language in favorite_languages_1.values():
    print(language.title())

print("\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages_1.values()):
    print(language.title())
