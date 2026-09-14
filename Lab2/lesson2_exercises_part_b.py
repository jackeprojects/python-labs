# Part B, Tuples and unpacking

# 1. Unpack a tuple representing RGB values, into three variables, and print them
rgb = 0,0,0
red, green, blue = rgb
print(red)
print(green)
print(blue)


# 2. Unpack a tuple containing a person's name, age and city and use the values in a formatted sentence
person = "Alex", 34, "Örebro"

name, age, city = person
print(name)
print(age)
print(city)


# 3. Attempt to change a tuple's element, explain why tuples are useful when values shouldn't be changed
# rgb[0] = 255  # Gives TypeError since tuples are immutable,
# can't reassign values to their elements,
# which is why it's useful when you want to protect data from being changed


# 4. Create a list containing at least four coordinate tuples, access x and y values
coord_1 = 10, 20
coord_2 = 30, 40
coord_3 = 50, 60
coord_4 = 70, 80
coordinates = [coord_1, coord_2, coord_3, coord_4]
print(coordinates[1][0])
print(coordinates[0][1])
print(coordinates[3][1])
print(coordinates[2][0])