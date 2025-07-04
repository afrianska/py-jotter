from pathlib import Path
import json

'''
def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username.lower())
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username.lower()}")
'''


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username.lower())
    path.write_text(contents)
    return username


def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username.lower()}!")


greet_user()
