# Part E, Applied challenge: Registration summary

from datetime import datetime

# 1. & 2. Collect first & last name, city, year of birth, and fav programming language
first_name = input("What's your first name?: ").strip()
last_name = input("What's your last name?: ").strip()
city = input("What city do you live in?: ").strip()
birth_year = input("What year were you born?: ").strip()
programming_language = input("What's your favorite programming language?: ").strip()


# 3. Create a user id from parts of name, and year of birth
username = first_name[:3] + last_name[-3:] + birth_year[-2:]


# 4. Print clean multi-line summary using f-strings.
print(f"""
Name: {first_name} {last_name}
City : {city}
Birth year: {birth_year}
Programming language: {programming_language}
Username: {username}
""")


# 5. Print initials, name length excluding the space, and programming language reversed
print(first_name[0] + last_name[0])
print(len(first_name) + len(last_name))
print(programming_language[::-1])


# 6. Three extra derived pieces of information
age = datetime.now().year - int(birth_year)
print(f"You are {age} years old!")

city_name_length = len(city.replace(" ", ""))
print(f"Your city's name has {city_name_length} characters!")

if first_name[0].lower() == programming_language[0].lower():
    print(f"Your name and favorite programming language starts with the same character!")