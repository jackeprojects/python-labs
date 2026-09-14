# Part C, Sets

# 1. Create a list with duplicate course names, convert to a set, and compare lengths
course_list = ["Python Fundementals", "Python Fundementals", "Python Fundementals"]
print(len(course_list))
course_set = set(course_list)
print(len(course_set))
print(course_list)
print(course_set)


# 2. Find shared, unique, and combined skills of two developers
dev_1 = {"C#", "XAML", ".NET", "ASP.NET", "SQL"}
dev_2 = {"Python", "C#", "SQL", "CSS", "HTML"}
dev_1_unique_skills = dev_1 - dev_2
shared_skills = dev_1 & dev_2
combined_skills = dev_1 | dev_2

print(dev_1_unique_skills)
print(shared_skills)
print(combined_skills)


# 3. Create a set, practice add, remove/discard and membership testing
consoles = {"Playstation 2", "Xbox", "Playstation 3", "Xbox 360", "Nintendo Wii"}
print(consoles)
consoles.remove("Nintendo Wii")
print(consoles)

consoles.add("Nintendo 3DS")
print(consoles)

consoles.remove("Playstation 3")
print(consoles)

consoles.discard("Nintendo Switch")
print(consoles)

if "Xbox" in consoles:
    print("Xbox exists!")


# 4. Explain why a set is a better choice than a list in a real-world uniqueness problem
# Easier for tracking unique items like id-numbers since duplicates are ignored,
# unlike a list, which doesn't ignore duplicates