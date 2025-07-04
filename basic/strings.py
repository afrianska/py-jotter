string_with_single_quotes = "This is string"
print(string_with_single_quotes)

string_with_double_quotes = "This is also string"
print(string_with_double_quotes)

print("-------------")
# Change case in a string
name = "artemis saikrama"

print(name.title())  # to Capitalize
print(name.upper())  # to Upper
print(name.lower())  # to lower

print("-------------")
# Using variable in a string
first_name = "artemis"
last_name = "saikrama"
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}"
print(message)

print("-------------")
# Adding whitespace to string with tabs or newlines
print("Python")
print("\tPython")  # tab
print("Languages:\nPython\nRust\nJavaScript")
print("Languages:\n\tPython\n\t\tRust\n\t\t\tJavaScript")

print("-------------")
# Stripping whitespace
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

print("-------------")
# Removing prefixes
crafting_web_url = "https://crafting.web.app"
print(crafting_web_url.removeprefix("https://"))
simple_url = crafting_web_url.removeprefix("https://")
print(simple_url)

print("-------------")
