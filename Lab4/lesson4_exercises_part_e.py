# Part E, Decomposition

# 1. Build temperature report using functions for celsius-to-fahrenheit, classification, and formatting
def temperature_report(celsius):
    fahrenheit = celsius_to_fahrenheit(celsius)
    weather_state = classification(fahrenheit)
    return format_report(celsius, fahrenheit, weather_state)


def format_report(celsius, fahrenheit, weather_state):
    return f"It's {weather_state} outside ({celsius}C / {fahrenheit}F)"


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def classification(fahrenheit):
    if fahrenheit <= 52:
        return "cold"
    elif fahrenheit <= 84:
        return "warm"
    else:
        return "hot"

print(temperature_report(25))


# 2. Build order calculation using separate functions for subtotal, discount, and final total
def order(price, quantity, price_discount=0):
    sub = subtotal(price, quantity)
    disc = discount(sub, price_discount)
    total = final_total(disc)
    return total


def subtotal(price, quantity):
    return price * quantity


def discount(price, price_discount):
    return price - price_discount


def final_total(price):
    return f"Your total is {price}"

print(order(17, 7, 11))


# 3. Refactor one earlier exercise that contains repeated code into at least three functions
media1 = {"title": "The Legend of Zelda: Breath of the Wild", "category": "Game", "release_year": 2017, "genre": "Adventure"}
media2 = {"title": "Inception", "category": "Movie", "release_year": 2010, "genre": "Sci-Fi"}
media3 = {"title": "Dune", "category": "Book", "release_year": 1965, "genre": "Sci-Fi"}
media4 = {"title": "The Witcher 3: Wild Hunt", "category": "Game", "release_year": 2015, "genre": "RPG"}
media5 = {"title": "The Dark Knight", "category": "Movie", "release_year": 2008, "genre": "Action"}
media6 = {"title": "1984", "category": "Book", "release_year": 1949, "genre": "Dystopian"}
media7 = {"title": "Hades", "category": "Game", "release_year": 2020, "genre": "Roguelike"}
media8 = {"title": "Parasite", "category": "Movie", "release_year": 2019, "genre": "Thriller"}

media_catalogue = [media1, media2, media3, media4, media5, media6, media7, media8]

def format_media_summary(item):
    return f"{item['title']} ({item['release_year']}) - {item['category']}, {item['genre']}"


def print_media_summary(item):
    print(format_media_summary(item))


def print_catalogue(catalogue):
    for item in catalogue:
        print_media_summary(item)

print_catalogue(media_catalogue)


# 4. Write a main-like section at that calls your functions in a clear sequence
print("TEMPERATURE REPORT\n--------------------")
print(f"{temperature_report(25)}\n")

print("ORDER CALCULATION\n--------------------")
print(f"{order(17, 7, 11)}\n")

print("MEDIA CATALOGUE\n--------------------")
print_catalogue(media_catalogue)