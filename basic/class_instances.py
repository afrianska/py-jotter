# Working with classes and instances

# The car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

print("\n-----")


# Setting a devault value for attibute
class CarV2:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = CarV2("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

print("\n-----")
# Modifying attribute values
# Modifying an attribute's value directly
"""From above class"""
my_new_car_v2 = CarV2("byd", "byd m6", 2024)
my_new_car_v2.odometer_reading = 23

print(my_new_car_v2.get_descriptive_name())
my_new_car_v2.read_odometer()

print("\n-----")


# Modifying an attribute's values through a method
class CarV3:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage


my_new_car_v3 = CarV3("byd", "byd seal", 2024)
my_new_car_v3.update_odometer(26)

print(my_new_car_v3.get_descriptive_name())
my_new_car_v3.read_odometer()

print("\n-----")


# We can extend the method
class CarV4:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car_v4 = CarV4("byd", "byd seal", 2024)
my_new_car_v4.update_odometer(50)

print(my_new_car_v4.get_descriptive_name())
my_new_car_v4.read_odometer()

my_new_car_v4.update_odometer(4)

print("\n-----")


# Incrementing an attribute's value trough a method
class CarV5:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car_v5 = CarV5("subaru", "outback", 2019)
my_new_car_v5.update_odometer(23_500)

print(my_new_car_v5.get_descriptive_name())
my_new_car_v5.read_odometer()

my_new_car_v5.increment_odometer(100)
my_new_car_v5.read_odometer()
