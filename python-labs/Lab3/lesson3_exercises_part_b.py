# Part B, Truthy, falsy and membership

# 1. Create exmaples with empty string, non-empty string, zero, non-zero integer,
# empty list and non-empty list, test each directly in if statement
def is_empty(example):
    if example:
        return f"truthy"
    else:
        return f"falsy"

empty_string = ""
non_empty_string = " "
none = None
zero_int = 0
non_zero_int = -1
empty_list = []
non_empty_list = ["apple"]
print(is_empty(empty_string))
print(is_empty(non_empty_string))
print(is_empty(none))
print(is_empty(zero_int))
print(is_empty(non_zero_int))
print(is_empty(empty_list))
print(is_empty(non_empty_list))


# 2. Ask for a language check whether it exists in a predefined list of supported languages
languages = ["english", "swedish", "german"]
language = input("Enter a language: ").lower()

if language not in languages:
    print(f"{language} is a not supported language!")
else:
    print(f"{language.capitalize()} is a supported language!")


# 3. Create a list of blocked usernames and reject a supplied username if it appears in the list
blocked_usernames = ["alligator1", "crocodile2", "test3"]

username = input("Enter a username: ")

if username not in blocked_usernames:
    print(f"Your username is {username}!")
else:
    print("That username is blocked!")

# 4. Use not to express at least 2 conditions in a readable way
age = int(input("What's your age?: "))
if not age >= 18:
    print("You're not an adult")
if not age <= 65:
    print("You're a senior")