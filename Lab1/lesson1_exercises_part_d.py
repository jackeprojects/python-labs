# Part D, String investigation

# 1. Predict output before slicing str
input_string = "Prediction"

print(input_string[1])  # "r"
print(input_string[:1])  # "P"
print(input_string[:-1])  # "Predictio"
print(input_string[::-1])  # noitciderP
print(input_string[:-1:2])  # Peito
print(input_string[1:])  # rediction
print(input_string[-1:])  # n
print(input_string[:-1:])  # Predictio


# 2. Produce 6 slices from str
ai = "Artificial Intelligence"

# Prints char at that specific index
print(ai[1])

# No number before ":" (start) indicates to start at beginning of string (first index),
# positive index means counting forward (from start of str),
# stop at index 1 (doesn't print at),
print(ai[:1])

# Negative index means counting backward (from end of string),
# stop at index -1 (equivalent to index 22, doesn't print at),
print(ai[:-1])

# No numbers before second ":" (stop) indicates to stop at end of string (last index),
# but since step is negative (-1) it will instead stop at the beginning of the string
# -1 indicates that every character should be printed, backwards
print(ai[::-1])

# Start from beginning, stop right before last char of string, print every other char
print(ai[:-1:2])

# Start from index 1, stop is empty which means to end of string, no step - meaning every char
print(ai[1:])


# 3. Examples of split(), strip(), replace(), and operator in
id_number = " 19910203 - 1234 "

if "-" in id_number:
    id_date_of_birth, id_birth_number = id_number.split("-")
    id_date_of_birth = id_date_of_birth.strip()
    id_birth_number = id_birth_number.strip()
    print(id_date_of_birth)
    print(id_birth_number)

    id_birth_number_hidden = id_birth_number.replace(id_birth_number, "XXXX")
    print(id_birth_number_hidden)

    id_number_censored = f"{id_date_of_birth}-{id_birth_number_hidden}"
    print (id_number_censored)


# 4. Example and explanation for why you cant change individual char in str
animal = "elephant"
# animal[0] = "E"  # Gives a TypeError, str is immutable, can't change individual chars

new_animal = "E" + animal[1:]
print(new_animal)  # Have to create a new string to change char