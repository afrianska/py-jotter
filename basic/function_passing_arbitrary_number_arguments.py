# Passing an arbitrary number of arguments
# asterisk in the parameter name to tell python to make a tuple.
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

print("\n-----")


# Mixing positional and arbitrary arguments
def make_pizza_v2(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza_v2(16, "pepperoni")
make_pizza_v2(12, "mushooms", "green peppers", "extra cheese")


print("\n-----")


# Using arbitrary keyword arguments
# double asterisk ** in python to create dictionary or object
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
