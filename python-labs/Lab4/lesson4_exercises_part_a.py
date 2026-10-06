# Part A, Function fundamentals

# 1. Write greet(), show_course_name(), print_separator(), and call each more than once
def greet():
    print("Welcome!")


def show_course_name():
    print("Python Fundamentals")


def print_separator():
    print()


greet()
print_separator()
show_course_name()
greet()
print_separator()
show_course_name()


# 2. Write greet_person(name), and introduce(name, city)
def greet_person(name):
    print(f"Hello, {name}!")


def introduce(name, city):
    print(f"My name is {name}, and I live in {city}")

greet_person("Adam")
introduce("James", "Florida")


# 3. Write add(a, b), subtract(a, b), multiply(a, b), and divide(a, b), they must return a value
def add(a, b):
    return a + b

print(add(1, 3))


def subtract(a, b):
    return a - b

print(subtract(1, 3))


def multiply(a, b):
    return a * b

print(multiply(1, 3))


def divide(a, b):
    return a / b

print(divide(1, 3))


# 4. Demonstrate parameter vs argument in comments using a function
# def add(a, b)  # < variables inside parentheses when defining a function
# is what the function can take, these are parameters

print(add(6, 2))  # < variables inside parentheses when calling a function
# is what the function passes in, these are arguments


# 5. Create calculate_area(width, height), and use return value in another calculation
def calculate_area(width, height):
    return width * height

print(divide(calculate_area(20, 30), 2))