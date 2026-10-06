# Part C, Positional unpacking

# 1. Create a list[10, 20, 30], unpack it into a function expecting 3 positional parameters
packed_list = [10, 20, 30]
def unpacker(item_1, item_2, item_3):
    print(item_1)
    print(item_2)
    print(item_3)

unpacker(*packed_list)


# 2. Create a tuple containing first_name, last_name, city and call a function using *tuple
person = ("John", "Doe", "Copenhagen")

def packer(first_name, last_name, city):
    return f"{first_name} {last_name}, {city}"

print(packer(*person))


# 3. Use starred assignment: first, *middle, last = values, test with several list lengths
values = [1, 5, 2, 5, 78]
first, *middle, last = values

print(first)
print(middle)
print(last)

names = ["Adam", "Joan", "Joseph", "Katja"]
first, *middle, last = names

print(first)
print(middle)
print(last)

answers = [True, False, False, False, True, False]
first, *middle, last = answers

print(first)
print(middle)
print(last)

# 4. Explain the difference between * in a function definition and * in a function call
# *args as a parameter will pack the corresponding arguments into a tuple,
# while *args as an argument will unpack a list/tuple into the corresponding vars