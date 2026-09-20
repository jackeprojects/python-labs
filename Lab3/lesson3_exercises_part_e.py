# Part E, While loops

# 1. Create a countdown from 10 to 0
count = 10
while count >= 0:
    print(count)
    count -= 1


# 2. Ask repeatedly for a password until the correct password is entered
passwords = ["pass1", "thisIsNotAPassWord"]
password_valid = False
while not password_valid:
    input_password = input("Enter your password: ")
    if input_password in passwords:
        password_valid = True
        print("Success, you are now logged in")
    else:
        print("Incorrect password")


# 3. Create a menu that repeats until the user chooses 'quit', the menu can simply print which options was selected
quit_loop = True
while quit_loop:
    print("1. Create new note")
    print("2. Delete note")
    print("3. Quit")
    choice = input("Select an option: ")
    if choice == "1":
        print("Created note!")
    elif choice == "2":
        print("Deleted note!")
    elif choice == "3":
        quit_loop = False


# 4. Ask the user for numbers until they enter 0, keep a running total
numbers_loop = True
numbers_total = 0
while numbers_loop:
        numbers_input = int(input("Enter the number '0' to quit: "))
        numbers_total += numbers_input
        if numbers_input == 0:
            numbers_loop = False
            print(f"Your total is: {numbers_total}")


# 5. Create a guessing loop with a fixed secret number, tell the user whether each guess is too high or too low
answer_to_life = 42
correct = False

while not correct:
    guess = int(input("Guess the secret number: "))
    if guess == answer_to_life:
        correct = True
        print("Correct")
    elif guess > answer_to_life:
        print("Too high")
    else:
        print("Too low")