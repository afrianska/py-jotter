# Passing a list
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["artemis", "hera", "aprodhite"]
greet_users(usernames)

print("\n-----")
# Modifying a list in a function
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")

    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

print("\n-----")


# Try to organize
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")

    for completed_model in completed_models:
        print(completed_model)


unprinted_designs_2 = ["phone case", "phone holder", "phone rak"]
completed_models_2 = []

print_models(unprinted_designs_2, completed_models_2)
show_completed_models(completed_models_2)

print("\n-----")
# Preventing a function from modifying a list
print_models(completed_models_2[:], completed_models_2[:])
show_completed_models(completed_models_2)
