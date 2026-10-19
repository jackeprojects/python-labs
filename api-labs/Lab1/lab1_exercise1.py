from api_client import get_json

# 1. Sort products by price
products = get_json("https://fakestoreapi.com/products")

sorted_products = sorted(products, key=lambda product: product["price"])

for product in sorted_products:
    print(f"{product['title']}: {product['price']}")


# 2. Look at the categories
categories = get_json("https://fakestoreapi.com/products/categories")

print("\n", categories)
chosen_category = input("Enter in one of the categories: ")

if chosen_category:
    category = get_json(f"https://fakestoreapi.com/products/category/{chosen_category}")

    if category:
        sorted_category = sorted(category, key=lambda product: product["price"], reverse=True)

        print(f"Total products in {chosen_category}: {len(category)}")
        print(f"Cheapest product: {sorted_category[-1]['title']}: {sorted_category[-1]['price']}")
    else:
        print("That category does not exist")


# 3. Move get_json to its own file
# get_json has been moved into api_client.py