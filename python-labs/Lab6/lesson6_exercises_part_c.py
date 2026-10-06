# Part C, enumerate

# 1. Print a playlist with numbering starting at 1 using enumerate
songs = ["Fireworks", "Shut It Down", "The Resistence"]
for index, song in enumerate(songs, start=1):
    print(index, song)


# 2. Give a list of tasks, print "Task1:", "Task2:" etc
tasks = ["Cook food", "Take out the trash", "Walk the dog"]
for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")


# 3. Find and print indexes of all values above a threshold
numbers = [1, 152, 84, 46, 5, 78, 32]
threshold = 58
for index, number in enumerate(numbers):
    if number >= threshold:
        print(index)


# 4. Rewrite a range(len(...)) loop using enumerate and explain why the new version is cleaner
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):
    print(i, fruits[i])

for index, fruit in enumerate(fruits):
    print(index, fruit)  # no need for manual indexing, and reads more naturally