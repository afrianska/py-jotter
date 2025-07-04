# Return Value
# Return a simple value
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("khatia", "buniatishvili")

print(musician)


# Making an argument optional
def get_formatted_name_opt(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()


footballer_full_name = get_formatted_name_opt("florian", "wirtz", "richard")
footballer_non_full_name = get_formatted_name_opt("florian", "wirtz")
print(footballer_full_name)
print(footballer_non_full_name)
