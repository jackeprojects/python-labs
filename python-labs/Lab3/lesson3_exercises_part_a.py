# Part A, Conditions

# 1. Write a program that classifies a number as positive, negative, or zero
number = float(input("Input a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. Ask for age and classify it into 4 age groups using using if/elif/else
age = int(input("What's your age?: "))
if age < 18:
    print("Minor")
elif age >= 18 and age <= 29:
    print("Young Adult")
elif age >= 30 and age <= 64:
    print("Adult")
else:
    print("Senior")


# 3. Create a login check using a stored username and password. both must match
stored_username = "notMyPassword"
stored_password = "notMyUsername"
username = input("Input your username: ")
if username != stored_username:
    print(f"Could not find a user with the username \"{username}\"")
else:
    password = input("Input your password: ")
    if password != stored_password:
        print("Incorrect password!")
    else:
        print(f"You've succesfully logged in! Welcome, {username}.")


# 4. Given a score from 0-100, print a grade using 5 ranges
score = int(input("From 0-100, input your score: "))
if score >= 0 and score <= 20:
    print("You suck.")
elif score > 20 and score <= 40:
    print("Bad.")
elif score > 40 and score <= 60:
    print("Not the worst.")
elif score > 60 and score <= 80:
    print("You can do better.")
elif score > 80 and score <= 100:
    print("Acceptable.")
else:
    print(f"{score} isn't a valid score")


# 5. Create a shipping rule based on order total and whether the customer is a member, use and/or
order_total = float(input("What's your order total?: "))
is_member = input("Type \"y\" if you are a member: ")

if order_total > 250 and is_member == "y":
    print("Free shipping for your purchase above 250")
else:
    print("Standard shipping fee")


# 6. Write 5 expressions using ==, !=, >, <, >=, <=, and predict each boolean result
print(7 == 8)  # False
print(5 != 3)  # True
print(10 > 7)  # True
print(5 < 5)  # False
print(1 >= 45)  # False
print(56 <= 2)  # False