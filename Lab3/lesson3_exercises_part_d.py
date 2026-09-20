# Part D, range, enumerate and nested loops

# 1. Use range to print 10 down to 1
for number in range(10, 0, -1):
    print(number)


# 2. Generate the multiplication table for a number supplied byu by the user
user_number = int(input("Enter a number: "))
for number in range(1, 10):
    print(f"{user_number} x {number} = {user_number * number}")

# 3. Use enumerate to print a playlist with track numbers starting at 1
tracks = ["Weak and Powerless", "Hexagram", "Minerva", "Hole in the Earth"]
for key, value in enumerate(tracks, start=1):
    print(f"{key}. {value}")


# 4. Use nested loops to print coordinate pairs for x=1..3 and y=1..4
for x in range(1,4):
    for y in range(1,5):
        print(x, y, sep=", ")


# 5. Create a 5x5 text grid using nested loops
for row in range(5):
    for column in range(5):
        print("*", end=" ")

    print()