# Part D, Functions and collections

# 1. Write calculate_total(numbers) manually using loop
def calculate_total(numbers):
    numbers_sum = 0
    for number in numbers:
        numbers_sum += number

    return numbers_sum

number_list = [2, 3, 1, 43, 12, 6, 2]
print(calculate_total(number_list))


# 2. Write count_even(numbers)
def count_even(numbers):
    even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers += 1

    return even_numbers

print(count_even(number_list))


# 3. Write get_long_word(words, minimum_length), return new list
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)

    return long_words

word_list = ["apple", "sofisticated", "elevator", "stapler", "ore", "burrow"]

print(get_long_words(word_list, 8))


# 4. Write find_student(students, name) where students is list of dicionaries, return matching or none
def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None

students_list = [{"name": "Cory", "active": False, "score": 30},
                 {"name": "Angel", "active": True, "score": 78},
                 {"name": "Andrew", "active": True, "score": 57}]

print(find_student(students_list, "Cory"))
print(find_student(students_list, "Johnny"))


# 5. Write average_score(students) for a list of dictionaries containing scores
def average_score(students):
    scores_sum = 0
    for student in students:
        scores_sum += student["score"]

    return scores_sum / len(students)

print(average_score(students_list))


# 6. Write get_active_users(users), return only dictionaries where active is True
def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)

    return active_users

print(get_active_users(students_list))