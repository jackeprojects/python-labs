# Part F, Applied challenge: Data cleanup

# 1. Start with a list of 12 dictionaries representing products, with messy name and category, price, and stock
messy_products = [
    {"name": "  laptop", "category": "ELECTRONICS", "price": 12000, "stock": 4},
    {"name": "MOUSE ", "category": "electronics", "price": 350, "stock": 0},
    {"name": "Keyboard", "category": "Electronics", "price": 800, "stock": 6},
    {"name": " monitor ", "category": "ELECTRONICS", "price": 3200, "stock": 3},
    {"name": "HEADSET", "category": "electronics", "price": 950, "stock": 0},
    {"name": "webcam  ", "category": "Electronics", "price": 1100, "stock": 5},
    {"name": "Desk Chair", "category": "  furniture", "price": 2500, "stock": 2},
    {"name": "  bookshelf", "category": "FURNITURE", "price": 1800, "stock": 0},
    {"name": "COFFEE TABLE", "category": "furniture ", "price": 2200, "stock": 1},
    {"name": "cutting board", "category": "KITCHENWARE", "price": 150, "stock": 20},
    {"name": " Mixing Bowl ", "category": "kitchenware", "price": 200, "stock": 15},
    {"name": "SAUCEPAN", "category": "Kitchenware", "price": 400, "stock": 0}
]


# 2. Create a cleaned list where names/categories are normalized, use comprehensions where readable
products = [{"name": product["name"].strip().title(),
            "category": product["category"].strip().title(),
            "price": product["price"],
            "stock": product["stock"]} for product in messy_products]
print(products)


# 3. Create a list of in-stock products
in_stock = [product for product in products if product["stock"] > 0]
print(in_stock)


# 4. Create a set of unique normalized categories
#categories = {product["category"].strip().title() for product in products}
unique_categories = {product["category"] for product in products}
print(type(unique_categories))


# 5. Create a dictionary mapping product name to inventory value (price * stock)
value = {product["name"]: product["price"] * product["stock"] for product in products}
print(value)


# 6. Sort products by inventory value from highest to lowest
print()
value_sorted = sorted(value.items(), key=lambda product: product[1], reverse=True)
print(value_sorted)


# 7. Use enumerate to print a ranked report
def ranked_report(sorted_list):
    for position, product in enumerate(sorted_list, start=1):
        print(f"{position}. {product[0]}: {product[1]}")

ranked_report(value_sorted)


# 8. Use zip to combine at least one pair of separate derived lists in a meaningful way
product_names = [product["name"] for product in products]
product_stock = [product["stock"] for product in products]

def zip_and_print(item_1, item_2):
    for value_1, value_2, in zip(item_1, item_2):
        print(f"{value_1} | {value_2}")

zip_and_print(product_names, product_stock)


# 9. Write a over-complecated comprehension, a clearer alternative, and explain why cleaner version wins
overcomplicated = [value for product in products for key, value in product.items() if key == "name"]
simplified = [product["name"] for product in products]

print(overcomplicated)
print(simplified)

# simpler version accesses the key directly by key,
# instead of looping it to compare every key to the one we want