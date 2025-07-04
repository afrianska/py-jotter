# Reading the contents of file
from pathlib import Path

path = Path("pi_digits.txt")

contents = path.read_text()
print(contents)

print("\n-----")
contents = contents.rstrip()
print(contents)

print("\n-----")
contents = path.read_text().rstrip()
print(contents)

print("\n-----")
# Accessing a file's lines
lines = contents.splitlines()
for line in lines:
    print(line)

print("\n-----")
# Working with a file's contents
pi_string = ""
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

print("\n-----")
# Large files: on million digits
path_million = Path("pi_million_digits.txt")
contents_million = path_million.read_text()
lines_million = contents_million.splitlines()
pi_million_string = ""
for line in lines_million:
    pi_million_string += line.lstrip()
print(f"{pi_million_string[:66]}...")
print(len(pi_million_string))
