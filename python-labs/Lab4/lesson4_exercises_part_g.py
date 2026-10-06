# Part G, Stretch challenges

# 1. Write a function that returns minimum and maximum from a list without min()/max(), return two values
numbers = [1, -456, 12, 0, -3, 8, 2]

def get_min_and_max(numbers):
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if max_number < number:
            max_number = number
        elif min_number > number:
            min_number = number

    return max_number, min_number

print(get_min_and_max(numbers))


# 2. Write a function that checks whether a word is a palindrome
word_1 = "radar"
word_2 = "ball"
word_3 = "elevator"
word_4 = "civic"
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome(word_1))
print(is_palindrome(word_2))
print(is_palindrome(word_3))
print(is_palindrome(word_4))


# 3. Write a function that counts character frequencies and returns a dictionary
def character_frequencies(word):
    frequencies = {}
    for char in word:
        if char in frequencies:
            frequencies[char] = frequencies[char] + 1
        else:
            frequencies[char] = 1

    return frequencies

print(character_frequencies(word_1))

# 4. Write a function that receives a list of numbers and returns a new dictionary with keys: positive, negative, and zero, containing counts
def positive_negative_zero(numbers):
    numbers_count = {"positive": 0, "negative": 0, "zero": 0}
    for number in numbers:
            if number > 0:
                numbers_count["positive"] = numbers_count["positive"] + 1
            elif number < 0:
                numbers_count["negative"] = numbers_count["negative"] + 1
            else:
                numbers_count["zero"] = numbers_count["zero"] + 1

    return numbers_count

print(positive_negative_zero(numbers))


# 5. Add light type hints and docstring to 5 functions
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers together"""
    return a + b

print(add_numbers(5, 10))

def greet(name: str) -> str:
    """Greets a person using their name"""
    return f"Greetings, {name}!"

print(greet("Matt"))

def is_adult(age: int) -> bool:
    """Checks if person is over 18"""
    return age >= 18

print(is_adult(27))

def average_number(numbers: list) -> float:
    """Gets average number from list of numbers"""
    return round(sum(numbers) / len(numbers), 1)

print(average_number(numbers))

def username_generator(first_name: str, last_name: str, age: int) -> str:
    """Generates username from first_name, last_name, and age"""
    return f"""{first_name[0]}{age}{last_name[::-2]}"""

print(username_generator("Samuel", "Smith", 52))