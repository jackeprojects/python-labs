# Part D, zip and unpacking

# 1. Combine separate name and score lists using zip and print each pair
names = ["Charles", "Gordon", "Sophie"]
scores = [20, 87, 93]

for name,score in zip(names, scores):
    print(name, score)


# 2. Create a dictionary using dict(zip(keys, values))
keys = ["title", "author", "pages"]
values = ["Dune", "Frank Herbert", 412]
print(dict(zip(keys, values)))


# 3. Combine 3 lists: product name, price, and stock
product_name = ["gpu", "cpu", "ram"]
prices = [8000, 4000, 20000]
stock = [4, 7, 0]

for name, price, quantity in zip(product_name, prices, stock):
    print(name, price, quantity)


# 4. Investigate what happens when zipped lists have different lengths
# Since names only has 3 items,
# the 4th age wont print
ages = [28, 24, 57, 35]
for name, age, in zip(names, ages):
    print(name, age)


# 5. Use tuple unpacking directly in a for loop over zipped data
games = ["Demon's Souls", "Gears 5"]
platforms = ["Playstation 5", "Xbox Series X/S"]
for game, platform in zip(games, platforms):
    print(game, platform)


# 6. Swap two variables without a temporary variable
a = 7
b = 2
print(a, b)

a,b = b, a
print(a, b)