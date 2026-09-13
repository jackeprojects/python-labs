# Part A, Warm-up: Python basics

# 1. Print name, course name and today's study goal on seperate lines
print("Name")
print("Course name")
print("Today's study goal")


# 2. Variables for a persons name, age, height, and if theyre a student
person_name = "name"
person_age = 35
person_height_meters = 1.75
person_is_student = False

print(person_name)
print(person_age)
print(person_height_meters)
print(person_is_student)
print(type(person_name))
print(type(person_age))
print(type(person_height_meters))
print(type(person_is_student))


# 3. Change and print a variables data type
print(type(person_is_student))
print(str(type(person_is_student)))  # Change the variable from type bool to type str
# This means that in Python, a variable's type dynamically changes based on its value


# 4. Create and calculate two numeric variables
first_number = 3
second_number = 8

print(f"Addition: {first_number} + {second_number} = {first_number + second_number}")
print(f"Subtraction: {first_number} - {second_number} = {first_number - second_number}")
print(f"Multiplication: {first_number} * {second_number} = {first_number * second_number}")
print(f"Normal division: {first_number} / {second_number} = {first_number / second_number}")
print(f"Floor division: {first_number} // {second_number} = {first_number // second_number}")
print(f"Remainder: {first_number} % {second_number} = {first_number % second_number}")
print(f"Exponentiation: {first_number} to the power of {second_number} = {first_number ** second_number}")


# 5. Examples for explicit type conversions
str_to_int = input("Enter a number: ")
#print(str_to_int + 2)  # Gives a TypeError, can't add since str_to_int is a str
print(int(str_to_int) + 2)

# I can't think of an example where int to float is absolutely necessary

age = 24
#print("I am " + age + " years old!")  # Also give TypeError, can only combine str with str
print("I am " + str(age) + " years old!")