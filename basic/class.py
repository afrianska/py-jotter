# Creating and using a class
# Creating the dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


# making an instance from a class
my_dog = Dog("Willie", 6)
print(my_dog)

print("\n-----")
# accesing atrribute
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print("\n-----")
# calling method
my_dog.sit()
my_dog.roll_over()

print("\n-----")
# Creating multiple instances
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
