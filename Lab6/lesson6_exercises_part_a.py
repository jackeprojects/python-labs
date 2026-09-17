# Part A, List comprehensions

# 1. Create squares for number 1-20 using a normal loop, then list comprehension
squares_loop = []
for number in range(1, 21):
    squares_loop.append(number ** 2)

print(squares_loop)

squares_comprehension = [number ** 2 for number in range(1,21)]
print (squares_comprehension)


# 2. Create a lits containing only even numbers from 1-100
even_numbers = [number for number in range(1,101) if number % 2 == 0]
print(even_numbers)


# 3. Convert a list of names to stripped, title-cased names
collected_names = [" jason ", " moe", "john "]
fixed_names = [name.strip().title() for name in collected_names]
print(fixed_names)


# 4. Given scores, create a list containing only passing scores
all_scores = [60, 20, 78, 10, 72, 80, 96, 32]
passing_scores_1 = [score for score in all_scores if score >= 50]
print(passing_scores_1)


# 5. Create labels such as PASS/FAIL for every score using a condition expression in a comprehension
passing_scores_2 = ["PASS" if score >= 50 else "FAIL" for score in all_scores]
print(passing_scores_2)


# 6. Rewrite 3 earlier loop_based transformations fomr Lessons 2-4 as comprehensions
words = ["apple", "sofisticated", "elevator", "stapler", "ore", "burrow"]
minimum_length = 8
long_words = [word for word in words if len(word) >= minimum_length]
print(long_words)

students_list = [{"name": "Cory", "active": False, "score": 30},
                 {"name": "Angel", "active": True, "score": 78},
                 {"name": "Andrew", "active": True, "score": 57}]

active_users = [user for user in students_list if user["active"]]
print(active_users)

average_score = sum([student["score"] for student in students_list]) / len(students_list)
print(average_score)