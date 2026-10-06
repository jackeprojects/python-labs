# Part A, Lists

# 1. List of 8 programming languages, acces first, last, third, and second-to-last value
programming_languages = ["Python", "C#", "C++", "C", "F#", "Java", "Rust", "R"]
print(programming_languages[0])
print(programming_languages[-1])
print(programming_languages[-2])
print(programming_languages[2])


# 2. Print three slices of the list, and in reverse order
print(programming_languages[0:])
print(programming_languages[1:3])
print(programming_languages[3:-3])
print(programming_languages[::-1])


# 3. Use append, insert, remove, pop, after each operation print changed list
programming_languages.append("PowerShell")
print(programming_languages)
programming_languages.insert(0, "GDScript")
print(programming_languages)
programming_languages.remove("C")
print(programming_languages)
programming_languages.pop(4)
print(programming_languages)


# 4. Calculate numeric lists length, minimum, maximum and sum using in-built functions
numeric_list = [2, 4, 1, 5, 6, 1, 9, 2]

print(len(numeric_list))
print(min(numeric_list))
print(max(numeric_list))
print(sum(numeric_list))


# 5. Sort lists ascending and descending, explain difference between sort() and sorted()
first_list = [6, 21, 9, -2, 2, 98, 2,  1]
second_list = [7, 14, 8, 5, 9, 2, 0, 1]

first_list.sort()
print(first_list)
second_list_sorted = sorted(second_list, reverse=True)
print(second_list_sorted)
# .sort() modifies the list and doesnt return anything
# .sorted() doesnt modify the list and instead returns a copy of it


# 6. Demonstrate reference/copy issue using list_b = list_a, fix it with copy()
list_a = ["Apple", "Banana", "Orange"]
list_b = list_a
print(f"List a: {list_a}")
print(f"List b: {list_b}")

list_b.append("Kiwi")
print(f"List a: {list_a}")
print(f"List b: {list_b}")

list_b = list_a.copy()
list_b.append("Melon")
print(f"List a: {list_a}")
print(f"List b: {list_b}")