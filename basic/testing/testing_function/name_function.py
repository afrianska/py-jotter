# Testing a function
def get_formatted_name(first, last, middle=""):
    # full_name = f"{first} {last}"

    # try to make false test
    full_name = f"{first} {middle} {last}"

    # respond to fix the code
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
