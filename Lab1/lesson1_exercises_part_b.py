# Part B, User input and calculations

from datetime import datetime

# 1. Profile program, ask for name, year of birth, and print approximate age
user_name = input("Whats your name?: ")
user_year = int(input("What year were you born?: "))

current_year = datetime.now().year
approx_age = current_year - user_year
print(f"The approximate age, in {current_year}, for someone born in {user_year} would be {approx_age}")


# 2. Ask for item price, discount percentage, calculate, round and print the final price to 2 decimals
item_price = float(input("Type in a price for an item: "))
item_discount_percentage = float(input("Now type in a discount percentage: "))
item_price_final = item_price - (item_price * (item_discount_percentage / 100))

if item_price_final <= 0:
    print("The final price of the item with the discount applied is: Free")
else:
    print(f"The final price of the item with the discount applied is: {item_price_final:.2f}")


# 3. Ask for a temp in celsius and convert to fahrenheit
celsius = float(input("Type in a temperature (celsius): "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} celsius is {fahrenheit} in fahrenheit")


# 4. Ask for length and width of a room, calculate area and perimeter
room_length = float(input("Type in the length of a room (meters): "))
room_width = float(input("Type in the width of a room (meters): "))
room_area = room_length * room_width
room_perimeter = (room_length + room_width) * 2

print(f"The area of the room is: {room_area}m^2")
print(f"The perimeter of the room is: {room_perimeter}m")


# 5. What happens when user inputs "hello" in area and perimeter calculator
# If the user inputs a str like "hello" instead of a number, calling float(),
# would give a ValueError saying it couldn't convert a str to a float