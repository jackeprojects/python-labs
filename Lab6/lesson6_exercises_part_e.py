# Part E, sorted and lambda

# 1. Sort a list of words by length using sorted(..., key=...)
fruits = ["apple", "orange", "pear", "grapefruit"]
sorted_fruits = sorted(fruits, key=len)
print(fruits)
print(sorted_fruits)


# 2. Sort a list of student dictionaries by score ascending, and descending
students = [{"name": "Cory", "active": False, "score": 30},
            {"name": "Angel", "active": True, "score": 78},
            {"name": "Andrew", "active": True, "score": 57}]

students_ascending = sorted(students, key=lambda student: student["score"])
students_descending = sorted(students, key=lambda student: student["score"], reverse=True)
print(students_ascending)
print(students_descending)


# 3. Sort producs by price using a lambda
products = [{"name": "Headset", "price": 800},
            {"name": "Keyboard", "price": 1900},
            {"name": "Mouse", "price": 1200}]
products_sorted = sorted(products, key=lambda product: product["price"])
print(products_sorted)


# 4. Sort people by last name when each item is a dictionary containing first_name and last_name
people = [{"first_name": "Joe", "last_name": "Smith"},
          {"first_name": "Andrew", "last_name": "Andersson"},
          {"first_name": "Jane", "last_name": "Doe"}]
people_sorted = sorted(people, key=lambda person: person["last_name"])
print(people_sorted)


# 5. Write a normal named function for a sort key, then replace it with lambda. Compare when each is clearer
def get_first_name(person):
    return person["first_name"]

people_sorted_normal = sorted(people, key=get_first_name)
print(people_sorted_normal)

people_sorted_lambda = sorted(people, key=lambda person: person["first_name"])
print(people_sorted_lambda)

# Personally I think that the lambda version is cleaner, because it doesnt split up the process