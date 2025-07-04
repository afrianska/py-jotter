# Fucntion
# Defining a function
"""
def greet_user():
    # Display a simple greeting
    print("Hello!")

greet_user()
"""

# Passing Information to a Function
"""
def greet_user(username):
    # Display a simple greeting.
    print(f"Hello, {username.title()}!")

greet_user("jolly")
"""

# Arguments and Parameters
"""
From example above we can define what's argument and parameter
'username' in greet_user(username) is called parameter.
'jolly' in greet_user('jolly') is called argument.
"""


# Passing arguments
# Positional argument
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("dog", "merry")

# Multiple function calls
describe_pet("cat", "gordon")
describe_pet("gose", "lily")

# Order matters in positional arguments
describe_pet("gordon", "cat")  # the result will reverse than above.

# Keyword Arguments
describe_pet(animal_type="bird", pet_name="james")
describe_pet(pet_name="james", animal_type="bird")


# Default value
def describe_pet_with_default_value(pet_name, animal_type="dog"):
    print(f"\nI have {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_with_default_value(pet_name="leo")
describe_pet_with_default_value("leo")
describe_pet_with_default_value(pet_name="jan", animal_type="monkey")

# Equivalent function calls
describe_pet_with_default_value("yahya")
describe_pet_with_default_value(pet_name="dongker")
describe_pet_with_default_value("luke", "cat")
describe_pet_with_default_value(pet_name="luke")
describe_pet_with_default_value(animal_type="cat", pet_name="luke")

# Avoid argument errors
describe_pet_with_default_value()  # this will be error, need argument to fill parameter of function
