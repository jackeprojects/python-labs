# Part B, Dictionary and set comprehension

# 1. Create a dictionary mapping numbers 1-10 to their squares
number_squares = {number: number ** 2 for number in range(1, 11)}
print(number_squares)


# 2. Given a list of words, create a dictionary mapping each word to its length
words = ["python", "code", "developer", "loop", "function"]

words_length = {word: len(word) for word in words}
print(words_length)


# 3. Given a list with duplicates, create a set comprehension containing lowercase, normalized valus
duplicate_words = ["Python", "python", "CODE", "Code", "loop", "LOOP"]

normalized_words = {word.lower() for word in duplicate_words}
print(normalized_words)


# 4. Create a dictionary of only products whose price is below a chosen threshold 
products = {"Laptop": 899, "Mouse": 25, "Keyboard": 45, "Monitor": 199, "Webcam": 60, "Headset": 30}

budget_products = {key: value for key, value in products.items() if value <= 50}
print(budget_products)


# 5. Create a dictionary mapping student names to PAS/FAIL from a list of student dictionaries
students = [{"name": "Cory", "active": False, "score": 30},
                 {"name": "Angel", "active": True, "score": 78},
                 {"name": "Andrew", "active": True, "score": 57}]

students_results = {student["name"]: "PASS" if student["score"] >= 50 else "FAIL" for student in students}
print(students_results)