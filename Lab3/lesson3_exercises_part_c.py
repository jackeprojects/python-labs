# Part C, For loops

# 1. Loop over a list of names and print a numbered greeting for each.
names = ["Andrew", "Alex", "Carl", "Emma", "Seth", "Karen"]

for i, name in enumerate(names, start=1):
    print(f"{i}. Hi {name}!")


# 2. Loop over numbers 1-50 and print only even numbers
for number in range(1, 51):
    if number % 2 == 0:
        print(number)


# 3. Calculate sum of a list manually using loop rather than sum()
numbers = [200, 237, 14, -56, 345, -124, 465, -645]
numbers_sum= 0
for number in numbers:
    numbers_sum += number

print(numbers_sum)


# 4. Find the largest number in a list manually without max()
biggest_number = numbers[0]
for number in numbers:
    if biggest_number < number:
        biggest_number = number

print(biggest_number)


# 5. Count how many words in a list have more than 5 chars
words = ["door", "construct", "corporate", "unilateral"]
count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(count)


# 6. Given a list of scores, count passes and failures using a threshold of 70
scores = [98, 43, 76, 38, 42, 98, 100]

passes = 0
failures = 0
for score in scores:
    if score >= 70:
        passes += 1
    else:
        failures += 1

print(passes)
print(failures)


# 7. Loop over a dictionary using keys, values, items(), in three separate examples
game = {"name": "Fallout", "release_date": 1997, "genre" : "CRPG"}
for item in game.items():
    print(item)
for key in game.keys():
    print(key)
for value in game.values():
    print(value)