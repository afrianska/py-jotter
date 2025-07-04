# Function return a dictionary
"""
def build_person(first_name, last_name):
    person = {"first": first_name, "last": last_name}
    return person


actors = build_person("emma", "stones")
print(actors)


# another example
def build_person_opt(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age

    return person


musician = build_person_opt("michael", "bubble", age=40)
print(musician)
"""


# Using a fucntion whti a while loop
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == "q":
        break

    l_name = input("Last Name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
