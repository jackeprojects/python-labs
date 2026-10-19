from api_client import get_json
import requests

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


# 4. Create and change a product
new_product = {
    "title": "RTX 5090",
    "price": 999999,
    "description": "A Graphics Card",
    "category": "electronics",
    "image": "https://cdn.inet.se/img/800x10000/cms/55413314-e5f2-4420-bac7-8cc4b619330e.webp"
}

response = requests.post("https://fakestoreapi.com/products", json=new_product, timeout=5)
if response.ok:
    print(response.status_code)
    print(response.json())
else:
    print(f"Could not create product: {response.status_code}")

updated_price = {"price": 9}

response = requests.patch("https://fakestoreapi.com/products/7", json=updated_price, timeout=5)
if response.ok:
    print(response.status_code)
    print(response.json())
else:
    print(f"Could not update product: {response.status_code}")


# 5. Break it on purpose
get_json("https://fakestoreapi.com/produkt")  # Error: 404
get_json("https://fakestoreapi.com/products", timeout=0.001)  # The request has timed out
get_json("https://superfakedomain64.com")  # Could not reach the server