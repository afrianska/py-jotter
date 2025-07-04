# Using a while loop with lists and dictionaries
# Moving items from one list to another

# Start with users that need to be verified,
# and an empry list to hold confirmed users.
"""
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# Verify each verified user into the list of confirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
"""

"""
print("\n-----")
# Removing all instances of specific values from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)
"""

print("\n-----")
# Filling a dictionary with user input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person\s name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (Y = Yes/ N = No) ")
    if repeat == "N" or repeat == "n":
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
