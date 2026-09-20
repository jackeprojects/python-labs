# Part G, Stretch challenges

# 1. Flatten a list using comprehension
greetings = ["hi", "hello", "greetings"]
goodbyes = ["bye", "goodbye", "see you later"]
interactions =  [greetings, goodbyes]
print(interactions)

interactions_flattened = [amount for lists in interactions for amount in lists]
print(interactions_flattened)


# 2. Create a multiplication table using a nested comprehension, then decide if result is readable enough
table = [[row * column for row in range(1,6)] for column in range(1,6)]
print(table)

# Personally I think it's clear enough,
# but it would be clearer if written normally as a nested loop
# since the logic in the comprehension is packed into one line



# 3. Given names and scores, create only passing students dictionaries in one readable comprehension
students = [{"name": "Cory", "score": 30},
            {"name": "Angel", "score": 78},
            {"name": "Andrew", "score": 57}]

student_names = ["Cory", "Angel", "Andrew"]
student_scores = [30, 78, 57]

student_results = [{"name": name, "score": score} for name, score in zip(student_names, student_scores) if score >= 50]
print(student_results)


# 4. Use any() and all() to answer useful questions about a score list, after first solving them with loops
everyone_passed_if = True
for score in student_scores:
    if score < 50:
        everyone_passed_if = False

print(everyone_passed_if)

someone_failed = any(score < 50 for score in student_scores)
print (someone_failed)

everyone_passed_all = all(score >= 50 for score in student_scores)
print (everyone_passed_all)



# 5. Create 5 examples where Pythonic syntax reduces boilerplate without reducing clarity
# Example 1
passing_scores_1 = []
for score in student_scores:
    if score >= 50:
        passing_scores_1.append(score)

print(passing_scores_1)

passing_scores_2 = [score for score in student_scores if score >= 50]
print(passing_scores_2)

# Example 2
total_score_1 = 0
for score in student_scores:
    total_score_1 += score

print(total_score_1)

total_score_2 = sum(student_scores)
print(total_score_2)

# Example 3
for i in range(len(student_scores)):
    print(i, student_scores[i])

for key, value in enumerate(student_scores):
    print(key, value)

# Example 4
def get_score(student):
    return student["score"]

sorted_score_1 = sorted(students, key=get_score)
print(sorted_score_1)

sorted_score_2 = sorted(students, key=lambda student: student["score"])
print(sorted_score_2)

# Example 5
print("Student " + students[0]["name"] + " has the score " + str(students[0]["score"]))

print(f"Student {students[0]['name']} has the score {students[0]['score']}")