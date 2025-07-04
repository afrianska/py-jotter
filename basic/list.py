# In Python, sqare brackets [] indicate a list
female_gods_greek = ["athena", "aprodhite", "artemis", "hera"]
print(female_gods_greek)

print("-----")
# Accessing element in a list
print(female_gods_greek[0])
print(female_gods_greek[2].title())

print("-----")
# Index positions
print(female_gods_greek[1])

# value is hera, this special syntax accessing last elementi
print(female_gods_greek[-1])
print(female_gods_greek[-3])

print("-----")
# Using individual value from a list
message = f"My favorite god was {female_gods_greek[2].upper()}"
print(message)

print("-----")
# Modifying, Adding and removing element in list
## Modifying
car_brands = ["mercedes", "toyota", "byd", "tesla"]
print(car_brands)

car_brands[0] = "audi"
print(car_brands)

print("-----")
# Adding element to end of a list
car_brands.append("bmw")
print(car_brands)

print("-----")
## Insert element into a list
car_brands.insert(2, "fiat")
print(car_brands)

print("-----")
# Removing element from a list
## with del
del car_brands[0]
print(car_brands)

print("-----")
## with pop()
popped_car_brands = car_brands.pop()
print(car_brands)
print(popped_car_brands)

last_owned = car_brands.pop()
print(f"The last car brand I owned was a {last_owned.title()}.")

first_owned = car_brands.pop(0)
print(f"The first car brand I owned was a {first_owned.title()}")

print("-----")
# Removing using remove()
print(car_brands)
car_brands.remove("byd")
print(car_brands)

italian_brand = "fiat"
car_brands.remove(italian_brand)
print(car_brands)
print(f"\nA {italian_brand.title()} is italian brand.")

print("-----")
# Organizing a list permanently using sort()
fishes = ["shark", "whale", "dolpin", "tuna"]
print(fishes)

fishes.sort()
print(fishes)

fishes.sort(reverse=True)
print(fishes)

print("-----")
# Organizing a list temporarily using sorted()
print("Here is the original list:")
print(fishes)
print("\nHere is the sorted list:")
print(sorted(fishes))
print("\nHere is the original list again:")
print(fishes)

print("-----")
# Print in reverse verison
fishes.reverse()
print(fishes)

print("-----")
# Finding the lenght of a list
print(len(fishes))

print("-----")
# Avoiding index errors when working with lists
# print(fishes[5]) # we only have length 4, if we put 5 of course will error
