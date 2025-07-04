# Python Dictionaries
# I'm from javascript programming language, this on is similar with objects
# A simple dictionary
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print("-----")
# Accessing value in dictionary
alien_1 = {"color": "red", "points": 5}
new_points = alien_1["points"] * 2

print(f"You just earned {new_points} points!")

print("-----")
# Adding new key-value pairs
alien_3 = {"color": "blue", "points": 6}
print(alien_3)

alien_3["x_position"] = 0
alien_3["y_position"] = 25
print(alien_3)

print("-----")
# Starting with an empry dictionary
alien_4 = {}
print(alien_4)

alien_4["color"] = "purple"
alien_4["points"] = 7
print(alien_4)

print("-----")
# Modifying values in a dictionary
alien_5 = {"color": "grey"}
print(f"The alien is {alien_5['color']}.")

alien_5["color"] = "yellow"
print(f"The alien is now {alien_5['color']}")

print("-----")
# The more Interesting example
alien_6 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_6['x_position']}.")

## Move the alien to the right
## Determine how far to move the alien based on its current speed
if alien_6["speed"] == "slow":
    x_increment = 1
elif alien_6["speed"] == "medium":
    x_increment = 2
else:
    x_incerment = 3

## The new position is the old position plus the increment
alien_6["x_position"] = alien_6["x_position"] + x_increment

print(f"New position: {alien_6['x_position']}")

print("-----")
# Removing key-value pairs
alien_7 = {"color": "orange", "points": 5}
print(alien_7)

del alien_7["points"]
print(alien_7)

print("-----")
# A dictionary of similar objects
favorite_languages = {"jen": "python", "sarah": "c", "edward": "rust", "phil": "python"}
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

print("-----")
# Using get() to access values
alien_8 = {"color": "green", "speed": "slow"}
# print(alien_8['points']) # this will be error couse no 'points' in dictionary alien_8

point_value = alien_8.get("points", "No point value assigned.")
print(point_value)
