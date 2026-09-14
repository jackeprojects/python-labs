# Part G, Stretch challenges

# 1. Given two lists of usernames, determine duplicates, unique usernames, using sets
usernames_1 = ["john_doe", "jane_doe9", "shaun_23"]
usernames_2 = ["cool_kyle", "aust1n_3", "jane_doe9"]

set_1 = set(usernames_1)
set_2 = set(usernames_2)

duplicates = set_1 & set_2
uniques_1 = set_1 - set_2
uniques_2 = set_2 - set_1
all_unique_usernames = set_1 | set_2

print(duplicates)
print(uniques_1)
print(uniques_2)
print(all_unique_usernames)


# 2. Design a nested collection for a small online course platform
course_platform = [
    {"course": "Python Fundementals", "teacher": "Kyle", "students": ["Liam", "Sofia", "Noah"], "topics": ["Variables", "Loops", "Functions"]},
    {"course": "Web Development", "teacher": "Joan", "students": ["Emma", "Oliver"], "topics": ["HTML", "CSS"]},
    {"course": "Databases", "teacher": "Lara", "students": ["Ava", "Lucas", "Mia"], "topics": ["SQL", "Indexing"]}
]
print(course_platform[0]["students"][1])


# 3. Crate a dicionary-based inventory for 5 producs, update stock value manually, and calculate total units
inventory = {"Keyboards": 15, "Mice": 22, "Monitors": 8, "Webcams": 12, "Headsets": 19}

total_units = sum(inventory.values())
print(total_units)

inventory["Keyboards"] = 10  # 5 keyboards get bought
inventory["Monitors"] = 5  # 3 monitors get bought

total_units = sum(inventory.values())
print(inventory)
print(total_units)


# 4. Compare list vs tuple vs set vs dictionary, give a situation where each fit the best
# List, ordered, mutable, allows duplicates, best for to-do lists
# Tuple, ordered, immutable, allows duplicates, best for protected data that shouldnt be changed
# Set, unordered, mutable, doesn't allow duplicates, best for tracking unique elements
# Dictionary, ordered, mutable, allows duplicate values, not keys, best for looking up values by names