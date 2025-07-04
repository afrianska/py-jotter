# Write text
from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming.")

# Write multiple text
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)
