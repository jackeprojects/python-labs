# Part F, break and continue

# 1. Loop through numbers 1-100 and stop when you reach the first number divisible by 7, and 9
for number in range(1, 101):
    if number % 7 == 0 and number % 9 == 0:
        print(number)
        break


# 2. Loop through a list of strings and skip empty strings using continue
greetings = ["hey", "hello", "greetings", "", "howdy", ""]
for greeting in greetings:
    if not greeting:
        continue
    else:
        print(greeting)


# 3. Search a list for a target name, print 'found' and break when it appears,
# otherwise, explain how you know it was not found
greeting_found = False
for greeting in greetings:
    if greeting == "greetings":
        print("Found")
        greeting_found = True
        break
if not greeting_found:
    print("Checked all items, no match")


# 4. Process a list of numeric values where negative values should be skipped
# and processing stops completelywhen teh value 999 appears
numbers = [342, -45, 1234, -68, 37, 543, 999, -1]
for number in numbers:
    if number < 0:
        continue
    elif number == 999:
        break
    print(number)
