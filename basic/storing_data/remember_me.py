# Saving and reading user-generated data
from pathlib import Path
import json

path = Path("username.json")
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    # To test this block, delete 'usernam.json' file
    username = input("What is your name? ")
    contents = json.dumps(username.lower())
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username.lower()}")
