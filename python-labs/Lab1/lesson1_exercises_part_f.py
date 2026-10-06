# Part F, Stretch challenges Python Foundation

# 1. Converts input seconds to hours, remaining minutes and seconds using // and %

total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600  # 3600 seconds in an hour
remaining = total_seconds % 3600
minutes = remaining // 60  # 60 minutes in one hour
seconds = remaining % 60  # 60 seconds in one minute

print(f"Total seconds: {total_seconds}")
print(f"{hours}h : {minutes}m : {seconds}s")


# 2. Given a four-digit-integer, extract and print each digit
four_digit_number = 4432

first_digit = (four_digit_number % 10000) // 1000
second_digit = (four_digit_number % 1000) // 100
third_digit = (four_digit_number % 100) // 10
fourth_digit = four_digit_number % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)


# 3. Masks text input while keeping first two and last two chars unmasked
text = input("Input text: ")

if len(text) > 4:
    middle_length = len(text) - 4
    masked_text = text[:2] + "*" * middle_length + text[-2:]
    print(masked_text)
else:
    print("Text needs to be more than 3 characters!")


# 4. "Predict before running" examples
number = "42"
print(int(number) - 17)  # 25

animal = "Elephant"
print(animal[2:5])  # "pha"

text = "Python"
print(text[::-1])  # "nohtyP"

total = 13
print(f"{total // 10}, {total % 10}")  #1, 3

sentence = "  Hello World!   "
print(sentence.strip().lower())  # "hello world"