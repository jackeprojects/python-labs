import requests

def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request has timed out")
    except requests.exceptions.ConnectionError:
        print("Could not reach the server")
    except requests.exceptions.HTTPError as error:
        print(f"Error: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("Response was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {type(error).__name__}")
    return None

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