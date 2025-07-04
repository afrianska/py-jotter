# Working with Part of List

# Slicing a list
players = ["virgil", "salah", "gakpo", "robo", "macca"]

print(players[0:3])
print(players[1:4])
print(players[2:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a slice
players_tennis = ["nadal", "sinner", "rune", "djokovic", "alcaraz"]
print("Here are the first three players on the court:")
for player in players_tennis[:3]:
    print(player.title())

# Copying a list
my_foods = ["satay", "pecel", "rendang", "mie ayam", "soto"]
friend_foods = my_foods[:]
# friend_foods = my_foods # Something like this doesn't work

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("bakso")
friend_foods.append("ketoprak")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
