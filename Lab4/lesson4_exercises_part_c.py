# Part C, Defaults and keyword arguments

# 1. Create greet(name, greeting="Hello"), test positional, and keyword arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}."

print(greet("Josh"))
print(greet("Josh", "HEY"))
print(greet("Josh", greeting="Hi"))


# 2. Create calculate_price(price, quantity=1, discount=0), return final cost
def calculate_price(price, quantity=1, discount=0):
    return (price - discount) * quantity

print(calculate_price(300, 2))


# 3. Create create_profile(name, city="Unknown", active=True), return dictionairy
def create_profile(name, city="Unknown", active=True):
    return {"name": name, "city": city, "active": active}

print(create_profile("Jason", "Washington"))


# 4. Call function using keyword arguments in different order than definition
print(calculate_price(4600, discount=2500, quantity=3))


# 5. Write invalid default-parameter as comment and explain why it's invalid
# def greet(greeting="Hello", name)  # SyntaxError
# Parameter with no default value must come before parameters that do